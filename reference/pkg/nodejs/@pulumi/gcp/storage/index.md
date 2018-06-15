---
title: Module storage
---

<a href="../index.html">@pulumi/gcp</a> &gt; storage

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Bucket">class Bucket</a>
* <a href="#BucketACL">class BucketACL</a>
* <a href="#BucketIAMBinding">class BucketIAMBinding</a>
* <a href="#BucketIAMMember">class BucketIAMMember</a>
* <a href="#BucketObject">class BucketObject</a>
* <a href="#DefaultObjectACL">class DefaultObjectACL</a>
* <a href="#Notification">class Notification</a>
* <a href="#ObjectACL">class ObjectACL</a>
* <a href="#getObjectSignedUrl">function getObjectSignedUrl</a>
* <a href="#getProjectServiceAccount">function getProjectServiceAccount</a>
* <a href="#BucketACLArgs">interface BucketACLArgs</a>
* <a href="#BucketACLState">interface BucketACLState</a>
* <a href="#BucketArgs">interface BucketArgs</a>
* <a href="#BucketIAMBindingArgs">interface BucketIAMBindingArgs</a>
* <a href="#BucketIAMBindingState">interface BucketIAMBindingState</a>
* <a href="#BucketIAMMemberArgs">interface BucketIAMMemberArgs</a>
* <a href="#BucketIAMMemberState">interface BucketIAMMemberState</a>
* <a href="#BucketObjectArgs">interface BucketObjectArgs</a>
* <a href="#BucketObjectState">interface BucketObjectState</a>
* <a href="#BucketState">interface BucketState</a>
* <a href="#DefaultObjectACLArgs">interface DefaultObjectACLArgs</a>
* <a href="#DefaultObjectACLState">interface DefaultObjectACLState</a>
* <a href="#GetObjectSignedUrlArgs">interface GetObjectSignedUrlArgs</a>
* <a href="#GetObjectSignedUrlResult">interface GetObjectSignedUrlResult</a>
* <a href="#NotificationArgs">interface NotificationArgs</a>
* <a href="#NotificationState">interface NotificationState</a>
* <a href="#ObjectACLArgs">interface ObjectACLArgs</a>
* <a href="#ObjectACLState">interface ObjectACLState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts">storage/bucket.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts">storage/bucketACL.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts">storage/bucketIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts">storage/bucketIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts">storage/bucketObject.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts">storage/defaultObjectACL.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts">storage/getObjectSignedUrl.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getProjectServiceAccount.ts">storage/getProjectServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts">storage/notification.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts">storage/objectACL.ts</a> 


<h2 class="pdoc-module-header" id="Bucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L16">class Bucket</a>
</h2>

Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can't be changed.
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `google_storage_bucket_acl` resource.
For more information see
[the official documentation](https://cloud.google.com/storage/docs/overview)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L83">constructor</a>
</h3>

```typescript
new Bucket(name: string, args?: BucketArgs, opts?: pulumi.ResourceOptions)
```


Create a Bucket resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketState): Bucket
```


Get an existing Bucket resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L32">property cors</a>
</h3>

```typescript
public cors: pulumi.Output<{ ... }[] | undefined>;
```


The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L38">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L42">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L46">property lifecycleRules</a>
</h3>

```typescript
public lifecycleRules: pulumi.Output<{ ... }[] | undefined>;
```


The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L50">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L54">property logging</a>
</h3>

```typescript
public logging: pulumi.Output<{ ... } | undefined>;
```


The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L63">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L67">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L71">property storageClass</a>
</h3>

```typescript
public storageClass: pulumi.Output<string | undefined>;
```


The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L75">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The base URL of the bucket, in the format `gs://<bucket-name>`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L79">property versioning</a>
</h3>

```typescript
public versioning: pulumi.Output<{ ... } | undefined>;
```


The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L83">property websites</a>
</h3>

```typescript
public websites: pulumi.Output<{ ... }[] | undefined>;
```


Configuration if the bucket acts as a website. Structure is documented below.

<h2 class="pdoc-module-header" id="BucketACL">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L12">class BucketACL</a>
</h2>

Creates a new bucket ACL in Google cloud storage service (GCS). For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L40">constructor</a>
</h3>

```typescript
new BucketACL(name: string, args: BucketACLArgs, opts?: pulumi.ResourceOptions)
```


