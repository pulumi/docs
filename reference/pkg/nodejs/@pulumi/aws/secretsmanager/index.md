---
title: Module secretsmanager
---

<a href="../index.html">@pulumi/aws</a> &gt; secretsmanager

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Secret">class Secret</a>
* <a href="#SecretVersion">class SecretVersion</a>
* <a href="#getSecret">function getSecret</a>
* <a href="#getSecretVersion">function getSecretVersion</a>
* <a href="#GetSecretArgs">interface GetSecretArgs</a>
* <a href="#GetSecretResult">interface GetSecretResult</a>
* <a href="#GetSecretVersionArgs">interface GetSecretVersionArgs</a>
* <a href="#GetSecretVersionResult">interface GetSecretVersionResult</a>
* <a href="#SecretArgs">interface SecretArgs</a>
* <a href="#SecretState">interface SecretState</a>
* <a href="#SecretVersionArgs">interface SecretVersionArgs</a>
* <a href="#SecretVersionState">interface SecretVersionState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts">secretsmanager/getSecret.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts">secretsmanager/getSecretVersion.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts">secretsmanager/secret.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts">secretsmanager/secretVersion.ts</a> 


<h2 class="pdoc-module-header" id="Secret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L9">class Secret</a>
</h2>

Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](/docs/providers/aws/r/secretsmanager_secret_version.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L61">constructor</a>
</h3>

```typescript
new Secret(name: string, args?: SecretArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Secret resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState): Secret
```


Get an existing Secret resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L33">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Spaces are not permitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L41">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string | undefined>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L45">property recoveryWindowInDays</a>
</h3>

```typescript
public recoveryWindowInDays: pulumi.Output<number | undefined>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can range from 7 to 30 days. The default value is 30.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L49">property rotationEnabled</a>
</h3>

```typescript
public rotationEnabled: pulumi.Output<boolean>;
```


Specifies whether automatic rotation is enabled for this secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L53">property rotationLambdaArn</a>
</h3>

```typescript
public rotationLambdaArn: pulumi.Output<string | undefined>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L57">property rotationRules</a>
</h3>

```typescript
public rotationRules: pulumi.Output<{ ... } | undefined>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L61">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


Specifies a key-value map of user-defined tags that are attached to the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecretVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L11">class SecretVersion</a>
</h2>

Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the [`aws_secretsmanager_secret` resource](/docs/providers/aws/r/secretsmanager_secret.html).

~> **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from Terraform unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from Terraform to fully trigger version deprecation if necessary.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L39">constructor</a>
</h3>

```typescript
new SecretVersion(name: string, args: SecretVersionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecretVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretVersionState): SecretVersion
```


Get an existing SecretVersion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L27">property secretId</a>
</h3>

```typescript
public secretId: pulumi.Output<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L31">property secretString</a>
</h3>

```typescript
public secretString: pulumi.Output<string>;
```


Specifies text data that you want to encrypt and store in this version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L35">property versionId</a>
</h3>

```typescript
public versionId: pulumi.Output<string>;
```


The unique identifier of the version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L39">property versionStages</a>
</h3>

```typescript
public versionStages: pulumi.Output<string[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

<h2 class="pdoc-module-header" id="getSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L9">function getSecret</a>
</h2>

```typescript
getSecret(args?: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult>
```


Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the [`aws_secretsmanager_secret_version` data source](/docs/providers/aws/d/secretsmanager_secret_version.html).

<h2 class="pdoc-module-header" id="getSecretVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L9">function getSecretVersion</a>
</h2>

```typescript
getSecretVersion(args: GetSecretVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretVersionResult>
```


Retrieve information about a Secrets Manager secret version includings its secret value. To retrieve secret metadata, see the [`aws_secretsmanager_secret` data source](/docs/providers/aws/d/secretsmanager_secret.html).

<h2 class="pdoc-module-header" id="GetSecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L20">interface GetSecretArgs</a>
</h2>

A collection of arguments for invoking getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L24">property arn</a>
</h3>

```typescript
arn?: string;
```


The Amazon Resource Name (ARN) of the secret to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L28">property name</a>
</h3>

```typescript
name?: string;
```


The name of the secret to retrieve.

<h2 class="pdoc-module-header" id="GetSecretResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L34">interface GetSecretResult</a>
</h2>

A collection of values returned by getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L38">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L42">property description</a>
</h3>

```typescript
description: string;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L67">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L46">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L47">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L51">property rotationEnabled</a>
</h3>

```typescript
rotationEnabled: boolean;
```


Whether rotation is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L55">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn: string;
```


Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L59">property rotationRules</a>
</h3>

```typescript
rotationRules: { ... }[];
```


Rotation rules if rotation is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L63">property tags</a>
</h3>

```typescript
tags: { ... };
```


Tags of the secret.

<h2 class="pdoc-module-header" id="GetSecretVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L20">interface GetSecretVersionArgs</a>
</h2>

A collection of arguments for invoking getSecretVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L24">property secretId</a>
</h3>

```typescript
secretId: string;
```


Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L28">property versionId</a>
</h3>

```typescript
versionId?: string;
```


Specifies the unique identifier of the version of the secret that you want to retrieve. Overrides `version_stage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L32">property versionStage</a>
</h3>

```typescript
versionStage?: string;
```


Specifies the secret version that you want to retrieve by the staging label attached to the version. Defaults to `AWSCURRENT`.

<h2 class="pdoc-module-header" id="GetSecretVersionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L38">interface GetSecretVersionResult</a>
</h2>

A collection of values returned by getSecretVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L42">property secretString</a>
</h3>

```typescript
secretString: string;
```


The decrypted part of the protected secret information that was originally provided as a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L46">property versionId</a>
</h3>

```typescript
versionId: string;
```


The unique identifier of this version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L47">property versionStages</a>
</h3>

```typescript
versionStages: string[];
```

<h2 class="pdoc-module-header" id="SecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L151">interface SecretArgs</a>
</h2>

The set of arguments for constructing a Secret resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L155">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L159">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L163">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Spaces are not permitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L167">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L171">property recoveryWindowInDays</a>
</h3>

```typescript
recoveryWindowInDays?: pulumi.Input<number>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can range from 7 to 30 days. The default value is 30.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L175">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn?: pulumi.Input<string>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L179">property rotationRules</a>
</h3>

```typescript
rotationRules?: pulumi.Input<{ ... }>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L183">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Specifies a key-value map of user-defined tags that are attached to the secret.

<h2 class="pdoc-module-header" id="SecretState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L105">interface SecretState</a>
</h2>

Input properties used for looking up and filtering Secret resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L109">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L113">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L117">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Spaces are not permitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L125">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L129">property recoveryWindowInDays</a>
</h3>

```typescript
recoveryWindowInDays?: pulumi.Input<number>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can range from 7 to 30 days. The default value is 30.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L133">property rotationEnabled</a>
</h3>

```typescript
rotationEnabled?: pulumi.Input<boolean>;
```


Specifies whether automatic rotation is enabled for this secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L137">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn?: pulumi.Input<string>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L141">property rotationRules</a>
</h3>

```typescript
rotationRules?: pulumi.Input<{ ... }>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L145">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Specifies a key-value map of user-defined tags that are attached to the secret.

<h2 class="pdoc-module-header" id="SecretVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L99">interface SecretVersionArgs</a>
</h2>

The set of arguments for constructing a SecretVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L103">property secretId</a>
</h3>

```typescript
secretId: pulumi.Input<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L107">property secretString</a>
</h3>

```typescript
secretString: pulumi.Input<string>;
```


Specifies text data that you want to encrypt and store in this version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L111">property versionStages</a>
</h3>

```typescript
versionStages?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

<h2 class="pdoc-module-header" id="SecretVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L77">interface SecretVersionState</a>
</h2>

Input properties used for looking up and filtering SecretVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L81">property secretId</a>
</h3>

```typescript
secretId?: pulumi.Input<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L85">property secretString</a>
</h3>

```typescript
secretString?: pulumi.Input<string>;
```


Specifies text data that you want to encrypt and store in this version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L89">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


The unique identifier of the version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L93">property versionStages</a>
</h3>

```typescript
versionStages?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

