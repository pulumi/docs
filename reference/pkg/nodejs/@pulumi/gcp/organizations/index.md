---
title: Module organizations
---

<a href="../index.html">@pulumi/gcp</a> &gt; organizations

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Folder">class Folder</a>
* <a href="#IAMBinding">class IAMBinding</a>
* <a href="#IAMCustomRole">class IAMCustomRole</a>
* <a href="#IAMMember">class IAMMember</a>
* <a href="#IAMPolicy">class IAMPolicy</a>
* <a href="#Policy">class Policy</a>
* <a href="#Project">class Project</a>
* <a href="#getActiveFolder">function getActiveFolder</a>
* <a href="#getBillingAccount">function getBillingAccount</a>
* <a href="#getClientConfig">function getClientConfig</a>
* <a href="#getFolder">function getFolder</a>
* <a href="#getIAMPolicy">function getIAMPolicy</a>
* <a href="#getOrganization">function getOrganization</a>
* <a href="#getProject">function getProject</a>
* <a href="#FolderArgs">interface FolderArgs</a>
* <a href="#FolderState">interface FolderState</a>
* <a href="#GetActiveFolderArgs">interface GetActiveFolderArgs</a>
* <a href="#GetActiveFolderResult">interface GetActiveFolderResult</a>
* <a href="#GetBillingAccountArgs">interface GetBillingAccountArgs</a>
* <a href="#GetBillingAccountResult">interface GetBillingAccountResult</a>
* <a href="#GetClientConfigResult">interface GetClientConfigResult</a>
* <a href="#GetFolderArgs">interface GetFolderArgs</a>
* <a href="#GetFolderResult">interface GetFolderResult</a>
* <a href="#GetIAMPolicyArgs">interface GetIAMPolicyArgs</a>
* <a href="#GetIAMPolicyResult">interface GetIAMPolicyResult</a>
* <a href="#GetOrganizationArgs">interface GetOrganizationArgs</a>
* <a href="#GetOrganizationResult">interface GetOrganizationResult</a>
* <a href="#GetProjectArgs">interface GetProjectArgs</a>
* <a href="#GetProjectResult">interface GetProjectResult</a>
* <a href="#IAMBindingArgs">interface IAMBindingArgs</a>
* <a href="#IAMBindingState">interface IAMBindingState</a>
* <a href="#IAMCustomRoleArgs">interface IAMCustomRoleArgs</a>
* <a href="#IAMCustomRoleState">interface IAMCustomRoleState</a>
* <a href="#IAMMemberArgs">interface IAMMemberArgs</a>
* <a href="#IAMMemberState">interface IAMMemberState</a>
* <a href="#IAMPolicyArgs">interface IAMPolicyArgs</a>
* <a href="#IAMPolicyState">interface IAMPolicyState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#ProjectArgs">interface ProjectArgs</a>
* <a href="#ProjectState">interface ProjectState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts">organizations/folder.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts">organizations/getActiveFolder.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts">organizations/getBillingAccount.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts">organizations/getClientConfig.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts">organizations/getFolder.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts">organizations/getIAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts">organizations/getOrganization.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts">organizations/getProject.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts">organizations/iAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts">organizations/iAMCustomRole.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts">organizations/iAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts">organizations/iAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts">organizations/policy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts">organizations/project.ts</a> 


<h2 class="pdoc-module-header" id="Folder">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L21">class Folder</a>
</h2>

