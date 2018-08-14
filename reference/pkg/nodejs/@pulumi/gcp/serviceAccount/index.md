---
title: Module serviceAccount
---

<a href="../index.html">@pulumi/gcp</a> &gt; serviceAccount

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#IAMBinding">class IAMBinding</a>
* <a href="#IAMMember">class IAMMember</a>
* <a href="#IAMPolicy">class IAMPolicy</a>
* <a href="#Key">class Key</a>
* <a href="#getAccount">function getAccount</a>
* <a href="#getAccountKey">function getAccountKey</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#GetAccountArgs">interface GetAccountArgs</a>
* <a href="#GetAccountKeyArgs">interface GetAccountKeyArgs</a>
* <a href="#GetAccountKeyResult">interface GetAccountKeyResult</a>
* <a href="#GetAccountResult">interface GetAccountResult</a>
* <a href="#IAMBindingArgs">interface IAMBindingArgs</a>
* <a href="#IAMBindingState">interface IAMBindingState</a>
* <a href="#IAMMemberArgs">interface IAMMemberArgs</a>
* <a href="#IAMMemberState">interface IAMMemberState</a>
* <a href="#IAMPolicyArgs">interface IAMPolicyArgs</a>
* <a href="#IAMPolicyState">interface IAMPolicyState</a>
* <a href="#KeyArgs">interface KeyArgs</a>
* <a href="#KeyState">interface KeyState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts">serviceAccount/account.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts">serviceAccount/getAccount.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts">serviceAccount/getAccountKey.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts">serviceAccount/iAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts">serviceAccount/iAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts">serviceAccount/iAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts">serviceAccount/key.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L9">class Account</a>
</h2>

