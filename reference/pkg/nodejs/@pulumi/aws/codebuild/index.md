---
title: Module codebuild
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Project">class Project</a>
* <a href="#ProjectArgs">interface ProjectArgs</a>
* <a href="#ProjectState">interface ProjectState</a>

<a href="/codebuild/project.ts">codebuild/project.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L9">class Project</a>
</h2>

Provides a CodeBuild Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L65">constructor</a>
</h3>

```typescript
new Project(name: string, args: ProjectArgs, opts?: pulumi.ResourceOptions)
```


Create a Project resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Project(name: string, state?: ProjectState, opts?: pulumi.ResourceOptions)
```


Create a Project resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState): Project
```


Get an existing Project resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L25">property artifacts</a>
</h3>

```typescript
public artifacts: pulumi.Output<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L29">property buildTimeout</a>
</h3>

```typescript
public buildTimeout: pulumi.Output<number | undefined>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L33">property cache</a>
</h3>

```typescript
public cache: pulumi.Output<{ ... } | undefined>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L41">property encryptionKey</a>
</h3>

```typescript
public encryptionKey: pulumi.Output<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L45">property environment</a>
</h3>

```typescript
public environment: pulumi.Output<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L53">property serviceRole</a>
</h3>

```typescript
public serviceRole: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L57">property source</a>
</h3>

```typescript
public source: pulumi.Output<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L61">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L65">property vpcConfig</a>
</h3>

```typescript
public vpcConfig: pulumi.Output<{ ... } | undefined>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

<h2 class="pdoc-module-header" id="ProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L172">interface ProjectArgs</a>
</h2>

The set of arguments for constructing a Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L176">property artifacts</a>
</h3>

```typescript
artifacts: pulumi.Input<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L180">property buildTimeout</a>
</h3>

```typescript
buildTimeout?: pulumi.Input<number>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L184">property cache</a>
</h3>

```typescript
cache?: pulumi.Input<{ ... }>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L188">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L192">property encryptionKey</a>
</h3>

```typescript
encryptionKey?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L196">property environment</a>
</h3>

```typescript
environment: pulumi.Input<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L200">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L204">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L208">property source</a>
</h3>

```typescript
source: pulumi.Input<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L212">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L216">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

<h2 class="pdoc-module-header" id="ProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L122">interface ProjectState</a>
</h2>

Input properties used for looking up and filtering Project resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L126">property artifacts</a>
</h3>

```typescript
artifacts?: pulumi.Input<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L130">property buildTimeout</a>
</h3>

```typescript
buildTimeout?: pulumi.Input<number>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L134">property cache</a>
</h3>

```typescript
cache?: pulumi.Input<{ ... }>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L138">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L142">property encryptionKey</a>
</h3>

```typescript
encryptionKey?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L146">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L154">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L158">property source</a>
</h3>

```typescript
source?: pulumi.Input<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L162">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/codebuild/project.ts#L166">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

