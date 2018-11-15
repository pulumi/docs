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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L10">class Secret</a>
</h2>

Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L66">constructor</a>
</h3>

```typescript
new Secret(name: string, args?: SecretArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Secret resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L30">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L34">property kmsKeyId</a>
</h3>

```typescript
public kmsKeyId: pulumi.Output<string | undefined>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L42">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L46">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string | undefined>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L50">property recoveryWindowInDays</a>
</h3>

```typescript
public recoveryWindowInDays: pulumi.Output<number | undefined>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L54">property rotationEnabled</a>
</h3>

```typescript
public rotationEnabled: pulumi.Output<boolean>;
```


Specifies whether automatic rotation is enabled for this secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L58">property rotationLambdaArn</a>
</h3>

```typescript
public rotationLambdaArn: pulumi.Output<string | undefined>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L62">property rotationRules</a>
</h3>

```typescript
public rotationRules: pulumi.Output<{ ... } | undefined>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L66">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L12">class SecretVersion</a>
</h2>

Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the [`aws_secretsmanager_secret` resource](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret.html).

~> **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from Terraform unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from Terraform to fully trigger version deprecation if necessary.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L48">constructor</a>
</h3>

```typescript
new SecretVersion(name: string, args: SecretVersionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecretVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L32">property secretBinary</a>
</h3>

```typescript
public secretBinary: pulumi.Output<string | undefined>;
```


Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L36">property secretId</a>
</h3>

```typescript
public secretId: pulumi.Output<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L40">property secretString</a>
</h3>

```typescript
public secretString: pulumi.Output<string | undefined>;
```


Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L44">property versionId</a>
</h3>

```typescript
public versionId: pulumi.Output<string>;
```


The unique identifier of the version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L48">property versionStages</a>
</h3>

```typescript
public versionStages: pulumi.Output<string[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

<h2 class="pdoc-module-header" id="getSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L10">function getSecret</a>
</h2>

```typescript
getSecret(args?: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult>
```


Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the [`aws_secretsmanager_secret_version` data source](https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version.html).

<h2 class="pdoc-module-header" id="getSecretVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L10">function getSecretVersion</a>
</h2>

```typescript
getSecretVersion(args: GetSecretVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretVersionResult>
```


Retrieve information about a Secrets Manager secret version, including its secret value. To retrieve secret metadata, see the [`aws_secretsmanager_secret` data source](https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret.html).

<h2 class="pdoc-module-header" id="GetSecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L21">interface GetSecretArgs</a>
</h2>

A collection of arguments for invoking getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L25">property arn</a>
</h3>

```typescript
arn?: string;
```


The Amazon Resource Name (ARN) of the secret to retrieve.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L29">property name</a>
</h3>

```typescript
name?: string;
```


The name of the secret to retrieve.

<h2 class="pdoc-module-header" id="GetSecretResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L35">interface GetSecretResult</a>
</h2>

A collection of values returned by getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L39">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L43">property description</a>
</h3>

```typescript
description: string;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L72">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L47">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId: string;
```


The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L48">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L52">property policy</a>
</h3>

```typescript
policy: string;
```


The resource-based policy document that's attached to the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L56">property rotationEnabled</a>
</h3>

```typescript
rotationEnabled: boolean;
```


Whether rotation is enabled or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L60">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn: string;
```


Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L64">property rotationRules</a>
</h3>

```typescript
rotationRules: { ... }[];
```


Rotation rules if rotation is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecret.ts#L68">property tags</a>
</h3>

```typescript
tags: { ... };
```


Tags of the secret.

<h2 class="pdoc-module-header" id="GetSecretVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L21">interface GetSecretVersionArgs</a>
</h2>

A collection of arguments for invoking getSecretVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L25">property secretId</a>
</h3>

```typescript
secretId: string;
```


Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L29">property versionId</a>
</h3>

```typescript
versionId?: string;
```


Specifies the unique identifier of the version of the secret that you want to retrieve. Overrides `version_stage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L33">property versionStage</a>
</h3>

```typescript
versionStage?: string;
```


Specifies the secret version that you want to retrieve by the staging label attached to the version. Defaults to `AWSCURRENT`.

<h2 class="pdoc-module-header" id="GetSecretVersionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L39">interface GetSecretVersionResult</a>
</h2>

A collection of values returned by getSecretVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L43">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L60">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L47">property secretBinary</a>
</h3>

```typescript
secretBinary: string;
```


The decrypted part of the protected secret information that was originally provided as a binary. Base64 encoded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L51">property secretString</a>
</h3>

```typescript
secretString: string;
```


The decrypted part of the protected secret information that was originally provided as a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L55">property versionId</a>
</h3>

```typescript
versionId: string;
```


The unique identifier of this version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/getSecretVersion.ts#L56">property versionStages</a>
</h3>

```typescript
versionStages: string[];
```

<h2 class="pdoc-module-header" id="SecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L162">interface SecretArgs</a>
</h2>

The set of arguments for constructing a Secret resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L166">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L170">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L178">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L182">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L186">property recoveryWindowInDays</a>
</h3>

```typescript
recoveryWindowInDays?: pulumi.Input<number>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L190">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn?: pulumi.Input<string>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L194">property rotationRules</a>
</h3>

```typescript
rotationRules?: pulumi.Input<{ ... }>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L198">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Specifies a key-value map of user-defined tags that are attached to the secret.

<h2 class="pdoc-module-header" id="SecretState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L112">interface SecretState</a>
</h2>

Input properties used for looking up and filtering Secret resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L116">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L120">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L124">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L132">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L136">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L140">property recoveryWindowInDays</a>
</h3>

```typescript
recoveryWindowInDays?: pulumi.Input<number>;
```


Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L144">property rotationEnabled</a>
</h3>

```typescript
rotationEnabled?: pulumi.Input<boolean>;
```


Specifies whether automatic rotation is enabled for this secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L148">property rotationLambdaArn</a>
</h3>

```typescript
rotationLambdaArn?: pulumi.Input<string>;
```


Specifies the ARN of the Lambda function that can rotate the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L152">property rotationRules</a>
</h3>

```typescript
rotationRules?: pulumi.Input<{ ... }>;
```


A structure that defines the rotation configuration for this secret. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secret.ts#L156">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Specifies a key-value map of user-defined tags that are attached to the secret.

<h2 class="pdoc-module-header" id="SecretVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L117">interface SecretVersionArgs</a>
</h2>

The set of arguments for constructing a SecretVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L121">property secretBinary</a>
</h3>

```typescript
secretBinary?: pulumi.Input<string>;
```


Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L125">property secretId</a>
</h3>

```typescript
secretId: pulumi.Input<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L129">property secretString</a>
</h3>

```typescript
secretString?: pulumi.Input<string>;
```


Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L133">property versionStages</a>
</h3>

```typescript
versionStages?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

<h2 class="pdoc-module-header" id="SecretVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L87">interface SecretVersionState</a>
</h2>

Input properties used for looking up and filtering SecretVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L95">property secretBinary</a>
</h3>

```typescript
secretBinary?: pulumi.Input<string>;
```


Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L99">property secretId</a>
</h3>

```typescript
secretId?: pulumi.Input<string>;
```


Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L103">property secretString</a>
</h3>

```typescript
secretString?: pulumi.Input<string>;
```


Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L107">property versionId</a>
</h3>

```typescript
versionId?: pulumi.Input<string>;
```


The unique identifier of the version of the secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/secretsmanager/secretVersion.ts#L111">property versionStages</a>
</h3>

```typescript
versionStages?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

