---
title: Module projects
---

<a href="../index.html">@pulumi/gcp</a> &gt; projects

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IAMBinding">class IAMBinding</a>
* <a href="#IAMCustomRole">class IAMCustomRole</a>
* <a href="#IAMMember">class IAMMember</a>
* <a href="#IAMPolicy">class IAMPolicy</a>
* <a href="#OrganizationPolicy">class OrganizationPolicy</a>
* <a href="#Service">class Service</a>
* <a href="#Services">class Services</a>
* <a href="#UsageExportBucket">class UsageExportBucket</a>
* <a href="#IAMBindingArgs">interface IAMBindingArgs</a>
* <a href="#IAMBindingState">interface IAMBindingState</a>
* <a href="#IAMCustomRoleArgs">interface IAMCustomRoleArgs</a>
* <a href="#IAMCustomRoleState">interface IAMCustomRoleState</a>
* <a href="#IAMMemberArgs">interface IAMMemberArgs</a>
* <a href="#IAMMemberState">interface IAMMemberState</a>
* <a href="#IAMPolicyArgs">interface IAMPolicyArgs</a>
* <a href="#IAMPolicyState">interface IAMPolicyState</a>
* <a href="#OrganizationPolicyArgs">interface OrganizationPolicyArgs</a>
* <a href="#OrganizationPolicyState">interface OrganizationPolicyState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>
* <a href="#ServicesArgs">interface ServicesArgs</a>
* <a href="#ServicesState">interface ServicesState</a>
* <a href="#UsageExportBucketArgs">interface UsageExportBucketArgs</a>
* <a href="#UsageExportBucketState">interface UsageExportBucketState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts">projects/iAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts">projects/iAMCustomRole.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts">projects/iAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts">projects/iAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts">projects/organizationPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts">projects/service.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts">projects/services.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts">projects/usageExportBucket.ts</a> 


<h2 class="pdoc-module-header" id="IAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L17">class IAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:

* `google_project_iam_policy`: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.
* `google_project_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.
* `google_project_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.

