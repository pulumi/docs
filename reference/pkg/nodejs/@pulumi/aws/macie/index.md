---
title: Module macie
---

<a href="../index.html">@pulumi/aws</a> &gt; macie

<h2 class="pdoc-module-header">Index</h2>

* <a href="#MemberAccountAssociation">class MemberAccountAssociation</a>
* <a href="#S3BucketAssociation">class S3BucketAssociation</a>
* <a href="#MemberAccountAssociationArgs">interface MemberAccountAssociationArgs</a>
* <a href="#MemberAccountAssociationState">interface MemberAccountAssociationState</a>
* <a href="#S3BucketAssociationArgs">interface S3BucketAssociationArgs</a>
* <a href="#S3BucketAssociationState">interface S3BucketAssociationState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts">macie/memberAccountAssociation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts">macie/s3BucketAssociation.ts</a> 


<h2 class="pdoc-module-header" id="MemberAccountAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L12">class MemberAccountAssociation</a>
</h2>

Associates an AWS account with Amazon Macie as a member account.

~> **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L28">constructor</a>
</h3>

```typescript
new MemberAccountAssociation(name: string, args: MemberAccountAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MemberAccountAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberAccountAssociationState): MemberAccountAssociation
```


Get an existing MemberAccountAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L28">property memberAccountId</a>
</h3>

```typescript
public memberAccountId: pulumi.Output<string>;
```


The ID of the AWS account that you want to associate with Amazon Macie as a member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="S3BucketAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L12">class S3BucketAssociation</a>
</h2>

Associates an S3 resource with Amazon Macie for monitoring and data classification.

~> **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L40">constructor</a>
</h3>

```typescript
new S3BucketAssociation(name: string, args: S3BucketAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a S3BucketAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: S3BucketAssociationState): S3BucketAssociation
```


Get an existing S3BucketAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L28">property bucketName</a>
</h3>

```typescript
public bucketName: pulumi.Output<string>;
```


The name of the S3 bucket that you want to associate with Amazon Macie.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L32">property classificationType</a>
</h3>

```typescript
public classificationType: pulumi.Output<{ ... }>;
```


The configuration of how Amazon Macie classifies the S3 objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L36">property memberAccountId</a>
</h3>

```typescript
public memberAccountId: pulumi.Output<string | undefined>;
```


The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L40">property prefix</a>
</h3>

```typescript
public prefix: pulumi.Output<string | undefined>;
```


Object key prefix identifying one or more S3 objects to which the association applies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MemberAccountAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L67">interface MemberAccountAssociationArgs</a>
</h2>

The set of arguments for constructing a MemberAccountAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L71">property memberAccountId</a>
</h3>

```typescript
memberAccountId: pulumi.Input<string>;
```


The ID of the AWS account that you want to associate with Amazon Macie as a member account.

<h2 class="pdoc-module-header" id="MemberAccountAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L57">interface MemberAccountAssociationState</a>
</h2>

Input properties used for looking up and filtering MemberAccountAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/memberAccountAssociation.ts#L61">property memberAccountId</a>
</h3>

```typescript
memberAccountId?: pulumi.Input<string>;
```


The ID of the AWS account that you want to associate with Amazon Macie as a member account.

<h2 class="pdoc-module-header" id="S3BucketAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L97">interface S3BucketAssociationArgs</a>
</h2>

The set of arguments for constructing a S3BucketAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L101">property bucketName</a>
</h3>

```typescript
bucketName: pulumi.Input<string>;
```


The name of the S3 bucket that you want to associate with Amazon Macie.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L105">property classificationType</a>
</h3>

```typescript
classificationType?: pulumi.Input<{ ... }>;
```


The configuration of how Amazon Macie classifies the S3 objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L109">property memberAccountId</a>
</h3>

```typescript
memberAccountId?: pulumi.Input<string>;
```


The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L113">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```


Object key prefix identifying one or more S3 objects to which the association applies.

<h2 class="pdoc-module-header" id="S3BucketAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L75">interface S3BucketAssociationState</a>
</h2>

Input properties used for looking up and filtering S3BucketAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L79">property bucketName</a>
</h3>

```typescript
bucketName?: pulumi.Input<string>;
```


The name of the S3 bucket that you want to associate with Amazon Macie.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L83">property classificationType</a>
</h3>

```typescript
classificationType?: pulumi.Input<{ ... }>;
```


The configuration of how Amazon Macie classifies the S3 objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L87">property memberAccountId</a>
</h3>

```typescript
memberAccountId?: pulumi.Input<string>;
```


The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/macie/s3BucketAssociation.ts#L91">property prefix</a>
</h3>

```typescript
prefix?: pulumi.Input<string>;
```


Object key prefix identifying one or more S3 objects to which the association applies.

