---
title: Module codecommit
---

<a href="../index.html">@pulumi/aws</a> &gt; codecommit

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Repository">class Repository</a>
* <a href="#Trigger">class Trigger</a>
* <a href="#getRepository">function getRepository</a>
* <a href="#GetRepositoryArgs">interface GetRepositoryArgs</a>
* <a href="#GetRepositoryResult">interface GetRepositoryResult</a>
* <a href="#RepositoryArgs">interface RepositoryArgs</a>
* <a href="#RepositoryState">interface RepositoryState</a>
* <a href="#TriggerArgs">interface TriggerArgs</a>
* <a href="#TriggerState">interface TriggerState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts">codecommit/getRepository.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts">codecommit/repository.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts">codecommit/trigger.ts</a> 


<h2 class="pdoc-module-header" id="Repository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L14">class Repository</a>
</h2>

Provides a CodeCommit Repository Resource.

~> **NOTE on CodeCommit Availability**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L54">constructor</a>
</h3>

```typescript
new Repository(name: string, args: RepositoryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Repository resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryState): Repository
```


Get an existing Repository resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L34">property cloneUrlHttp</a>
</h3>

```typescript
public cloneUrlHttp: pulumi.Output<string>;
```


The URL to use for cloning the repository over HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L38">property cloneUrlSsh</a>
</h3>

```typescript
public cloneUrlSsh: pulumi.Output<string>;
```


The URL to use for cloning the repository over SSH.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L42">property defaultBranch</a>
</h3>

```typescript
public defaultBranch: pulumi.Output<string | undefined>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L46">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L50">property repositoryId</a>
</h3>

```typescript
public repositoryId: pulumi.Output<string>;
```


The ID of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L54">property repositoryName</a>
</h3>

```typescript
public repositoryName: pulumi.Output<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Trigger">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L14">class Trigger</a>
</h2>

Provides a CodeCommit Trigger Resource.

~> **NOTE on CodeCommit**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L32">constructor</a>
</h3>

```typescript
new Trigger(name: string, args: TriggerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Trigger resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerState): Trigger
```


Get an existing Trigger resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L27">property configurationId</a>
</h3>

```typescript
public configurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L31">property repositoryName</a>
</h3>

```typescript
public repositoryName: pulumi.Output<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L32">property triggers</a>
</h3>

```typescript
public triggers: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getRepository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L10">function getRepository</a>
</h2>

```typescript
getRepository(args: GetRepositoryArgs, opts?: pulumi.InvokeOptions): Promise<GetRepositoryResult>
```


The CodeCommit Repository data source allows the ARN, Repository ID, Repository URL for HTTP and Repository URL for SSH to be retrieved for an CodeCommit repository.

<h2 class="pdoc-module-header" id="GetRepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L19">interface GetRepositoryArgs</a>
</h2>

A collection of arguments for invoking getRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L23">property repositoryName</a>
</h3>

```typescript
repositoryName: string;
```


The name for the repository. This needs to be less than 100 characters.

<h2 class="pdoc-module-header" id="GetRepositoryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L29">interface GetRepositoryResult</a>
</h2>

A collection of values returned by getRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L37">property cloneUrlHttp</a>
</h3>

```typescript
cloneUrlHttp: string;
```


The URL to use for cloning the repository over HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L41">property cloneUrlSsh</a>
</h3>

```typescript
cloneUrlSsh: string;
```


The URL to use for cloning the repository over SSH.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L49">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/getRepository.ts#L45">property repositoryId</a>
</h3>

```typescript
repositoryId: string;
```


The ID of the repository

<h2 class="pdoc-module-header" id="RepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L129">interface RepositoryArgs</a>
</h2>

The set of arguments for constructing a Repository resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L133">property defaultBranch</a>
</h3>

```typescript
defaultBranch?: pulumi.Input<string>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L137">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L141">property repositoryName</a>
</h3>

```typescript
repositoryName: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h2 class="pdoc-module-header" id="RepositoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L95">interface RepositoryState</a>
</h2>

Input properties used for looking up and filtering Repository resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L99">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L103">property cloneUrlHttp</a>
</h3>

```typescript
cloneUrlHttp?: pulumi.Input<string>;
```


The URL to use for cloning the repository over HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L107">property cloneUrlSsh</a>
</h3>

```typescript
cloneUrlSsh?: pulumi.Input<string>;
```


The URL to use for cloning the repository over SSH.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L111">property defaultBranch</a>
</h3>

```typescript
defaultBranch?: pulumi.Input<string>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L115">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L119">property repositoryId</a>
</h3>

```typescript
repositoryId?: pulumi.Input<string>;
```


The ID of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/repository.ts#L123">property repositoryName</a>
</h3>

```typescript
repositoryName?: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h2 class="pdoc-module-header" id="TriggerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L80">interface TriggerArgs</a>
</h2>

The set of arguments for constructing a Trigger resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L84">property repositoryName</a>
</h3>

```typescript
repositoryName: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L85">property triggers</a>
</h3>

```typescript
triggers: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h2 class="pdoc-module-header" id="TriggerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L68">interface TriggerState</a>
</h2>

Input properties used for looking up and filtering Trigger resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L69">property configurationId</a>
</h3>

```typescript
configurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L73">property repositoryName</a>
</h3>

```typescript
repositoryName?: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codecommit/trigger.ts#L74">property triggers</a>
</h3>

```typescript
triggers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

