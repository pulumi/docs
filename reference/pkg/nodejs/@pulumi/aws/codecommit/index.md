---
title: Module codecommit
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Repository">class Repository</a>
* <a href="#Trigger">class Trigger</a>
* <a href="#RepositoryArgs">interface RepositoryArgs</a>
* <a href="#RepositoryState">interface RepositoryState</a>
* <a href="#TriggerArgs">interface TriggerArgs</a>
* <a href="#TriggerState">interface TriggerState</a>

<a href="/codecommit/repository.ts">codecommit/repository.ts</a> <a href="/codecommit/trigger.ts">codecommit/trigger.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Repository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L13">class Repository</a>
</h2>

Provides a CodeCommit Repository Resource.

~> **NOTE on CodeCommit Availability**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L53">constructor</a>
</h3>

```typescript
new Repository(name: string, args: RepositoryArgs, opts?: pulumi.ResourceOptions)
```


Create a Repository resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Repository(name: string, state?: RepositoryState, opts?: pulumi.ResourceOptions)
```


Create a Repository resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryState): Repository
```


Get an existing Repository resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L33">property cloneUrlHttp</a>
</h3>

```typescript
public cloneUrlHttp: pulumi.Output<string>;
```


The URL to use for cloning the repository over HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L37">property cloneUrlSsh</a>
</h3>

```typescript
public cloneUrlSsh: pulumi.Output<string>;
```


The URL to use for cloning the repository over SSH.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L41">property defaultBranch</a>
</h3>

```typescript
public defaultBranch: pulumi.Output<string | undefined>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L49">property repositoryId</a>
</h3>

```typescript
public repositoryId: pulumi.Output<string>;
```


The ID of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L53">property repositoryName</a>
</h3>

```typescript
public repositoryName: pulumi.Output<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Trigger">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L13">class Trigger</a>
</h2>

Provides a CodeCommit Trigger Resource.

~> **NOTE on CodeCommit**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L31">constructor</a>
</h3>

```typescript
new Trigger(name: string, args: TriggerArgs, opts?: pulumi.ResourceOptions)
```


Create a Trigger resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Trigger(name: string, state?: TriggerState, opts?: pulumi.ResourceOptions)
```


Create a Trigger resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerState): Trigger
```


Get an existing Trigger resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L26">property configurationId</a>
</h3>

```typescript
public configurationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L30">property repositoryName</a>
</h3>

```typescript
public repositoryName: pulumi.Output<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L31">property triggers</a>
</h3>

```typescript
public triggers: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L130">interface RepositoryArgs</a>
</h2>

The set of arguments for constructing a Repository resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L134">property defaultBranch</a>
</h3>

```typescript
defaultBranch?: pulumi.Input<string>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L138">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L142">property repositoryName</a>
</h3>

```typescript
repositoryName: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h2 class="pdoc-module-header" id="RepositoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L96">interface RepositoryState</a>
</h2>

Input properties used for looking up and filtering Repository resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L100">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L104">property cloneUrlHttp</a>
</h3>

```typescript
cloneUrlHttp?: pulumi.Input<string>;
```


The URL to use for cloning the repository over HTTPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L108">property cloneUrlSsh</a>
</h3>

```typescript
cloneUrlSsh?: pulumi.Input<string>;
```


The URL to use for cloning the repository over SSH.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L112">property defaultBranch</a>
</h3>

```typescript
defaultBranch?: pulumi.Input<string>;
```


The default branch of the repository. The branch specified here needs to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the repository. This needs to be less than 1000 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L120">property repositoryId</a>
</h3>

```typescript
repositoryId?: pulumi.Input<string>;
```


The ID of the repository

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/repository.ts#L124">property repositoryName</a>
</h3>

```typescript
repositoryName?: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h2 class="pdoc-module-header" id="TriggerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L81">interface TriggerArgs</a>
</h2>

The set of arguments for constructing a Trigger resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L85">property repositoryName</a>
</h3>

```typescript
repositoryName: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L86">property triggers</a>
</h3>

```typescript
triggers: pulumi.Input<{ ... }[]>;
```

<h2 class="pdoc-module-header" id="TriggerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L69">interface TriggerState</a>
</h2>

Input properties used for looking up and filtering Trigger resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L70">property configurationId</a>
</h3>

```typescript
configurationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L74">property repositoryName</a>
</h3>

```typescript
repositoryName?: pulumi.Input<string>;
```


The name for the repository. This needs to be less than 100 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codecommit/trigger.ts#L75">property triggers</a>
</h3>

```typescript
triggers?: pulumi.Input<{ ... }[]>;
```

