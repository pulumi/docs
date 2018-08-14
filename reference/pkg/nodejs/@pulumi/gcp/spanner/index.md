---
title: Module spanner
---

<a href="../index.html">@pulumi/gcp</a> &gt; spanner

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Database">class Database</a>
* <a href="#DatabaseIAMBinding">class DatabaseIAMBinding</a>
* <a href="#DatabaseIAMMember">class DatabaseIAMMember</a>
* <a href="#DatabaseIAMPolicy">class DatabaseIAMPolicy</a>
* <a href="#Instance">class Instance</a>
* <a href="#InstanceIAMBinding">class InstanceIAMBinding</a>
* <a href="#InstanceIAMMember">class InstanceIAMMember</a>
* <a href="#InstanceIAMPolicy">class InstanceIAMPolicy</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseIAMBindingArgs">interface DatabaseIAMBindingArgs</a>
* <a href="#DatabaseIAMBindingState">interface DatabaseIAMBindingState</a>
* <a href="#DatabaseIAMMemberArgs">interface DatabaseIAMMemberArgs</a>
* <a href="#DatabaseIAMMemberState">interface DatabaseIAMMemberState</a>
* <a href="#DatabaseIAMPolicyArgs">interface DatabaseIAMPolicyArgs</a>
* <a href="#DatabaseIAMPolicyState">interface DatabaseIAMPolicyState</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceIAMBindingArgs">interface InstanceIAMBindingArgs</a>
* <a href="#InstanceIAMBindingState">interface InstanceIAMBindingState</a>
* <a href="#InstanceIAMMemberArgs">interface InstanceIAMMemberArgs</a>
* <a href="#InstanceIAMMemberState">interface InstanceIAMMemberState</a>
* <a href="#InstanceIAMPolicyArgs">interface InstanceIAMPolicyArgs</a>
* <a href="#InstanceIAMPolicyState">interface InstanceIAMPolicyState</a>
* <a href="#InstanceState">interface InstanceState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts">spanner/database.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts">spanner/databaseIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts">spanner/databaseIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts">spanner/databaseIAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts">spanner/instance.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts">spanner/instanceIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts">spanner/instanceIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts">spanner/instanceIAMPolicy.ts</a> 


<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L9">class Database</a>
</h2>

