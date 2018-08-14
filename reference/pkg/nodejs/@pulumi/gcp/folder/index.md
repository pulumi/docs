---
title: Module folder
---

<a href="../index.html">@pulumi/gcp</a> &gt; folder

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IAMBinding">class IAMBinding</a>
* <a href="#IAMMember">class IAMMember</a>
* <a href="#IAMPolicy">class IAMPolicy</a>
* <a href="#OrganizationPolicy">class OrganizationPolicy</a>
* <a href="#IAMBindingArgs">interface IAMBindingArgs</a>
* <a href="#IAMBindingState">interface IAMBindingState</a>
* <a href="#IAMMemberArgs">interface IAMMemberArgs</a>
* <a href="#IAMMemberState">interface IAMMemberState</a>
* <a href="#IAMPolicyArgs">interface IAMPolicyArgs</a>
* <a href="#IAMPolicyState">interface IAMPolicyState</a>
* <a href="#OrganizationPolicyArgs">interface OrganizationPolicyArgs</a>
* <a href="#OrganizationPolicyState">interface OrganizationPolicyState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts">folder/iAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts">folder/iAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts">folder/iAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts">folder/organizationPolicy.ts</a> 


<h2 class="pdoc-module-header" id="IAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L14">class IAMBinding</a>
</h2>

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L49">constructor</a>
</h3>

```typescript
new IAMBinding(name: string, args: IAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L30">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the folder's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L34">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L43">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```


An array of identites that will be granted the privilege in the `role`.
Each entry can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L49">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_folder_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L15">class IAMMember</a>
</h2>

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be. Similarly, roles controlled by `google_folder_iam_binding`
   should not be assigned to using `google_folder_iam_member`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L49">constructor</a>
</h3>

```typescript
new IAMMember(name: string, args: IAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L24">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L31">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the folder's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L35">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L44">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```


The identity that will be granted the privilege in the `role`.
This field can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L49">property role</a>
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

<h2 class="pdoc-module-header" id="IAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L10">class IAMPolicy</a>
</h2>

Allows creation and management of the IAM policy for an existing Google Cloud
Platform folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L36">constructor</a>
</h3>

```typescript
new IAMPolicy(name: string, args: IAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L26">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the folder's IAM policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L30">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L36">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="OrganizationPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L12">class OrganizationPolicy</a>
</h2>

Allows management of Organization policies for a Google Folder. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/folders/setOrgPolicy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L57">constructor</a>
</h3>

```typescript
new OrganizationPolicy(name: string, args: OrganizationPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OrganizationPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationPolicyState): OrganizationPolicy
```


Get an existing OrganizationPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L28">property booleanPolicy</a>
</h3>

```typescript
public booleanPolicy: pulumi.Output<{ ... } | undefined>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L32">property constraint</a>
</h3>

```typescript
public constraint: pulumi.Output<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L40">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The resource name of the folder to set the policy for. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L45">property listPolicy</a>
</h3>

```typescript
public listPolicy: pulumi.Output<{ ... } | undefined>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L49">property restorePolicy</a>
</h3>

```typescript
public restorePolicy: pulumi.Output<{ ... } | undefined>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L53">property updateTime</a>
</h3>

```typescript
public updateTime: pulumi.Output<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L57">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="IAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L119">interface IAMBindingArgs</a>
</h2>

The set of arguments for constructing a IAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L123">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L132">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```


An array of identites that will be granted the privilege in the `role`.
Each entry can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L138">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_folder_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L90">interface IAMBindingState</a>
</h2>

Input properties used for looking up and filtering IAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L94">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the folder's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L98">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L107">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of identites that will be granted the privilege in the `role`.
Each entry can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMBinding.ts#L113">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_folder_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L118">interface IAMMemberArgs</a>
</h2>

The set of arguments for constructing a IAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L122">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L131">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```


The identity that will be granted the privilege in the `role`.
This field can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L136">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L90">interface IAMMemberState</a>
</h2>

Input properties used for looking up and filtering IAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L94">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the folder's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L98">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L107">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```


The identity that will be granted the privilege in the `role`.
This field can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMMember.ts#L112">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L92">interface IAMPolicyArgs</a>
</h2>

The set of arguments for constructing a IAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L96">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L102">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.

<h2 class="pdoc-module-header" id="IAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L72">interface IAMPolicyState</a>
</h2>

Input properties used for looking up and filtering IAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L76">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the folder's IAM policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L80">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/iAMPolicy.ts#L86">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.

<h2 class="pdoc-module-header" id="OrganizationPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L142">interface OrganizationPolicyArgs</a>
</h2>

The set of arguments for constructing a OrganizationPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L146">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L150">property constraint</a>
</h3>

```typescript
constraint: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L154">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The resource name of the folder to set the policy for. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L159">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L163">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L167">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="OrganizationPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L103">interface OrganizationPolicyState</a>
</h2>

Input properties used for looking up and filtering OrganizationPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L107">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L111">property constraint</a>
</h3>

```typescript
constraint?: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L115">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L119">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The resource name of the folder to set the policy for. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L124">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It
can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L128">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L132">property updateTime</a>
</h3>

```typescript
updateTime?: pulumi.Input<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/folder/organizationPolicy.ts#L136">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