~> **Note:** `google_project_iam_policy` **cannot** be used in conjunction with `google_project_iam_binding` and `google_project_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_project_iam_binding` resources **can be** used in conjunction with `google_project_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L45">constructor</a>
</h3>

```typescript
new IAMBinding(name: string, args: IAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L26">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L33">property etag</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L34">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L39">property project</a>
</h3>

```typescript
public project: pulumi.Output<string | undefined>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L45">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMCustomRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L12">class IAMCustomRole</a>
</h2>

Allows management of a customized Cloud IAM project role. For more information see
[the official documentation](https://cloud.google.com/iam/docs/understanding-custom-roles)
and
[API](https://cloud.google.com/iam/reference/rest/v1/projects.roles).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L55">constructor</a>
</h3>

```typescript
new IAMCustomRole(name: string, args: IAMCustomRoleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMCustomRole resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMCustomRoleState): IAMCustomRole
```


Get an existing IAMCustomRole resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L28">property deleted</a>
</h3>

```typescript
public deleted: pulumi.Output<boolean | undefined>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A human-readable description for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L36">property permissions</a>
</h3>

```typescript
public permissions: pulumi.Output<string[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L41">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L45">property roleId</a>
</h3>

```typescript
public roleId: pulumi.Output<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L51">property stage</a>
</h3>

```typescript
public stage: pulumi.Output<string | undefined>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L55">property title</a>
</h3>

```typescript
public title: pulumi.Output<string>;
```


A human-readable title for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L17">class IAMMember</a>
</h2>

Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:

* `google_project_iam_policy`: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.
* `google_project_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.
* `google_project_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.

~> **Note:** `google_project_iam_policy` **cannot** be used in conjunction with `google_project_iam_binding` and `google_project_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_project_iam_binding` resources **can be** used in conjunction with `google_project_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L45">constructor</a>
</h3>

```typescript
new IAMMember(name: string, args: IAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L26">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L33">property etag</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L34">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L39">property project</a>
</h3>

```typescript
public project: pulumi.Output<string | undefined>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L45">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L17">class IAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:

* `google_project_iam_policy`: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.
* `google_project_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.
* `google_project_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.

~> **Note:** `google_project_iam_policy` **cannot** be used in conjunction with `google_project_iam_binding` and `google_project_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_project_iam_binding` resources **can be** used in conjunction with `google_project_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L70">constructor</a>
</h3>

```typescript
new IAMPolicy(name: string, args: IAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L26">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L43">property authoritative</a>
</h3>

```typescript
public authoritative: pulumi.Output<boolean | undefined>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value indicating if this policy
should overwrite any existing IAM policy on the project. When set to true,
**any policies not in your config file will be removed**. This can **lock
you out** of your project until an Organization Administrator grants you
access again, so please exercise caution. If this argument is `true` and you
want to delete the resource, you must set the `disable_project` argument to
`true`, acknowledging that the project will be inaccessible to anyone but the
Organization Admins, as it will no longer have an IAM policy. Rather than using
this, you should use `google_project_iam_binding` and
`google_project_iam_member`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L49">property disableProject</a>
</h3>

```typescript
public disableProject: pulumi.Output<boolean | undefined>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value that must be set to `true`
if you want to delete a `google_project_iam_policy` that is authoritative.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L53">property etag</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L59">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L64">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L70">property restorePolicy</a>
</h3>

```typescript
public restorePolicy: pulumi.Output<string>;
```


(DEPRECATED) (Computed, only for `google_project_iam_policy`)
The IAM policy that will be restored when a
non-authoritative policy resource is deleted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="OrganizationPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L12">class OrganizationPolicy</a>
</h2>

Allows management of Organization policies for a Google Project. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L56">constructor</a>
</h3>

```typescript
new OrganizationPolicy(name: string, args: OrganizationPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OrganizationPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L28">property booleanPolicy</a>
</h3>

```typescript
public booleanPolicy: pulumi.Output<{ ... } | undefined>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L32">property constraint</a>
</h3>

```typescript
public constraint: pulumi.Output<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L40">property listPolicy</a>
</h3>

```typescript
public listPolicy: pulumi.Output<{ ... } | undefined>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L44">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project id of the project to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L48">property restorePolicy</a>
</h3>

```typescript
public restorePolicy: pulumi.Output<{ ... } | undefined>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L52">property updateTime</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L56">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L15">class Service</a>
</h2>

Allows management of a single API service for an existing Google Cloud Platform project.

For a list of services available, visit the
[API library page](https://console.cloud.google.com/apis/library) or run `gcloud services list`.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_project_services` or they will fight over which services should be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L39">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L31">property disableOnDestroy</a>
</h3>

```typescript
public disableOnDestroy: pulumi.Output<boolean | undefined>;
```


If true, disable the service when the terraform resource is destroyed.  Defaults to true.  May be useful in the event that a project is long-lived but the infrastructure running in that project changes frequently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L35">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project ID. If not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L39">property service</a>
</h3>

```typescript
public service: pulumi.Output<string>;
```


The service to enable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Services">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L18">class Services</a>
</h2>

Allows management of enabled API services for an existing Google Cloud
Platform project. Services in an existing project that are not defined
in the config will be removed.

For a list of services available, visit the
[API library page](https://console.cloud.google.com/apis/library) or run `gcloud services list`.

~> **Note:** This resource attempts to be the authoritative source on which APIs are enabled, which can
	lead to conflicts when certain APIs or actions enable other APIs. To just ensure that a specific
	API is enabled, use the [google_project_service](google_project_service.html) resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L42">constructor</a>
</h3>

```typescript
new Services(name: string, args: ServicesArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Services resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServicesState): Services
```


Get an existing Services resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L31">property disableOnDestroy</a>
</h3>

```typescript
public disableOnDestroy: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L37">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project ID.
Changing this forces Terraform to attempt to disable all previously managed
API services in the previous project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L42">property services</a>
</h3>

```typescript
public services: pulumi.Output<string[]>;
```


The list of services that are enabled. Supports
update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="UsageExportBucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L35">class UsageExportBucket</a>
</h2>

Allows creation and management of a Google Cloud Platform project.

Projects created with this resource must be associated with an Organization.
See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `google_project`
resource must have `roles/resourcemanager.projectCreator`. See the
[Access Control for Organizations Using IAM](https://cloud.google.com/resource-manager/docs/access-control-org)
doc for more information.

Note that prior to 0.8.5, `google_project` functioned like a data source,
meaning any project referenced by it had to be created and managed outside
Terraform. As of 0.8.5, `google_project` functions like any other Terraform
resource, with Terraform creating and managing the project. To replicate the old
behavior, either:

* Use the project ID directly in whatever is referencing the project, using the
  [google_project_iam_policy](/docs/providers/google/r/google_project_iam.html)
  to replace the old `policy_data` property.
* Use the [import](/docs/import/usage.html) functionality
  to import your pre-existing project into Terraform, where it can be referenced and
  used just like always, keeping in mind that Terraform will attempt to undo any changes
  made outside Terraform.

~> It's important to note that any project resources that were added to your Terraform config
prior to 0.8.5 will continue to function as they always have, and will not be managed by
Terraform. Only newly added projects are affected.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L50">constructor</a>
</h3>

```typescript
new UsageExportBucket(name: string, args: UsageExportBucketArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UsageExportBucket resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L44">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UsageExportBucketState): UsageExportBucket
```


Get an existing UsageExportBucket resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L48">property bucketName</a>
</h3>

```typescript
public bucketName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L49">property prefix</a>
</h3>

```typescript
public prefix: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L105">interface IAMBindingArgs</a>
</h2>

The set of arguments for constructing a IAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L106">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L111">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L117">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L83">interface IAMBindingState</a>
</h2>

Input properties used for looking up and filtering IAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L87">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the project's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L88">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L93">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMBinding.ts#L99">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMCustomRoleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L139">interface IAMCustomRoleArgs</a>
</h2>

The set of arguments for constructing a IAMCustomRole resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L143">property deleted</a>
</h3>

```typescript
deleted?: pulumi.Input<boolean>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L147">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L151">property permissions</a>
</h3>

```typescript
permissions: pulumi.Input<pulumi.Input<string>[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L156">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L160">property roleId</a>
</h3>

```typescript
roleId: pulumi.Input<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L166">property stage</a>
</h3>

```typescript
stage?: pulumi.Input<string>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L170">property title</a>
</h3>

```typescript
title: pulumi.Input<string>;
```


A human-readable title for the role.

<h2 class="pdoc-module-header" id="IAMCustomRoleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L102">interface IAMCustomRoleState</a>
</h2>

Input properties used for looking up and filtering IAMCustomRole resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L106">property deleted</a>
</h3>

```typescript
deleted?: pulumi.Input<boolean>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L110">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L114">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<pulumi.Input<string>[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L119">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project that the service account will be created in.
Defaults to the provider project configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L123">property roleId</a>
</h3>

```typescript
roleId?: pulumi.Input<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L129">property stage</a>
</h3>

```typescript
stage?: pulumi.Input<string>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMCustomRole.ts#L133">property title</a>
</h3>

```typescript
title?: pulumi.Input<string>;
```


A human-readable title for the role.

<h2 class="pdoc-module-header" id="IAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L105">interface IAMMemberArgs</a>
</h2>

The set of arguments for constructing a IAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L106">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L111">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L117">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L83">interface IAMMemberState</a>
</h2>

Input properties used for looking up and filtering IAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L87">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the project's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L88">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L93">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMMember.ts#L99">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_project_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L156">interface IAMPolicyArgs</a>
</h2>

The set of arguments for constructing a IAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L170">property authoritative</a>
</h3>

```typescript
authoritative?: pulumi.Input<boolean>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value indicating if this policy
should overwrite any existing IAM policy on the project. When set to true,
**any policies not in your config file will be removed**. This can **lock
you out** of your project until an Organization Administrator grants you
access again, so please exercise caution. If this argument is `true` and you
want to delete the resource, you must set the `disable_project` argument to
`true`, acknowledging that the project will be inaccessible to anyone but the
Organization Admins, as it will no longer have an IAM policy. Rather than using
this, you should use `google_project_iam_binding` and
`google_project_iam_member`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L176">property disableProject</a>
</h3>

```typescript
disableProject?: pulumi.Input<boolean>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value that must be set to `true`
if you want to delete a `google_project_iam_policy` that is authoritative.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L182">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L187">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h2 class="pdoc-module-header" id="IAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L109">interface IAMPolicyState</a>
</h2>

Input properties used for looking up and filtering IAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L123">property authoritative</a>
</h3>

```typescript
authoritative?: pulumi.Input<boolean>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value indicating if this policy
should overwrite any existing IAM policy on the project. When set to true,
**any policies not in your config file will be removed**. This can **lock
you out** of your project until an Organization Administrator grants you
access again, so please exercise caution. If this argument is `true` and you
want to delete the resource, you must set the `disable_project` argument to
`true`, acknowledging that the project will be inaccessible to anyone but the
Organization Admins, as it will no longer have an IAM policy. Rather than using
this, you should use `google_project_iam_binding` and
`google_project_iam_member`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L129">property disableProject</a>
</h3>

```typescript
disableProject?: pulumi.Input<boolean>;
```


(Optional, only for `google_project_iam_policy`)
A boolean value that must be set to `true`
if you want to delete a `google_project_iam_policy` that is authoritative.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L133">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the project's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L139">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L144">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not specified, uses the
ID of the project configured with the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/iAMPolicy.ts#L150">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<string>;
```


(DEPRECATED) (Computed, only for `google_project_iam_policy`)
The IAM policy that will be restored when a
non-authoritative policy resource is deleted.

<h2 class="pdoc-module-header" id="OrganizationPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L140">interface OrganizationPolicyArgs</a>
</h2>

The set of arguments for constructing a OrganizationPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L144">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L148">property constraint</a>
</h3>

```typescript
constraint: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L152">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L156">property project</a>
</h3>

```typescript
project: pulumi.Input<string>;
```


The project id of the project to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L160">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L164">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="OrganizationPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L102">interface OrganizationPolicyState</a>
</h2>

Input properties used for looking up and filtering OrganizationPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L106">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L110">property constraint</a>
</h3>

```typescript
constraint?: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L114">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L118">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L122">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project id of the project to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L126">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L130">property updateTime</a>
</h3>

```typescript
updateTime?: pulumi.Input<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/organizationPolicy.ts#L134">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L90">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L94">property disableOnDestroy</a>
</h3>

```typescript
disableOnDestroy?: pulumi.Input<boolean>;
```


If true, disable the service when the terraform resource is destroyed.  Defaults to true.  May be useful in the event that a project is long-lived but the infrastructure running in that project changes frequently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L98">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L102">property service</a>
</h3>

```typescript
service: pulumi.Input<string>;
```


The service to enable.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L72">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L76">property disableOnDestroy</a>
</h3>

```typescript
disableOnDestroy?: pulumi.Input<boolean>;
```


If true, disable the service when the terraform resource is destroyed.  Defaults to true.  May be useful in the event that a project is long-lived but the infrastructure running in that project changes frequently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L80">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/service.ts#L84">property service</a>
</h3>

```typescript
service?: pulumi.Input<string>;
```


The service to enable.

<h2 class="pdoc-module-header" id="ServicesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L93">interface ServicesArgs</a>
</h2>

The set of arguments for constructing a Services resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L94">property disableOnDestroy</a>
</h3>

```typescript
disableOnDestroy?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L100">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID.
Changing this forces Terraform to attempt to disable all previously managed
API services in the previous project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L105">property services</a>
</h3>

```typescript
services: pulumi.Input<pulumi.Input<string>[]>;
```


The list of services that are enabled. Supports
update.

<h2 class="pdoc-module-header" id="ServicesState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L75">interface ServicesState</a>
</h2>

Input properties used for looking up and filtering Services resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L76">property disableOnDestroy</a>
</h3>

```typescript
disableOnDestroy?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L82">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID.
Changing this forces Terraform to attempt to disable all previously managed
API services in the previous project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/services.ts#L87">property services</a>
</h3>

```typescript
services?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of services that are enabled. Supports
update.

<h2 class="pdoc-module-header" id="UsageExportBucketArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L92">interface UsageExportBucketArgs</a>
</h2>

The set of arguments for constructing a UsageExportBucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L93">property bucketName</a>
</h3>

```typescript
bucketName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L94">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L95">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="UsageExportBucketState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L83">interface UsageExportBucketState</a>
</h2>

Input properties used for looking up and filtering UsageExportBucket resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L84">property bucketName</a>
</h3>

```typescript
bucketName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L85">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/projects/usageExportBucket.ts#L86">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

