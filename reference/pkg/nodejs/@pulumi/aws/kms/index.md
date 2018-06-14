---
title: Module kms
---

<a href="../index.html">@pulumi/aws</a> &gt; kms

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Alias">class Alias</a>
* <a href="#Grant">class Grant</a>
* <a href="#Key">class Key</a>
* <a href="#getAlias">function getAlias</a>
* <a href="#getCipherText">function getCipherText</a>
* <a href="#getKey">function getKey</a>
* <a href="#getSecret">function getSecret</a>
* <a href="#AliasArgs">interface AliasArgs</a>
* <a href="#AliasState">interface AliasState</a>
* <a href="#GetAliasArgs">interface GetAliasArgs</a>
* <a href="#GetAliasResult">interface GetAliasResult</a>
* <a href="#GetCipherTextArgs">interface GetCipherTextArgs</a>
* <a href="#GetCipherTextResult">interface GetCipherTextResult</a>
* <a href="#GetKeyArgs">interface GetKeyArgs</a>
* <a href="#GetKeyResult">interface GetKeyResult</a>
* <a href="#GetSecretArgs">interface GetSecretArgs</a>
* <a href="#GrantArgs">interface GrantArgs</a>
* <a href="#GrantState">interface GrantState</a>
* <a href="#KeyArgs">interface KeyArgs</a>
* <a href="#KeyState">interface KeyState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts">kms/alias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts">kms/getAlias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts">kms/getCipherText.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts">kms/getKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getSecret.ts">kms/getSecret.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts">kms/grant.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts">kms/key.ts</a> 


<h2 class="pdoc-module-header" id="Alias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L11">class Alias</a>
</h2>

Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
but API (hence Terraform too) allows you to create as many aliases as
the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L44">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.ResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AliasState): Alias
```


Get an existing Alias resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the key alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L36">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates an unique alias beginning with the specified prefix.
The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L40">property targetKeyArn</a>
</h3>

```typescript
public targetKeyArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the target key identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L44">property targetKeyId</a>
</h3>

```typescript
public targetKeyId: pulumi.Output<string>;
```


Identifier for the key for which the alias is for, can be either an ARN or key_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Grant">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L9">class Grant</a>
</h2>

Provides a resource-based access control mechanism for a KMS customer master key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L57">constructor</a>
</h3>

```typescript
new Grant(name: string, args: GrantArgs, opts?: pulumi.ResourceOptions)
```


Create a Grant resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GrantState): Grant
```


Get an existing Grant resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L25">property constraints</a>
</h3>

```typescript
public constraints: pulumi.Output<{ ... }[] | undefined>;
```


A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L31">property grantCreationTokens</a>
</h3>

```typescript
public grantCreationTokens: pulumi.Output<string[] | undefined>;
```


A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
* `retire_on_delete` -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L35">property grantId</a>
</h3>

```typescript
public grantId: pulumi.Output<string>;
```


The unique identifier for the grant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L39">property grantToken</a>
</h3>

```typescript
public grantToken: pulumi.Output<string>;
```


The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L43">property granteePrincipal</a>
</h3>

```typescript
public granteePrincipal: pulumi.Output<string>;
```


The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L47">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


The unique identifier for the customer master key (CMK) that the grant applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A friendly name for identifying the grant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L55">property operations</a>
</h3>

```typescript
public operations: pulumi.Output<string[]>;
```


A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L56">property retireOnDelete</a>
</h3>

```typescript
public retireOnDelete: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L57">property retiringPrincipal</a>
</h3>

```typescript
public retiringPrincipal: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Key">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L9">class Key</a>
</h2>

Provides a KMS customer master key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L60">constructor</a>
</h3>

```typescript
new Key(name: string, args?: KeyArgs, opts?: pulumi.ResourceOptions)
```


Create a Key resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyState): Key
```


Get an existing Key resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L30">property deletionWindowInDays</a>
</h3>

```typescript
public deletionWindowInDays: pulumi.Output<number | undefined>;
```


Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the key as viewed in AWS console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L39">property enableKeyRotation</a>
</h3>

```typescript
public enableKeyRotation: pulumi.Output<boolean | undefined>;
```


Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
is enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L43">property isEnabled</a>
</h3>