Create a BucketACL resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketACLState): BucketACL
```


Get an existing BucketACL resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L28">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L32">property defaultAcl</a>
</h3>

```typescript
public defaultAcl: pulumi.Output<string | undefined>;
```


Configure this ACL to be the default ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L36">property predefinedAcl</a>
</h3>

```typescript
public predefinedAcl: pulumi.Output<string | undefined>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L40">property roleEntities</a>
</h3>

```typescript
public roleEntities: pulumi.Output<string[] | undefined>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BucketIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L16">class BucketIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:

* `google_storage_bucket_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.
* `google_storage_bucket_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.
* `google_storage_bucket_iam_policy`: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there's a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.


~> **Note:** `google_storage_bucket_iam_binding` resources **can be** used in conjunction with `google_storage_bucket_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L42">constructor</a>
</h3>

```typescript
new BucketIAMBinding(name: string, args: BucketIAMBindingArgs, opts?: pulumi.ResourceOptions)
```


Create a BucketIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketIAMBindingState): BucketIAMBinding
```


Get an existing BucketIAMBinding resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L32">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the storage bucket's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L37">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L42">property role</a>
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

<h2 class="pdoc-module-header" id="BucketIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L16">class BucketIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:

* `google_storage_bucket_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.
* `google_storage_bucket_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.
* `google_storage_bucket_iam_policy`: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there's a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.


~> **Note:** `google_storage_bucket_iam_binding` resources **can be** used in conjunction with `google_storage_bucket_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L42">constructor</a>
</h3>

```typescript
new BucketIAMMember(name: string, args: BucketIAMMemberArgs, opts?: pulumi.ResourceOptions)
```


Create a BucketIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketIAMMemberState): BucketIAMMember
```


Get an existing BucketIAMMember resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L32">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L36">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the storage bucket's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L37">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L42">property role</a>
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

<h2 class="pdoc-module-header" id="BucketObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L15">class BucketObject</a>
</h2>

Creates a new object inside an existing bucket in Google cloud storage service (GCS).
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `google_storage_object_acl` resource.
 For more information see
[the official documentation](https://cloud.google.com/storage/docs/key-terms#objects)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/objects).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L81">constructor</a>
</h3>

```typescript
new BucketObject(name: string, args: BucketObjectArgs, opts?: pulumi.ResourceOptions)
```


Create a BucketObject resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketObjectState): BucketObject
```


Get an existing BucketObject resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L31">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the containing bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L36">property cacheControl</a>
</h3>

```typescript
public cacheControl: pulumi.Output<string | undefined>;
```


[Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L41">property content</a>
</h3>

```typescript
public content: pulumi.Output<string | undefined>;
```


Data as `string` to be uploaded. Must be defined if
`source` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L45">property contentDisposition</a>
</h3>

```typescript
public contentDisposition: pulumi.Output<string | undefined>;
```


[Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L49">property contentEncoding</a>
</h3>

```typescript
public contentEncoding: pulumi.Output<string | undefined>;
```


[Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L53">property contentLanguage</a>
</h3>

```typescript
public contentLanguage: pulumi.Output<string | undefined>;
```


[Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L57">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string>;
```


[Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L61">property crc32c</a>
</h3>

```typescript
public crc32c: pulumi.Output<string>;
```


(Computed) Base 64 CRC32 hash of the uploaded data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L62">property detectMd5hash</a>
</h3>

```typescript
public detectMd5hash: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L66">property md5hash</a>
</h3>

```typescript
public md5hash: pulumi.Output<string>;
```


(Computed) Base 64 MD5 hash of the uploaded data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L70">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L75">property source</a>
</h3>

```typescript
public source: pulumi.Output<string | undefined>;
```


A path to the data you want to upload. Must be defined
if `content` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L81">property storageClass</a>
</h3>

```typescript
public storageClass: pulumi.Output<string>;
```


The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`. If not provided, this defaults to the bucket's default
storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DefaultObjectACL">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L12">class DefaultObjectACL</a>
</h2>

Creates a new default object ACL in Google Cloud Storage service (GCS). For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L32">constructor</a>
</h3>

```typescript
new DefaultObjectACL(name: string, args: DefaultObjectACLArgs, opts?: pulumi.ResourceOptions)
```


Create a DefaultObjectACL resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultObjectACLState): DefaultObjectACL
```


Get an existing DefaultObjectACL resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L28">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L32">property roleEntities</a>
</h3>

```typescript
public roleEntities: pulumi.Output<string[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Notification">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L13">class Notification</a>
</h2>

Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
 For more information see
[the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/notifications).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L55">constructor</a>
</h3>

```typescript
new Notification(name: string, args: NotificationArgs, opts?: pulumi.ResourceOptions)
```


Create a Notification resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotificationState): Notification
```


Get an existing Notification resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L29">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L33">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L37">property eventTypes</a>
</h3>

```typescript
public eventTypes: pulumi.Output<string[] | undefined>;
```


List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L41">property objectNamePrefix</a>
</h3>

```typescript
public objectNamePrefix: pulumi.Output<string | undefined>;
```


Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L45">property payloadFormat</a>
</h3>

```typescript
public payloadFormat: pulumi.Output<string>;
```


The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L49">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L55">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<string>;
```


The Cloud PubSub topic to which this subscription publishes. Expects either the
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ObjectACL">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L12">class ObjectACL</a>
</h2>

Creates a new object ACL in Google cloud storage service (GCS). For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L40">constructor</a>
</h3>

```typescript
new ObjectACL(name: string, args: ObjectACLArgs, opts?: pulumi.ResourceOptions)
```


Create a ObjectACL resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObjectACLState): ObjectACL
```


Get an existing ObjectACL resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L28">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L32">property object</a>
</h3>

```typescript
public object: pulumi.Output<string>;
```


The name of the object it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L36">property predefinedAcl</a>
</h3>

```typescript
public predefinedAcl: pulumi.Output<string | undefined>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L40">property roleEntities</a>
</h3>

```typescript
public roleEntities: pulumi.Output<string[] | undefined>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details. Must be set if `predefined_acl` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getObjectSignedUrl">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L11">function getObjectSignedUrl</a>
</h2>

```typescript
getObjectSignedUrl(args: GetObjectSignedUrlArgs): Promise<GetObjectSignedUrlResult>
```


The Google Cloud storage signed URL data source generates a signed URL for a given storage object. Signed URLs provide a way to give time-limited read or write access to anyone in possession of the URL, regardless of whether they have a Google account.

For more info about signed URL's is available [here](https://cloud.google.com/storage/docs/access-control/signed-urls).

<h2 class="pdoc-module-header" id="getProjectServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getProjectServiceAccount.ts#L11">function getProjectServiceAccount</a>
</h2>

```typescript
getProjectServiceAccount(): Promise<void>
```


Use this data source to get the email address of the project's Google Cloud Storage service account.
 For more information see
[API](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount).

<h2 class="pdoc-module-header" id="BucketACLArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L97">interface BucketACLArgs</a>
</h2>

The set of arguments for constructing a BucketACL resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L101">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L105">property defaultAcl</a>
</h3>

```typescript
defaultAcl?: pulumi.Input<string>;
```


Configure this ACL to be the default ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L109">property predefinedAcl</a>
</h3>

```typescript
predefinedAcl?: pulumi.Input<string>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L113">property roleEntities</a>
</h3>

```typescript
roleEntities?: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.

<h2 class="pdoc-module-header" id="BucketACLState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L75">interface BucketACLState</a>
</h2>

Input properties used for looking up and filtering BucketACL resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L79">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L83">property defaultAcl</a>
</h3>

```typescript
defaultAcl?: pulumi.Input<string>;
```


Configure this ACL to be the default ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L87">property predefinedAcl</a>
</h3>

```typescript
predefinedAcl?: pulumi.Input<string>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketACL.ts#L91">property roleEntities</a>
</h3>

```typescript
roleEntities?: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.

<h2 class="pdoc-module-header" id="BucketArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L194">interface BucketArgs</a>
</h2>

The set of arguments for constructing a Bucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L198">property cors</a>
</h3>

```typescript
cors?: pulumi.Input<{ ... }[]>;
```


The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L204">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L208">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L212">property lifecycleRules</a>
</h3>

```typescript
lifecycleRules?: pulumi.Input<{ ... }[]>;
```


The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L216">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L220">property logging</a>
</h3>

```typescript
logging?: pulumi.Input<{ ... }>;
```


The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L229">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L233">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L237">property versioning</a>
</h3>

```typescript
versioning?: pulumi.Input<{ ... }>;
```


The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L241">property websites</a>
</h3>

```typescript
websites?: pulumi.Input<{ ... }[]>;
```


Configuration if the bucket acts as a website. Structure is documented below.

<h2 class="pdoc-module-header" id="BucketIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L103">interface BucketIAMBindingArgs</a>
</h2>

The set of arguments for constructing a BucketIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L107">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L108">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L113">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="BucketIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L83">interface BucketIAMBindingState</a>
</h2>

Input properties used for looking up and filtering BucketIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L87">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L91">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the storage bucket's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L92">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMBinding.ts#L97">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="BucketIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L103">interface BucketIAMMemberArgs</a>
</h2>

The set of arguments for constructing a BucketIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L107">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L108">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L113">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="BucketIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L83">interface BucketIAMMemberState</a>
</h2>

Input properties used for looking up and filtering BucketIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L87">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L91">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the storage bucket's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L92">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketIAMMember.ts#L97">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="BucketObjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L194">interface BucketObjectArgs</a>
</h2>

The set of arguments for constructing a BucketObject resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L198">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the containing bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L203">property cacheControl</a>
</h3>

```typescript
cacheControl?: pulumi.Input<string>;
```


[Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L208">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


Data as `string` to be uploaded. Must be defined if
`source` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L212">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


[Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L216">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


[Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L220">property contentLanguage</a>
</h3>

```typescript
contentLanguage?: pulumi.Input<string>;
```


[Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L224">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


[Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L225">property detectMd5hash</a>
</h3>

```typescript
detectMd5hash?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L229">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L234">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


A path to the data you want to upload. Must be defined
if `content` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L240">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`. If not provided, this defaults to the bucket's default
storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.

<h2 class="pdoc-module-header" id="BucketObjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L134">interface BucketObjectState</a>
</h2>

Input properties used for looking up and filtering BucketObject resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L138">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the containing bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L143">property cacheControl</a>
</h3>

```typescript
cacheControl?: pulumi.Input<string>;
```


[Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L148">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


Data as `string` to be uploaded. Must be defined if
`source` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L152">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


[Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L156">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


[Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L160">property contentLanguage</a>
</h3>

```typescript
contentLanguage?: pulumi.Input<string>;
```


[Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L164">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


[Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L168">property crc32c</a>
</h3>

```typescript
crc32c?: pulumi.Input<string>;
```


(Computed) Base 64 CRC32 hash of the uploaded data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L169">property detectMd5hash</a>
</h3>

```typescript
detectMd5hash?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L173">property md5hash</a>
</h3>

```typescript
md5hash?: pulumi.Input<string>;
```


(Computed) Base 64 MD5 hash of the uploaded data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L177">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L182">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


A path to the data you want to upload. Must be defined
if `content` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucketObject.ts#L188">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`. If not provided, this defaults to the bucket's default
storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.

<h2 class="pdoc-module-header" id="BucketState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L133">interface BucketState</a>
</h2>

Input properties used for looking up and filtering Bucket resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L137">property cors</a>
</h3>

```typescript
cors?: pulumi.Input<{ ... }[]>;
```


The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L143">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L147">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L151">property lifecycleRules</a>
</h3>

```typescript
lifecycleRules?: pulumi.Input<{ ... }[]>;
```


The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L155">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L159">property logging</a>
</h3>

```typescript
logging?: pulumi.Input<{ ... }>;
```


The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L163">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L168">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L172">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L176">property storageClass</a>
</h3>

```typescript
storageClass?: pulumi.Input<string>;
```


The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L180">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The base URL of the bucket, in the format `gs://<bucket-name>`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L184">property versioning</a>
</h3>

```typescript
versioning?: pulumi.Input<{ ... }>;
```


The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/bucket.ts#L188">property websites</a>
</h3>

```typescript
websites?: pulumi.Input<{ ... }[]>;
```


Configuration if the bucket acts as a website. Structure is documented below.

<h2 class="pdoc-module-header" id="DefaultObjectACLArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L80">interface DefaultObjectACLArgs</a>
</h2>

The set of arguments for constructing a DefaultObjectACL resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L84">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L88">property roleEntities</a>
</h3>

```typescript
roleEntities: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.

<h2 class="pdoc-module-header" id="DefaultObjectACLState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L66">interface DefaultObjectACLState</a>
</h2>

Input properties used for looking up and filtering DefaultObjectACL resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L70">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/defaultObjectACL.ts#L74">property roleEntities</a>
</h3>

```typescript
roleEntities?: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.

<h2 class="pdoc-module-header" id="GetObjectSignedUrlArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L27">interface GetObjectSignedUrlArgs</a>
</h2>

A collection of arguments for invoking getObjectSignedUrl.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L31">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket to read the object from

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L37">property contentMd5</a>
</h3>

```typescript
contentMd5?: pulumi.Input<string>;
```


The [MD5 digest](https://cloud.google.com/storage/docs/hashes-etags#_MD5) value in Base64.
Typically retrieved from `google_storage_bucket_object.object.md5hash` attribute.
If you provide this in the datasource, the client (e.g. browser, curl) must provide the `Content-MD5` HTTP header with this same value in its request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L41">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


If you specify this in the datasource, the client must provide the `Content-Type` HTTP header with the same value in its request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L46">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```


What Google service account credentials json should be used to sign the URL.
This data source checks the following locations for credentials, in order of preference: data source `credentials` attribute, provider `credentials` attribute and finally the GOOGLE_APPLICATION_CREDENTIALS environment variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L51">property duration</a>
</h3>

```typescript
duration?: pulumi.Input<string>;
```


For how long shall the signed URL be valid (defaults to 1 hour - i.e. `1h`).
See [here](https://golang.org/pkg/time/#ParseDuration) for info on valid duration formats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L56">property extensionHeaders</a>
</h3>

```typescript
extensionHeaders?: pulumi.Input<{ ... }>;
```


As needed. The server checks to make sure that the client provides matching values in requests using the signed URL.
Any header starting with `x-goog-` is accepted but see the [Google Docs](https://cloud.google.com/storage/docs/xml-api/reference-headers) for list of headers that are supported by Google.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L60">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


What HTTP Method will the signed URL allow (defaults to `GET`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L64">property path</a>
</h3>

```typescript
path: pulumi.Input<string>;
```


The full path to the object inside the bucket

<h2 class="pdoc-module-header" id="GetObjectSignedUrlResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L70">interface GetObjectSignedUrlResult</a>
</h2>

A collection of values returned by getObjectSignedUrl.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/getObjectSignedUrl.ts#L74">property signedUrl</a>
</h3>

```typescript
signedUrl: string;
```


The signed URL that can be used to access the storage object without authentication.

<h2 class="pdoc-module-header" id="NotificationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L138">interface NotificationArgs</a>
</h2>

The set of arguments for constructing a Notification resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L142">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L146">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L150">property eventTypes</a>
</h3>

```typescript
eventTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L154">property objectNamePrefix</a>
</h3>

```typescript
objectNamePrefix?: pulumi.Input<string>;
```


Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L158">property payloadFormat</a>
</h3>

```typescript
payloadFormat: pulumi.Input<string>;
```


The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L164">property topic</a>
</h3>

```typescript
topic: pulumi.Input<string>;
```


The Cloud PubSub topic to which this subscription publishes. Expects either the
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`.

<h2 class="pdoc-module-header" id="NotificationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L102">interface NotificationState</a>
</h2>

Input properties used for looking up and filtering Notification resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L106">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L110">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L114">property eventTypes</a>
</h3>

```typescript
eventTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L118">property objectNamePrefix</a>
</h3>

```typescript
objectNamePrefix?: pulumi.Input<string>;
```


Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L122">property payloadFormat</a>
</h3>

```typescript
payloadFormat?: pulumi.Input<string>;
```


The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L126">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/notification.ts#L132">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<string>;
```


The Cloud PubSub topic to which this subscription publishes. Expects either the
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`.

<h2 class="pdoc-module-header" id="ObjectACLArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L100">interface ObjectACLArgs</a>
</h2>

The set of arguments for constructing a ObjectACL resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L104">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L108">property object</a>
</h3>

```typescript
object: pulumi.Input<string>;
```


The name of the object it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L112">property predefinedAcl</a>
</h3>

```typescript
predefinedAcl?: pulumi.Input<string>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L116">property roleEntities</a>
</h3>

```typescript
roleEntities?: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details. Must be set if `predefined_acl` is not.

<h2 class="pdoc-module-header" id="ObjectACLState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L78">interface ObjectACLState</a>
</h2>

Input properties used for looking up and filtering ObjectACL resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L82">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


The name of the bucket it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L86">property object</a>
</h3>

```typescript
object?: pulumi.Input<string>;
```


The name of the object it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L90">property predefinedAcl</a>
</h3>

```typescript
predefinedAcl?: pulumi.Input<string>;
```


The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/storage/objectACL.ts#L94">property roleEntities</a>
</h3>

```typescript
roleEntities?: pulumi.Input<pulumi.Input<string>[]>;
```


List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details. Must be set if `predefined_acl` is not.