Creates a Google Spanner Database within a Spanner Instance. For more information, see the [official documentation](https://cloud.google.com/spanner/), or the [JSON API](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L45">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L28">property ddls</a>
</h3>

```typescript
public ddls: pulumi.Output<string[] | undefined>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L32">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L41">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L45">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The current state of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L20">class DatabaseIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:

* `google_spanner_database_iam_policy`: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your database using `google_spanner_database_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_database_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.
* `google_spanner_database_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.

~> **Note:** `google_spanner_database_iam_policy` **cannot** be used in conjunction with `google_spanner_database_iam_binding` and `google_spanner_database_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_database_iam_binding` resources **can be** used in conjunction with `google_spanner_database_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L56">constructor</a>
</h3>

```typescript
new DatabaseIAMBinding(name: string, args: DatabaseIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatabaseIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseIAMBindingState): DatabaseIAMBinding
```


Get an existing DatabaseIAMBinding resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L36">property database</a>
</h3>

```typescript
public database: pulumi.Output<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L40">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L44">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L45">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L56">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L20">class DatabaseIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:

* `google_spanner_database_iam_policy`: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your database using `google_spanner_database_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_database_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.
* `google_spanner_database_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.

~> **Note:** `google_spanner_database_iam_policy` **cannot** be used in conjunction with `google_spanner_database_iam_binding` and `google_spanner_database_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_database_iam_binding` resources **can be** used in conjunction with `google_spanner_database_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L56">constructor</a>
</h3>

```typescript
new DatabaseIAMMember(name: string, args: DatabaseIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatabaseIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseIAMMemberState): DatabaseIAMMember
```


Get an existing DatabaseIAMMember resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L36">property database</a>
</h3>

```typescript
public database: pulumi.Output<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L40">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L44">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L45">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L56">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L20">class DatabaseIAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:

* `google_spanner_database_iam_policy`: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your database using `google_spanner_database_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_database_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.
* `google_spanner_database_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.

~> **Note:** `google_spanner_database_iam_policy` **cannot** be used in conjunction with `google_spanner_database_iam_binding` and `google_spanner_database_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_database_iam_binding` resources **can be** used in conjunction with `google_spanner_database_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L54">constructor</a>
</h3>

```typescript
new DatabaseIAMPolicy(name: string, args: DatabaseIAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatabaseIAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseIAMPolicyState): DatabaseIAMPolicy
```


Get an existing DatabaseIAMPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L36">property database</a>
</h3>

```typescript
public database: pulumi.Output<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L40">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L44">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L49">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L54">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L9">class Instance</a>
</h2>

Creates and manages a Google Spanner Instance. For more information, see the [official documentation](https://cloud.google.com/spanner/), or the [JSON API](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L59">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L30">property config</a>
</h3>

```typescript
public config: pulumi.Output<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L35">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L39">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L50">property numNodes</a>
</h3>

```typescript
public numNodes: pulumi.Output<number | undefined>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L55">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L59">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The current state of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="InstanceIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L20">class InstanceIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:

* `google_spanner_instance_iam_policy`: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your instance using `google_spanner_instance_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_instance_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.
* `google_spanner_instance_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.

~> **Note:** `google_spanner_instance_iam_policy` **cannot** be used in conjunction with `google_spanner_instance_iam_binding` and `google_spanner_instance_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_instance_iam_binding` resources **can be** used in conjunction with `google_spanner_instance_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L52">constructor</a>
</h3>

```typescript
new InstanceIAMBinding(name: string, args: InstanceIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a InstanceIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceIAMBindingState): InstanceIAMBinding
```


Get an existing InstanceIAMBinding resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L40">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L41">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L46">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L52">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="InstanceIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L20">class InstanceIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:

* `google_spanner_instance_iam_policy`: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your instance using `google_spanner_instance_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_instance_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.
* `google_spanner_instance_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.

~> **Note:** `google_spanner_instance_iam_policy` **cannot** be used in conjunction with `google_spanner_instance_iam_binding` and `google_spanner_instance_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_instance_iam_binding` resources **can be** used in conjunction with `google_spanner_instance_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L52">constructor</a>
</h3>

```typescript
new InstanceIAMMember(name: string, args: InstanceIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a InstanceIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceIAMMemberState): InstanceIAMMember
```


Get an existing InstanceIAMMember resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L40">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L41">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L46">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L52">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="InstanceIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L20">class InstanceIAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:

* `google_spanner_instance_iam_policy`: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.

~> **Warning:** It's entirely possibly to lock yourself out of your instance using `google_spanner_instance_iam_policy`. Any permissions granted by default will be removed unless you include them in your config.

* `google_spanner_instance_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.
* `google_spanner_instance_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.

~> **Note:** `google_spanner_instance_iam_policy` **cannot** be used in conjunction with `google_spanner_instance_iam_binding` and `google_spanner_instance_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_spanner_instance_iam_binding` resources **can be** used in conjunction with `google_spanner_instance_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L50">constructor</a>
</h3>

```typescript
new InstanceIAMPolicy(name: string, args: InstanceIAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a InstanceIAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceIAMPolicyState): InstanceIAMPolicy
```


Get an existing InstanceIAMPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L40">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L45">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L112">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L119">property ddls</a>
</h3>

```typescript
ddls?: pulumi.Input<pulumi.Input<string>[]>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L123">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L132">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L134">interface DatabaseIAMBindingArgs</a>
</h2>

The set of arguments for constructing a DatabaseIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L138">property database</a>
</h3>

```typescript
database: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L142">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L143">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L148">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L154">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="DatabaseIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L104">interface DatabaseIAMBindingState</a>
</h2>

Input properties used for looking up and filtering DatabaseIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L108">property database</a>
</h3>

```typescript
database?: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L112">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L116">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L117">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L122">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMBinding.ts#L128">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="DatabaseIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L134">interface DatabaseIAMMemberArgs</a>
</h2>

The set of arguments for constructing a DatabaseIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L138">property database</a>
</h3>

```typescript
database: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L142">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L143">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L148">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L154">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="DatabaseIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L104">interface DatabaseIAMMemberState</a>
</h2>

Input properties used for looking up and filtering DatabaseIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L108">property database</a>
</h3>

```typescript
database?: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L112">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L116">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L117">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L122">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMMember.ts#L128">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_database_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="DatabaseIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L125">interface DatabaseIAMPolicyArgs</a>
</h2>

The set of arguments for constructing a DatabaseIAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L129">property database</a>
</h3>

```typescript
database: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L133">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L138">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L143">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseIAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L97">interface DatabaseIAMPolicyState</a>
</h2>

Input properties used for looking up and filtering DatabaseIAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L101">property database</a>
</h3>

```typescript
database?: pulumi.Input<string>;
```


The name of the Spanner database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L105">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the database's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L109">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the Spanner instance the database belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L114">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/databaseIAMPolicy.ts#L119">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L82">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L89">property ddls</a>
</h3>

```typescript
ddls?: pulumi.Input<pulumi.Input<string>[]>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L93">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L102">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L106">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The current state of the database.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L147">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L156">property config</a>
</h3>

```typescript
config: pulumi.Input<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L161">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L165">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L176">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L181">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="InstanceIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L121">interface InstanceIAMBindingArgs</a>
</h2>

The set of arguments for constructing a InstanceIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L125">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L126">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L131">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L137">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="InstanceIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L95">interface InstanceIAMBindingState</a>
</h2>

Input properties used for looking up and filtering InstanceIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L99">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L103">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L104">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L109">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMBinding.ts#L115">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="InstanceIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L121">interface InstanceIAMMemberArgs</a>
</h2>

The set of arguments for constructing a InstanceIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L125">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L126">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L131">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L137">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="InstanceIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L95">interface InstanceIAMMemberState</a>
</h2>

Input properties used for looking up and filtering InstanceIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L99">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L103">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L104">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L109">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMMember.ts#L115">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_spanner_instance_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="InstanceIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L112">interface InstanceIAMPolicyArgs</a>
</h2>

The set of arguments for constructing a InstanceIAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L116">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L121">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L126">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="InstanceIAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L88">interface InstanceIAMPolicyState</a>
</h2>

Input properties used for looking up and filtering InstanceIAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L92">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the instance's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L96">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L101">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instanceIAMPolicy.ts#L106">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L103">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L112">property config</a>
</h3>

```typescript
config?: pulumi.Input<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L117">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L121">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L132">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L137">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L141">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The current state of the instance.