```typescript
public isEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the key is enabled. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L47">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


The globally unique identifier for the key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L52">property keyUsage</a>
</h3>

```typescript
public keyUsage: pulumi.Output<string>;
```


Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L56">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


A valid policy JSON document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L60">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAlias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L11">function getAlias</a>
</h2>

```typescript
getAlias(args: GetAliasArgs): Promise<GetAliasResult>
```


Use this data source to get the ARN of a KMS key alias.
By using this data source, you can reference key alias
without having to hard code the ARN as input.

<h2 class="pdoc-module-header" id="getCipherText">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L13">function getCipherText</a>
</h2>

```typescript
getCipherText(args: GetCipherTextArgs): Promise<GetCipherTextResult>
```


The KMS ciphertext data source allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key.

~> **Note:** All arguments including the plaintext be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h2 class="pdoc-module-header" id="getKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L12">function getKey</a>
</h2>

```typescript
getKey(args: GetKeyArgs): Promise<GetKeyResult>
```


Use this data source to get detailed information about
the specified KMS Key with flexible key id input.
This can be useful to reference key alias
without having to hard code the ARN as input.

<h2 class="pdoc-module-header" id="getSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getSecret.ts#L16">function getSecret</a>
</h2>

```typescript
getSecret(args: GetSecretArgs): Promise<void>
```


The KMS secret data source allows you to use data encrypted with the AWS KMS
service within your resource definitions.

~> **NOTE**: Using this data provider will allow you to conceal secret data within your
resource definitions but does not take care of protecting that data in the
logging output, plan output or state output.

Please take care to secure your secret data outside of resource definitions.

<h2 class="pdoc-module-header" id="AliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L108">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L117">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates an unique alias beginning with the specified prefix.
The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L121">property targetKeyId</a>
</h3>

```typescript
targetKeyId: pulumi.Input<string>;
```


Identifier for the key for which the alias is for, can be either an ARN or key_id.

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L81">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L85">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the key alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L94">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates an unique alias beginning with the specified prefix.
The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L98">property targetKeyArn</a>
</h3>

```typescript
targetKeyArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the target key identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/alias.ts#L102">property targetKeyId</a>
</h3>

```typescript
targetKeyId?: pulumi.Input<string>;
```


Identifier for the key for which the alias is for, can be either an ARN or key_id.

<h2 class="pdoc-module-header" id="GetAliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L20">interface GetAliasArgs</a>
</h2>

A collection of arguments for invoking getAlias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)

<h2 class="pdoc-module-header" id="GetAliasResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L30">interface GetAliasResult</a>
</h2>

A collection of values returned by getAlias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L34">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name(ARN) of the key alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L38">property targetKeyArn</a>
</h3>

```typescript
targetKeyArn: string;
```


ARN pointed to by the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getAlias.ts#L42">property targetKeyId</a>
</h3>

```typescript
targetKeyId: string;
```


Key identifier pointed to by the alias.

<h2 class="pdoc-module-header" id="GetCipherTextArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L24">interface GetCipherTextArgs</a>
</h2>

A collection of arguments for invoking getCipherText.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L28">property context</a>
</h3>

```typescript
context?: pulumi.Input<{ ... }>;
```


An optional mapping that makes up the encryption context.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L32">property keyId</a>
</h3>

```typescript
keyId: pulumi.Input<string>;
```


Globally unique key ID for the customer master key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L36">property plaintext</a>
</h3>

```typescript
plaintext: pulumi.Input<string>;
```


Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.

<h2 class="pdoc-module-header" id="GetCipherTextResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L42">interface GetCipherTextResult</a>
</h2>

A collection of values returned by getCipherText.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getCipherText.ts#L46">property ciphertextBlob</a>
</h3>

```typescript
ciphertextBlob: string;
```


Base64 encoded ciphertext

<h2 class="pdoc-module-header" id="GetKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L22">interface GetKeyArgs</a>
</h2>

A collection of arguments for invoking getKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L26">property grantTokens</a>
</h3>

```typescript
grantTokens?: pulumi.Input<pulumi.Input<string>[]>;
```


List of grant tokens

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L34">property keyId</a>
</h3>

```typescript
keyId: pulumi.Input<string>;
```


Key identifier which can be one of the following format:
* Key ID. E.g: `1234abcd-12ab-34cd-56ef-1234567890ab`
* Key ARN. E.g.: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
* Alias name. E.g.: `alias/my-key`
* Alias ARN: E.g.: `arn:aws:kms:us-east-1:111122223333:alias/my-key`

<h2 class="pdoc-module-header" id="GetKeyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L40">interface GetKeyResult</a>
</h2>

A collection of values returned by getKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L41">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L42">property awsAccountId</a>
</h3>

```typescript
awsAccountId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L43">property creationDate</a>
</h3>

```typescript
creationDate: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L44">property deletionDate</a>
</h3>