Allows management of a [Google Cloud Platform service account](https://cloud.google.com/compute/docs/access/service-accounts)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L56">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L26">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


The service account ID.
Changing this forces a new service account to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L31">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string | undefined>;
```


The display name for the service account.
Can be updated without creating a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L37">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


The e-mail address of the service account. This value
should be referenced from any `google_iam_policy` data sources
that would grant the service account privileges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The fully-qualified name of the service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L47">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string | undefined>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the service account. The policy will be
merged with any existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L52">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L56">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```


The unique id of the service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L19">class IAMBinding</a>
</h2>

When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource to configure permissions for who can edit the service account. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the [google_project_iam](google_project_iam.html) set of resources.

Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:

* `google_service_account_iam_policy`: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.
* `google_service_account_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.
* `google_service_account_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.

~> **Note:** `google_service_account_iam_policy` **cannot** be used in conjunction with `google_service_account_iam_binding` and `google_service_account_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_service_account_iam_binding` resources **can be** used in conjunction with `google_service_account_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L46">constructor</a>
</h3>

```typescript
new IAMBinding(name: string, args: IAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMBindingState): IAMBinding
```


Get an existing IAMBinding resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L35">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L36">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L42">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L46">property serviceAccountId</a>
</h3>

```typescript
public serviceAccountId: pulumi.Output<string>;
```


The service account id to apply policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L19">class IAMMember</a>
</h2>

When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource to configure permissions for who can edit the service account. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the [google_project_iam](google_project_iam.html) set of resources.

Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:

* `google_service_account_iam_policy`: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.
* `google_service_account_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.
* `google_service_account_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.

~> **Note:** `google_service_account_iam_policy` **cannot** be used in conjunction with `google_service_account_iam_binding` and `google_service_account_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_service_account_iam_binding` resources **can be** used in conjunction with `google_service_account_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L46">constructor</a>
</h3>

```typescript
new IAMMember(name: string, args: IAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMMemberState): IAMMember
```


Get an existing IAMMember resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L35">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L36">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L42">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L46">property serviceAccountId</a>
</h3>

```typescript
public serviceAccountId: pulumi.Output<string>;
```


The service account id to apply policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L19">class IAMPolicy</a>
</h2>

When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource to configure permissions for who can edit the service account. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the [google_project_iam](google_project_iam.html) set of resources.

Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:

* `google_service_account_iam_policy`: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.
* `google_service_account_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.
* `google_service_account_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.

~> **Note:** `google_service_account_iam_policy` **cannot** be used in conjunction with `google_service_account_iam_binding` and `google_service_account_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_service_account_iam_binding` resources **can be** used in conjunction with `google_service_account_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L44">constructor</a>
</h3>

```typescript
new IAMPolicy(name: string, args: IAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMPolicyState): IAMPolicy
```


Get an existing IAMPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L35">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L40">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L44">property serviceAccountId</a>
</h3>

```typescript
public serviceAccountId: pulumi.Output<string>;
```


The service account id to apply policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Key">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L10">class Key</a>
</h2>

Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L84">constructor</a>
</h3>

```typescript
new Key(name: string, args: KeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Key resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyState): Key
```


Get an existing Key resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L29">property keyAlgorithm</a>
</h3>

```typescript
public keyAlgorithm: pulumi.Output<string | undefined>;
```


The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
[ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
(only used on create)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name used for this key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L40">property pgpKey</a>
</h3>

```typescript
public pgpKey: pulumi.Output<string | undefined>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating or importing a new key pair. May either be
a base64-encoded public key or a `keybase:keybaseusername` string for looking up
in Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L46">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string>;
```


The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
service account keys through the CLI or web console. This is only populated when creating a new key, and when no
`pgp_key` is provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L52">property privateKeyEncrypted</a>
</h3>

```typescript
public privateKeyEncrypted: pulumi.Output<string>;
```


The private key material, base 64 encoded and
encrypted with the given `pgp_key`. This is only populated when creating a new
key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L57">property privateKeyFingerprint</a>
</h3>

```typescript
public privateKeyFingerprint: pulumi.Output<string>;
```


The MD5 public key fingerprint for the encrypted
private key. This is only populated when creating a new key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L61">property privateKeyType</a>
</h3>

```typescript
public privateKeyType: pulumi.Output<string | undefined>;
```


The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L65">property publicKey</a>
</h3>

```typescript
public publicKey: pulumi.Output<string>;
```


The public key, base64 encoded

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L69">property publicKeyType</a>
</h3>

```typescript
public publicKeyType: pulumi.Output<string | undefined>;
```


The output format of the public key requested. X509_PEM is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L75">property serviceAccountId</a>
</h3>

```typescript
public serviceAccountId: pulumi.Output<string>;
```


The Service account id of the Key Pair. This can be a string in the format
`{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L79">property validAfter</a>
</h3>

```typescript
public validAfter: pulumi.Output<string>;
```


The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L84">property validBefore</a>
</h3>

```typescript
public validBefore: pulumi.Output<string>;
```


The key can be used before this timestamp.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h2 class="pdoc-module-header" id="getAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L10">function getAccount</a>
</h2>

```typescript
getAccount(args: GetAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetAccountResult>
```


Get the service account from a project. For more information see
the official [API](https://cloud.google.com/compute/docs/access/service-accounts) documentation.

<h2 class="pdoc-module-header" id="getAccountKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L10">function getAccountKey</a>
</h2>

```typescript
getAccountKey(args: GetAccountKeyArgs, opts?: pulumi.InvokeOptions): Promise<GetAccountKeyResult>
```


Get service account public key. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get).

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L138">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L143">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


The service account ID.
Changing this forces a new service account to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L148">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the service account.
Can be updated without creating a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L154">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the service account. The policy will be
merged with any existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L159">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project that the service account will be created in.
Defaults to the provider project configuration.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L97">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L102">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The service account ID.
Changing this forces a new service account to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L107">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the service account.
Can be updated without creating a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L113">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The e-mail address of the service account. This value
should be referenced from any `google_iam_policy` data sources
that would grant the service account privileges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The fully-qualified name of the service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L123">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the service account. The policy will be
merged with any existing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L128">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/account.ts#L132">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```


The unique id of the service account.

<h2 class="pdoc-module-header" id="GetAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L20">interface GetAccountArgs</a>
</h2>

A collection of arguments for invoking getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L24">property accountId</a>
</h3>

```typescript
accountId: string;
```


The Service account id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L29">property project</a>
</h3>

```typescript
project?: string;
```


The ID of the project that the service account will be created in.
Defaults to the provider project configuration.

<h2 class="pdoc-module-header" id="GetAccountKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L21">interface GetAccountKeyArgs</a>
</h2>

A collection of arguments for invoking getAccountKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L26">property project</a>
</h3>

```typescript
project?: string;
```


The ID of the project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L30">property publicKeyType</a>
</h3>

```typescript
publicKeyType?: string;
```


The output format of the public key requested. X509_PEM is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L36">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId: string;
```


The Service account id of the Key Pair. This can be a string in the format
`{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.

<h2 class="pdoc-module-header" id="GetAccountKeyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L42">interface GetAccountKeyResult</a>
</h2>

A collection of values returned by getAccountKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L55">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L43">property keyAlgorithm</a>
</h3>

```typescript
keyAlgorithm: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L47">property name</a>
</h3>

```typescript
name: string;
```


The name used for this key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccountKey.ts#L51">property publicKey</a>
</h3>

```typescript
publicKey: string;
```


The public key, base64 encoded

<h2 class="pdoc-module-header" id="GetAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L35">interface GetAccountResult</a>
</h2>

A collection of values returned by getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L39">property displayName</a>
</h3>

```typescript
displayName: string;
```


The display name for the service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L45">property email</a>
</h3>

```typescript
email: string;
```


The e-mail address of the service account. This value
should be referenced from any `google_iam_policy` data sources
that would grant the service account privileges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L49">property name</a>
</h3>

```typescript
name: string;
```


The fully-qualified name of the service account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/getAccount.ts#L53">property uniqueId</a>
</h3>

```typescript
uniqueId: string;
```


The unique id of the service account.

<h2 class="pdoc-module-header" id="IAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L108">interface IAMBindingArgs</a>
</h2>

The set of arguments for constructing a IAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L109">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L115">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L119">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="IAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L87">interface IAMBindingState</a>
</h2>

Input properties used for looking up and filtering IAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L91">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L92">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L98">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMBinding.ts#L102">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId?: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="IAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L108">interface IAMMemberArgs</a>
</h2>

The set of arguments for constructing a IAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L109">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L115">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L119">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="IAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L87">interface IAMMemberState</a>
</h2>

Input properties used for looking up and filtering IAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L91">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L92">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L98">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_service_account_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMMember.ts#L102">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId?: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="IAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L99">interface IAMPolicyArgs</a>
</h2>

The set of arguments for constructing a IAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L104">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L108">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="IAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L80">interface IAMPolicyState</a>
</h2>

Input properties used for looking up and filtering IAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L84">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the service account IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L89">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/iAMPolicy.ts#L93">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId?: pulumi.Input<string>;
```


The service account id to apply policy to.

<h2 class="pdoc-module-header" id="KeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L203">interface KeyArgs</a>
</h2>

The set of arguments for constructing a Key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L210">property keyAlgorithm</a>
</h3>

```typescript
keyAlgorithm?: pulumi.Input<string>;
```


The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
[ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
(only used on create)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L217">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating or importing a new key pair. May either be
a base64-encoded public key or a `keybase:keybaseusername` string for looking up
in Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L221">property privateKeyType</a>
</h3>

```typescript
privateKeyType?: pulumi.Input<string>;
```


The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L225">property publicKeyType</a>
</h3>

```typescript
publicKeyType?: pulumi.Input<string>;
```


The output format of the public key requested. X509_PEM is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L231">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId: pulumi.Input<string>;
```


The Service account id of the Key Pair. This can be a string in the format
`{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.

<h2 class="pdoc-module-header" id="KeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L135">interface KeyState</a>
</h2>

Input properties used for looking up and filtering Key resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L142">property keyAlgorithm</a>
</h3>

```typescript
keyAlgorithm?: pulumi.Input<string>;
```


The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
[ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
(only used on create)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L146">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name used for this key pair

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L153">property pgpKey</a>
</h3>

```typescript
pgpKey?: pulumi.Input<string>;
```


An optional PGP key to encrypt the resulting private
key material. Only used when creating or importing a new key pair. May either be
a base64-encoded public key or a `keybase:keybaseusername` string for looking up
in Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L159">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```


The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
service account keys through the CLI or web console. This is only populated when creating a new key, and when no
`pgp_key` is provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L165">property privateKeyEncrypted</a>
</h3>

```typescript
privateKeyEncrypted?: pulumi.Input<string>;
```


The private key material, base 64 encoded and
encrypted with the given `pgp_key`. This is only populated when creating a new
key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L170">property privateKeyFingerprint</a>
</h3>

```typescript
privateKeyFingerprint?: pulumi.Input<string>;
```


The MD5 public key fingerprint for the encrypted
private key. This is only populated when creating a new key and `pgp_key` is supplied

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L174">property privateKeyType</a>
</h3>

```typescript
privateKeyType?: pulumi.Input<string>;
```


The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L178">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


The public key, base64 encoded

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L182">property publicKeyType</a>
</h3>

```typescript
publicKeyType?: pulumi.Input<string>;
```


The output format of the public key requested. X509_PEM is the default output format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L188">property serviceAccountId</a>
</h3>

```typescript
serviceAccountId?: pulumi.Input<string>;
```


The Service account id of the Key Pair. This can be a string in the format
`{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L192">property validAfter</a>
</h3>

```typescript
validAfter?: pulumi.Input<string>;
```


The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serviceAccount/key.ts#L197">property validBefore</a>
</h3>

```typescript
validBefore?: pulumi.Input<string>;
```


The key can be used before this timestamp.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