Allows management of a Google Cloud Platform folder. For more information see
[the official documentation](https://cloud.google.com/resource-manager/docs/creating-managing-folders)
and
[API](https://cloud.google.com/resource-manager/reference/rest/v2/folders).

A folder can contain projects, other folders, or a combination of both. You can use folders to group projects under an organization in a hierarchy. For example, your organization might contain multiple departments, each with its own set of Cloud Platform resources. Folders allows you to group these resources on a per-department basis. Folders are used to group resources that share common IAM policies.

Folders created live inside an Organization. See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `google_folder`
resource must have `roles/resourcemanager.folderCreator`. See the
[Access Control for Folders Using IAM](https://cloud.google.com/resource-manager/docs/access-control-folders)
doc for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L56">constructor</a>
</h3>

```typescript
new Folder(name: string, args: FolderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Folder resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L30">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderState): Folder
```


Get an existing Folder resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L38">property createTime</a>
</h3>

```typescript
public createTime: pulumi.Output<string>;
```


Timestamp when the Folder was created. Assigned by the server.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L43">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L47">property lifecycleState</a>
</h3>

```typescript
public lifecycleState: pulumi.Output<string>;
```


The lifecycle state of the folder such as `ACTIVE` or `DELETE_REQUESTED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The resource name of the Folder. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L56">property parent</a>
</h3>

```typescript
public parent: pulumi.Output<string>;
```


The resource name of the parent Folder or Organization.
Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L14">class IAMBinding</a>
</h2>

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Organization.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_member` for the __same role__ or they will fight over
   what your policy should be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L44">constructor</a>
</h3>

```typescript
new IAMBinding(name: string, args: IAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L30">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the organization's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L34">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L38">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L44">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_organization_iam_binding` can be used per role. Note that custom roles must be of the format
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L12">class IAMCustomRole</a>
</h2>

Allows management of a customized Cloud IAM organization role. For more information see
[the official documentation](https://cloud.google.com/iam/docs/understanding-custom-roles)
and
[API](https://cloud.google.com/iam/reference/rest/v1/organizations.roles).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L54">constructor</a>
</h3>

```typescript
new IAMCustomRole(name: string, args: IAMCustomRoleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMCustomRole resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L28">property deleted</a>
</h3>

```typescript
public deleted: pulumi.Output<boolean | undefined>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L32">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L36">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L40">property permissions</a>
</h3>

```typescript
public permissions: pulumi.Output<string[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L44">property roleId</a>
</h3>

```typescript
public roleId: pulumi.Output<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L50">property stage</a>
</h3>

```typescript
public stage: pulumi.Output<string | undefined>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L54">property title</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L14">class IAMMember</a>
</h2>

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Organization.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_binding` for the __same role__ or they will fight over
   what your policy should be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L43">constructor</a>
</h3>

```typescript
new IAMMember(name: string, args: IAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L30">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the organization's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L34">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L38">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L43">property role</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L22">class IAMPolicy</a>
</h2>

Allows management of the entire IAM policy for an existing Google Cloud Platform Organization.

~> **Warning:** New organizations have several default policies which will,
   without extreme caution, be **overwritten** by use of this resource.
   The safest alternative is to use multiple `google_organization_iam_binding`
   resources.  It is easy to use this resource to remove your own access to
   an organization, which will require a call to Google Support to have
   fixed, and can take multiple days to resolve.  If you do use this resource,
   the best way to be sure that you are not making dangerous changes is to start
   by importing your existing policy, and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_member` or `google_organization_iam_binding`
   or they will fight over what your policy should be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L45">constructor</a>
</h3>

```typescript
new IAMPolicy(name: string, args: IAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L31">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L35">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L39">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L45">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L12">class Policy</a>
</h2>

Allows management of Organization policies for a Google Organization. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L56">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L28">property booleanPolicy</a>
</h3>

```typescript
public booleanPolicy: pulumi.Output<{ ... } | undefined>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L32">property constraint</a>
</h3>

```typescript
public constraint: pulumi.Output<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L36">property etag</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L40">property listPolicy</a>
</h3>

```typescript
public listPolicy: pulumi.Output<{ ... } | undefined>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L44">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L48">property restorePolicy</a>
</h3>

```typescript
public restorePolicy: pulumi.Output<{ ... } | undefined>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L52">property updateTime</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L56">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="Project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L35">class Project</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L106">constructor</a>
</h3>

```typescript
new Project(name: string, args: ProjectArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Project resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L44">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState): Project
```


Get an existing Project resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L52">property appEngine</a>
</h3>

```typescript
public appEngine: pulumi.Output<{ ... } | undefined>;
```


A block of configuration to enable an App Engine app. Setting this
field will enabled the App Engine Admin API, which is required to manage the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L60">property autoCreateNetwork</a>
</h3>

```typescript
public autoCreateNetwork: pulumi.Output<boolean | undefined>;
```


Create the 'default' network automatically.  Default true.
Note: this might be more accurately described as "Delete Default Network", since the network
is created automatically then deleted before project creation returns, but we choose this
name to match the GCP Console UI. Setting this field to false will enable the Compute Engine
API which is required to delete the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L68">property billingAccount</a>
</h3>

```typescript
public billingAccount: pulumi.Output<string | undefined>;
```


The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (`roles/billing.admin`) in
the organization. See [Google Cloud Billing API Access Control](https://cloud.google.com/billing/v1/how-tos/access-control)
for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L76">property folderId</a>
</h3>

```typescript
public folderId: pulumi.Output<string>;
```


The numeric ID of the folder this project should be
created under. Only one of `org_id` or `folder_id` may be
specified. If the `folder_id` is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L80">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L84">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L88">property number</a>
</h3>

```typescript
public number: pulumi.Output<string>;
```


The numeric identifier of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L97">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
`org_id` or `folder_id` may be specified. If the `org_id` is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L101">property projectId</a>
</h3>

```typescript
public projectId: pulumi.Output<string>;
```


The project ID. Changing this forces a new project to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L106">property skipDelete</a>
</h3>

```typescript
public skipDelete: pulumi.Output<boolean>;
```


If true, the Terraform resource can be deleted
without deleting the Project via the Google API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getActiveFolder">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L9">function getActiveFolder</a>
</h2>

```typescript
getActiveFolder(args: GetActiveFolderArgs, opts?: pulumi.InvokeOptions): Promise<GetActiveFolderResult>
```


Get an active folder within GCP by `display_name` and `parent`.

<h2 class="pdoc-module-header" id="getBillingAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L24">function getBillingAccount</a>
</h2>

```typescript
getBillingAccount(args?: GetBillingAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetBillingAccountResult>
```


Use this data source to get information about a Google Billing Account.

```hcl
data "google_billing_account" "acct" {
  display_name = "My Billing Account"
  open         = true
}

resource "google_project" "my_project" {
  name       = "My Project"
  project_id = "your-project-id"
  org_id     = "1234567"

  billing_account = "${data.google_billing_account.acct.id}"
}
```

<h2 class="pdoc-module-header" id="getClientConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L9">function getClientConfig</a>
</h2>

```typescript
getClientConfig(opts?: pulumi.InvokeOptions): Promise<GetClientConfigResult>
```


Use this data source to access the configuration of the Google Cloud provider.

<h2 class="pdoc-module-header" id="getFolder">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L11">function getFolder</a>
</h2>

```typescript
getFolder(args: GetFolderArgs, opts?: pulumi.InvokeOptions): Promise<GetFolderResult>
```


Use this data source to get information about a Google Cloud Folder.

```hcl

<h2 class="pdoc-module-header" id="getIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L38">function getIAMPolicy</a>
</h2>

```typescript
getIAMPolicy(args: GetIAMPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetIAMPolicyResult>
```


Generates an IAM policy document that may be referenced by and applied to
other Google Cloud Platform resources, such as the `google_project` resource.

```
data "google_iam_policy" "admin" {
  binding {
    role = "roles/compute.instanceAdmin"

    members = [
      "serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com",
    ]
  }

  binding {
    role = "roles/storage.objectViewer"

    members = [
      "user:jane@example.com",
    ]
  }
}
```

This data source is used to define IAM policies to apply to other resources.
Currently, defining a policy through a datasource and referencing that policy
from another resource is the only way to apply an IAM policy to a resource.

**Note:** Several restrictions apply when setting IAM policies through this API.
See the [setIamPolicy docs](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)
for a list of these restrictions.

<h2 class="pdoc-module-header" id="getOrganization">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L20">function getOrganization</a>
</h2>

```typescript
getOrganization(args?: GetOrganizationArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationResult>
```


Use this data source to get information about a Google Cloud Organization.

```hcl
data "google_organization" "org" {
  domain = "example.com"
}

resource "google_folder" "sales" {
  display_name = "Sales"
  parent       = "${data.google_organization.org.name}"
}
```

<h2 class="pdoc-module-header" id="getProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L11">function getProject</a>
</h2>

```typescript
getProject(args?: GetProjectArgs, opts?: pulumi.InvokeOptions): Promise<GetProjectResult>
```


Use this data source to get project details.
For more information see
[API](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project)

<h2 class="pdoc-module-header" id="FolderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L125">interface FolderArgs</a>
</h2>

The set of arguments for constructing a Folder resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L130">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```


The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L135">property parent</a>
</h3>

```typescript
parent: pulumi.Input<string>;
```


The resource name of the parent Folder or Organization.
Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.

<h2 class="pdoc-module-header" id="FolderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L96">interface FolderState</a>
</h2>

Input properties used for looking up and filtering Folder resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L101">property createTime</a>
</h3>

```typescript
createTime?: pulumi.Input<string>;
```


Timestamp when the Folder was created. Assigned by the server.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L106">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L110">property lifecycleState</a>
</h3>

```typescript
lifecycleState?: pulumi.Input<string>;
```


The lifecycle state of the folder such as `ACTIVE` or `DELETE_REQUESTED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The resource name of the Folder. Its format is folders/{folder_id}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/folder.ts#L119">property parent</a>
</h3>

```typescript
parent?: pulumi.Input<string>;
```


The resource name of the parent Folder or Organization.
Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.

<h2 class="pdoc-module-header" id="GetActiveFolderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L19">interface GetActiveFolderArgs</a>
</h2>

A collection of arguments for invoking getActiveFolder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L23">property displayName</a>
</h3>

```typescript
displayName: string;
```


The folder's display name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L27">property parent</a>
</h3>

```typescript
parent: string;
```


The resource name of the parent Folder or Organization.

<h2 class="pdoc-module-header" id="GetActiveFolderResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L33">interface GetActiveFolderResult</a>
</h2>

A collection of values returned by getActiveFolder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getActiveFolder.ts#L37">property name</a>
</h3>

```typescript
name: string;
```


The resource name of the Folder. This uniquely identifies the folder.

<h2 class="pdoc-module-header" id="GetBillingAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L36">interface GetBillingAccountArgs</a>
</h2>

A collection of arguments for invoking getBillingAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L40">property billingAccount</a>
</h3>

```typescript
billingAccount?: string;
```


The name of the billing account in the form `{billing_account_id}` or `billingAccounts/{billing_account_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L44">property displayName</a>
</h3>

```typescript
displayName?: string;
```


The display name of the billing account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L48">property open</a>
</h3>

```typescript
open?: boolean;
```


`true` if the billing account is open, `false` if the billing account is closed.

<h2 class="pdoc-module-header" id="GetBillingAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L54">interface GetBillingAccountResult</a>
</h2>

A collection of values returned by getBillingAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L55">property displayName</a>
</h3>

```typescript
displayName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L68">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L59">property name</a>
</h3>

```typescript
name: string;
```


The resource name of the billing account in the form `billingAccounts/{billing_account_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L60">property open</a>
</h3>

```typescript
open: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getBillingAccount.ts#L64">property projectIds</a>
</h3>

```typescript
projectIds: string[];
```


The IDs of any projects associated with the billing account.

<h2 class="pdoc-module-header" id="GetClientConfigResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L17">interface GetClientConfigResult</a>
</h2>

A collection of values returned by getClientConfig.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L21">property accessToken</a>
</h3>

```typescript
accessToken: string;
```


The OAuth2 access token used by the client to authenticate against the Google Cloud API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L33">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L25">property project</a>
</h3>

```typescript
project: string;
```


The ID of the project to apply any resources to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getClientConfig.ts#L29">property region</a>
</h3>

```typescript
region: string;
```


The region to operate under.

<h2 class="pdoc-module-header" id="GetFolderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L21">interface GetFolderArgs</a>
</h2>

A collection of arguments for invoking getFolder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L25">property folder</a>
</h3>

```typescript
folder: string;
```


The name of the Folder in the form `{folder_id}` or `folders/{folder_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L29">property lookupOrganization</a>
</h3>

```typescript
lookupOrganization?: boolean;
```


`true` to find the organization that the folder belongs, `false` to avoid the lookup. It searches up the tree. (defaults to `false`)

<h2 class="pdoc-module-header" id="GetFolderResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L35">interface GetFolderResult</a>
</h2>

A collection of values returned by getFolder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L39">property createTime</a>
</h3>

```typescript
createTime: string;
```


Timestamp when the Organization was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L43">property displayName</a>
</h3>

```typescript
displayName: string;
```


The folder's display name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L63">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L47">property lifecycleState</a>
</h3>

```typescript
lifecycleState: string;
```


The Folder's current lifecycle state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L51">property name</a>
</h3>

```typescript
name: string;
```


The resource name of the Folder in the form `folders/{organization_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L55">property organization</a>
</h3>

```typescript
organization: string;
```


If `lookup_organization` is enable, the resource name of the Organization that the folder belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getFolder.ts#L59">property parent</a>
</h3>

```typescript
parent: string;
```


The resource name of the parent Folder or Organization.

<h2 class="pdoc-module-header" id="GetIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L47">interface GetIAMPolicyArgs</a>
</h2>

A collection of arguments for invoking getIAMPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L53">property bindings</a>
</h3>

```typescript
bindings: { ... }[];
```


A nested configuration block (described below)
defining a binding to be included in the policy document. Multiple
`binding` arguments are supported.

<h2 class="pdoc-module-header" id="GetIAMPolicyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L59">interface GetIAMPolicyResult</a>
</h2>

A collection of values returned by getIAMPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L68">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getIAMPolicy.ts#L64">property policyData</a>
</h3>

```typescript
policyData: string;
```


The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.

<h2 class="pdoc-module-header" id="GetOrganizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L31">interface GetOrganizationArgs</a>
</h2>

A collection of arguments for invoking getOrganization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L35">property domain</a>
</h3>

```typescript
domain?: string;
```


The domain name of the Organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L39">property organization</a>
</h3>

```typescript
organization?: string;
```


The name of the Organization in the form `{organization_id}` or `organizations/{organization_id}`.

<h2 class="pdoc-module-header" id="GetOrganizationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L45">interface GetOrganizationResult</a>
</h2>

A collection of values returned by getOrganization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L49">property createTime</a>
</h3>

```typescript
createTime: string;
```


Timestamp when the Organization was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L53">property directoryCustomerId</a>
</h3>

```typescript
directoryCustomerId: string;
```


The Google for Work customer ID of the Organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L54">property domain</a>
</h3>

```typescript
domain: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L66">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L58">property lifecycleState</a>
</h3>

```typescript
lifecycleState: string;
```


The Organization's current lifecycle state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getOrganization.ts#L62">property name</a>
</h3>

```typescript
name: string;
```


The resource name of the Organization in the form `organizations/{organization_id}`.

<h2 class="pdoc-module-header" id="GetProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L21">interface GetProjectArgs</a>
</h2>

A collection of arguments for invoking getProject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L25">property projectId</a>
</h3>

```typescript
projectId?: string;
```


The project ID. If it is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GetProjectResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L31">interface GetProjectResult</a>
</h2>

A collection of values returned by getProject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L32">property appEngines</a>
</h3>

```typescript
appEngines: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L33">property autoCreateNetwork</a>
</h3>

```typescript
autoCreateNetwork: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L34">property billingAccount</a>
</h3>

```typescript
billingAccount: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L35">property folderId</a>
</h3>

```typescript
folderId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L36">property labels</a>
</h3>

```typescript
labels: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L37">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L38">property number</a>
</h3>

```typescript
number: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L39">property orgId</a>
</h3>

```typescript
orgId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L40">property policyData</a>
</h3>

```typescript
policyData: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L41">property policyEtag</a>
</h3>

```typescript
policyEtag: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/getProject.ts#L42">property skipDelete</a>
</h3>

```typescript
skipDelete: boolean;
```

<h2 class="pdoc-module-header" id="IAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L109">interface IAMBindingArgs</a>
</h2>

The set of arguments for constructing a IAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L113">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L117">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L123">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_organization_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L85">interface IAMBindingState</a>
</h2>

Input properties used for looking up and filtering IAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L89">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the organization's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L93">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L97">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMBinding.ts#L103">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_organization_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMCustomRoleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L140">interface IAMCustomRoleArgs</a>
</h2>

The set of arguments for constructing a IAMCustomRole resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L144">property deleted</a>
</h3>

```typescript
deleted?: pulumi.Input<boolean>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L148">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L152">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L156">property permissions</a>
</h3>

```typescript
permissions: pulumi.Input<pulumi.Input<string>[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L160">property roleId</a>
</h3>

```typescript
roleId: pulumi.Input<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L166">property stage</a>
</h3>

```typescript
stage?: pulumi.Input<string>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L170">property title</a>
</h3>

```typescript
title: pulumi.Input<string>;
```


A human-readable title for the role.

<h2 class="pdoc-module-header" id="IAMCustomRoleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L104">interface IAMCustomRoleState</a>
</h2>

Input properties used for looking up and filtering IAMCustomRole resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L108">property deleted</a>
</h3>

```typescript
deleted?: pulumi.Input<boolean>;
```


The current deleted state of the role. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L112">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description for the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L116">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L120">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<pulumi.Input<string>[]>;
```


The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L124">property roleId</a>
</h3>

```typescript
roleId?: pulumi.Input<string>;
```


The role id to use for this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L130">property stage</a>
</h3>

```typescript
stage?: pulumi.Input<string>;
```


The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMCustomRole.ts#L134">property title</a>
</h3>

```typescript
title?: pulumi.Input<string>;
```


A human-readable title for the role.

<h2 class="pdoc-module-header" id="IAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L107">interface IAMMemberArgs</a>
</h2>

The set of arguments for constructing a IAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L111">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L115">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L120">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L84">interface IAMMemberState</a>
</h2>

Input properties used for looking up and filtering IAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L88">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the organization's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L92">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L96">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMMember.ts#L101">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="IAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L98">interface IAMPolicyArgs</a>
</h2>

The set of arguments for constructing a IAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L102">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L108">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.

<h2 class="pdoc-module-header" id="IAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L81">interface IAMPolicyState</a>
</h2>

Input properties used for looking up and filtering IAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L82">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L86">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization in which you want to create a custom role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/iAMPolicy.ts#L92">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The `google_iam_policy` data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L140">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L144">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L148">property constraint</a>
</h3>

```typescript
constraint: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L152">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L156">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L160">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L164">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L102">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L106">property booleanPolicy</a>
</h3>

```typescript
booleanPolicy?: pulumi.Input<{ ... }>;
```


A boolean policy is a constraint that is either enforced or not. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L110">property constraint</a>
</h3>

```typescript
constraint?: pulumi.Input<string>;
```


The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L114">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L118">property listPolicy</a>
</h3>

```typescript
listPolicy?: pulumi.Input<{ ... }>;
```


A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L122">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization to set the policy for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L126">property restorePolicy</a>
</h3>

```typescript
restorePolicy?: pulumi.Input<{ ... }>;
```


A restore policy is a constraint to restore the default policy. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L130">property updateTime</a>
</h3>

```typescript
updateTime?: pulumi.Input<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/policy.ts#L134">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


Version of the Policy. Default version is 0.

<h2 class="pdoc-module-header" id="ProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L218">interface ProjectArgs</a>
</h2>

The set of arguments for constructing a Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L223">property appEngine</a>
</h3>

```typescript
appEngine?: pulumi.Input<{ ... }>;
```


A block of configuration to enable an App Engine app. Setting this
field will enabled the App Engine Admin API, which is required to manage the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L231">property autoCreateNetwork</a>
</h3>

```typescript
autoCreateNetwork?: pulumi.Input<boolean>;
```


Create the 'default' network automatically.  Default true.
Note: this might be more accurately described as "Delete Default Network", since the network
is created automatically then deleted before project creation returns, but we choose this
name to match the GCP Console UI. Setting this field to false will enable the Compute Engine
API which is required to delete the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L239">property billingAccount</a>
</h3>

```typescript
billingAccount?: pulumi.Input<string>;
```


The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (`roles/billing.admin`) in
the organization. See [Google Cloud Billing API Access Control](https://cloud.google.com/billing/v1/how-tos/access-control)
for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L247">property folderId</a>
</h3>

```typescript
folderId?: pulumi.Input<string>;
```


The numeric ID of the folder this project should be
created under. Only one of `org_id` or `folder_id` may be
specified. If the `folder_id` is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L251">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L255">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L264">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
`org_id` or `folder_id` may be specified. If the `org_id` is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L268">property projectId</a>
</h3>

```typescript
projectId: pulumi.Input<string>;
```


The project ID. Changing this forces a new project to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L273">property skipDelete</a>
</h3>

```typescript
skipDelete?: pulumi.Input<boolean>;
```


If true, the Terraform resource can be deleted
without deleting the Project via the Google API.

<h2 class="pdoc-module-header" id="ProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L153">interface ProjectState</a>
</h2>

Input properties used for looking up and filtering Project resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L158">property appEngine</a>
</h3>

```typescript
appEngine?: pulumi.Input<{ ... }>;
```


A block of configuration to enable an App Engine app. Setting this
field will enabled the App Engine Admin API, which is required to manage the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L166">property autoCreateNetwork</a>
</h3>

```typescript
autoCreateNetwork?: pulumi.Input<boolean>;
```


Create the 'default' network automatically.  Default true.
Note: this might be more accurately described as "Delete Default Network", since the network
is created automatically then deleted before project creation returns, but we choose this
name to match the GCP Console UI. Setting this field to false will enable the Compute Engine
API which is required to delete the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L174">property billingAccount</a>
</h3>

```typescript
billingAccount?: pulumi.Input<string>;
```


The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (`roles/billing.admin`) in
the organization. See [Google Cloud Billing API Access Control](https://cloud.google.com/billing/v1/how-tos/access-control)
for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L182">property folderId</a>
</h3>

```typescript
folderId?: pulumi.Input<string>;
```


The numeric ID of the folder this project should be
created under. Only one of `org_id` or `folder_id` may be
specified. If the `folder_id` is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L186">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L194">property number</a>
</h3>

```typescript
number?: pulumi.Input<string>;
```


The numeric identifier of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L203">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
`org_id` or `folder_id` may be specified. If the `org_id` is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L207">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```


The project ID. Changing this forces a new project to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/organizations/project.ts#L212">property skipDelete</a>
</h3>

```typescript
skipDelete?: pulumi.Input<boolean>;
```


If true, the Terraform resource can be deleted
without deleting the Project via the Google API.