```typescript
deletionDate: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L45">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L46">property enabled</a>
</h3>

```typescript
enabled: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L47">property expirationModel</a>
</h3>

```typescript
expirationModel: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L48">property keyManager</a>
</h3>

```typescript
keyManager: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L49">property keyState</a>
</h3>

```typescript
keyState: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L50">property keyUsage</a>
</h3>

```typescript
keyUsage: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L51">property origin</a>
</h3>

```typescript
origin: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getKey.ts#L52">property validTo</a>
</h3>

```typescript
validTo: string;
```

<h2 class="pdoc-module-header" id="GetSecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getSecret.ts#L26">interface GetSecretArgs</a>
</h2>

A collection of arguments for invoking getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getSecret.ts#L27">property __hasDynamicAttributes</a>
</h3>

```typescript
__hasDynamicAttributes?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/getSecret.ts#L32">property secrets</a>
</h3>

```typescript
secrets: pulumi.Input<{ ... }[]>;
```


One or more encrypted payload definitions from the KMS
service.  See the Secret Definitions below.

<h2 class="pdoc-module-header" id="GrantArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L152">interface GrantArgs</a>
</h2>

The set of arguments for constructing a Grant resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L156">property constraints</a>
</h3>

```typescript
constraints?: pulumi.Input<{ ... }[]>;
```


A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L162">property grantCreationTokens</a>
</h3>

```typescript
grantCreationTokens?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
* `retire_on_delete` -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L166">property granteePrincipal</a>
</h3>

```typescript
granteePrincipal: pulumi.Input<string>;
```


The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L170">property keyId</a>
</h3>

```typescript
keyId: pulumi.Input<string>;
```


The unique identifier for the customer master key (CMK) that the grant applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for identifying the grant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L178">property operations</a>
</h3>

```typescript
operations: pulumi.Input<pulumi.Input<string>[]>;
```


A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L179">property retireOnDelete</a>
</h3>

```typescript
retireOnDelete?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L180">property retiringPrincipal</a>
</h3>

```typescript
retiringPrincipal?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="GrantState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L110">interface GrantState</a>
</h2>

Input properties used for looking up and filtering Grant resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L114">property constraints</a>
</h3>

```typescript
constraints?: pulumi.Input<{ ... }[]>;
```


A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L120">property grantCreationTokens</a>
</h3>

```typescript
grantCreationTokens?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
* `retire_on_delete` -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L124">property grantId</a>
</h3>

```typescript
grantId?: pulumi.Input<string>;
```


The unique identifier for the grant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L128">property grantToken</a>
</h3>

```typescript
grantToken?: pulumi.Input<string>;
```


The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L132">property granteePrincipal</a>
</h3>

```typescript
granteePrincipal?: pulumi.Input<string>;
```


The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L136">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The unique identifier for the customer master key (CMK) that the grant applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for identifying the grant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L144">property operations</a>
</h3>

```typescript
operations?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L145">property retireOnDelete</a>
</h3>

```typescript
retireOnDelete?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/grant.ts#L146">property retiringPrincipal</a>
</h3>

```typescript
retiringPrincipal?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="KeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L147">interface KeyArgs</a>
</h2>

The set of arguments for constructing a Key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L152">property deletionWindowInDays</a>
</h3>

```typescript
deletionWindowInDays?: pulumi.Input<number>;
```


Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L156">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the key as viewed in AWS console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L161">property enableKeyRotation</a>
</h3>

```typescript
enableKeyRotation?: pulumi.Input<boolean>;
```


Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
is enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L165">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Specifies whether the key is enabled. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L170">property keyUsage</a>
</h3>

```typescript
keyUsage?: pulumi.Input<string>;
```


Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L174">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid policy JSON document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the object.

<h2 class="pdoc-module-header" id="KeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L102">interface KeyState</a>
</h2>

Input properties used for looking up and filtering Key resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L106">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L111">property deletionWindowInDays</a>
</h3>

```typescript
deletionWindowInDays?: pulumi.Input<number>;
```


Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L115">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the key as viewed in AWS console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L120">property enableKeyRotation</a>
</h3>

```typescript
enableKeyRotation?: pulumi.Input<boolean>;
```


Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
is enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L124">property isEnabled</a>
</h3>

```typescript
isEnabled?: pulumi.Input<boolean>;
```


Specifies whether the key is enabled. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L128">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The globally unique identifier for the key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L133">property keyUsage</a>
</h3>

```typescript
keyUsage?: pulumi.Input<string>;
```


Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L137">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid policy JSON document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kms/key.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the object.

