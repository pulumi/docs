---
title: Module ecr
---

<a href="../index.html">@pulumi/aws</a> &gt; ecr

<h2 class="pdoc-module-header">Index</h2>

* <a href="#LifecyclePolicy">class LifecyclePolicy</a>
* <a href="#Repository">class Repository</a>
* <a href="#RepositoryPolicy">class RepositoryPolicy</a>
* <a href="#getCredentials">function getCredentials</a>
* <a href="#getRepository">function getRepository</a>
* <a href="#GetCredentialsArgs">interface GetCredentialsArgs</a>
* <a href="#GetCredentialsResult">interface GetCredentialsResult</a>
* <a href="#GetRepositoryArgs">interface GetRepositoryArgs</a>
* <a href="#GetRepositoryResult">interface GetRepositoryResult</a>
* <a href="#LifecyclePolicyArgs">interface LifecyclePolicyArgs</a>
* <a href="#LifecyclePolicyState">interface LifecyclePolicyState</a>
* <a href="#RepositoryArgs">interface RepositoryArgs</a>
* <a href="#RepositoryPolicyArgs">interface RepositoryPolicyArgs</a>
* <a href="#RepositoryPolicyState">interface RepositoryPolicyState</a>
* <a href="#RepositoryState">interface RepositoryState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts">ecr/getCredentials.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts">ecr/getRepository.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts">ecr/lifecyclePolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts">ecr/repository.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts">ecr/repositoryPolicy.ts</a> 


<h2 class="pdoc-module-header" id="LifecyclePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L9">class LifecyclePolicy</a>
</h2>

Provides an ECR lifecycle policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L33">constructor</a>
</h3>

```typescript
new LifecyclePolicy(name: string, args: LifecyclePolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a LifecyclePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LifecyclePolicyState): LifecyclePolicy
```


Get an existing LifecyclePolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L25">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L29">property registryId</a>
</h3>

```typescript
public registryId: pulumi.Output<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L33">property repository</a>
</h3>

```typescript
public repository: pulumi.Output<string>;
```


Name of the repository to apply the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Repository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L13">class Repository</a>
</h2>

Provides an EC2 Container Registry Repository.

~> **NOTE on ECR Availability**: The EC2 Container Registry is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#ecr_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L41">constructor</a>
</h3>

```typescript
new Repository(name: string, args?: RepositoryArgs, opts?: pulumi.ResourceOptions)
```


Create a Repository resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryState): Repository
```


Get an existing Repository resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Full ARN of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L37">property registryId</a>
</h3>

```typescript
public registryId: pulumi.Output<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L41">property repositoryUrl</a>
</h3>

```typescript
public repositoryUrl: pulumi.Output<string>;
```


The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RepositoryPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L15">class RepositoryPolicy</a>
</h2>

Provides an ECR repository policy.

Note that currently only one policy may be applied to a repository.

~> **NOTE on ECR Availability**: The EC2 Container Registry is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#ecr_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L39">constructor</a>
</h3>

```typescript
new RepositoryPolicy(name: string, args: RepositoryPolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a RepositoryPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryPolicyState): RepositoryPolicy
```


Get an existing RepositoryPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L31">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L35">property registryId</a>
</h3>

```typescript
public registryId: pulumi.Output<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L39">property repository</a>
</h3>

```typescript
public repository: pulumi.Output<string>;
```


Name of the repository to apply the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getCredentials">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L6">function getCredentials</a>
</h2>

```typescript
getCredentials(args: GetCredentialsArgs): Promise<GetCredentialsResult>
```

<h2 class="pdoc-module-header" id="getRepository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L9">function getRepository</a>
</h2>

```typescript
getRepository(args: GetRepositoryArgs): Promise<GetRepositoryResult>
```


The ECR Repository data source allows the ARN, Repository URI and Registry ID to be retrieved for an ECR repository.

<h2 class="pdoc-module-header" id="GetCredentialsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L15">interface GetCredentialsArgs</a>
</h2>

A collection of arguments for invoking getCredentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L16">property registryId</a>
</h3>

```typescript
registryId: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="GetCredentialsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L22">interface GetCredentialsResult</a>
</h2>

A collection of values returned by getCredentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L23">property authorizationToken</a>
</h3>

```typescript
authorizationToken: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L24">property expiresAt</a>
</h3>

```typescript
expiresAt: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L29">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getCredentials.ts#L25">property proxyEndpoint</a>
</h3>

```typescript
proxyEndpoint: string;
```

<h2 class="pdoc-module-header" id="GetRepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L18">interface GetRepositoryArgs</a>
</h2>

A collection of arguments for invoking getRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L22">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the ECR Repository.

<h2 class="pdoc-module-header" id="GetRepositoryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L28">interface GetRepositoryResult</a>
</h2>

A collection of values returned by getRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L32">property arn</a>
</h3>

```typescript
arn: string;
```


Full ARN of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L44">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L36">property registryId</a>
</h3>

```typescript
registryId: string;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/getRepository.ts#L40">property repositoryUrl</a>
</h3>

```typescript
repositoryUrl: string;
```


The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).

<h2 class="pdoc-module-header" id="LifecyclePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L87">interface LifecyclePolicyArgs</a>
</h2>

The set of arguments for constructing a LifecyclePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L91">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L95">property repository</a>
</h3>

```typescript
repository: pulumi.Input<string>;
```


Name of the repository to apply the policy.

<h2 class="pdoc-module-header" id="LifecyclePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L69">interface LifecyclePolicyState</a>
</h2>

Input properties used for looking up and filtering LifecyclePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L73">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L77">property registryId</a>
</h3>

```typescript
registryId?: pulumi.Input<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/lifecyclePolicy.ts#L81">property repository</a>
</h3>

```typescript
repository?: pulumi.Input<string>;
```


Name of the repository to apply the policy.

<h2 class="pdoc-module-header" id="RepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L95">interface RepositoryArgs</a>
</h2>

The set of arguments for constructing a Repository resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the repository.

<h2 class="pdoc-module-header" id="RepositoryPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L93">interface RepositoryPolicyArgs</a>
</h2>

The set of arguments for constructing a RepositoryPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L97">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L101">property repository</a>
</h3>

```typescript
repository: pulumi.Input<string>;
```


Name of the repository to apply the policy.

<h2 class="pdoc-module-header" id="RepositoryPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L75">interface RepositoryPolicyState</a>
</h2>

Input properties used for looking up and filtering RepositoryPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L79">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L83">property registryId</a>
</h3>

```typescript
registryId?: pulumi.Input<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repositoryPolicy.ts#L87">property repository</a>
</h3>

```typescript
repository?: pulumi.Input<string>;
```


Name of the repository to apply the policy.

<h2 class="pdoc-module-header" id="RepositoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L73">interface RepositoryState</a>
</h2>

Input properties used for looking up and filtering Repository resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Full ARN of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L85">property registryId</a>
</h3>

```typescript
registryId?: pulumi.Input<string>;
```


The registry ID where the repository was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecr/repository.ts#L89">property repositoryUrl</a>
</h3>

```typescript
repositoryUrl?: pulumi.Input<string>;
```


The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`

