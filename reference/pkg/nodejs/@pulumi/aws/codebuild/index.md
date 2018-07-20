---
title: Module codebuild
---

<a href="../index.html">@pulumi/aws</a> &gt; codebuild

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Project">class Project</a>
* <a href="#Webhook">class Webhook</a>
* <a href="#ProjectArgs">interface ProjectArgs</a>
* <a href="#ProjectState">interface ProjectState</a>
* <a href="#WebhookArgs">interface WebhookArgs</a>
* <a href="#WebhookState">interface WebhookState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts">codebuild/project.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts">codebuild/webhook.ts</a> 


<h2 class="pdoc-module-header" id="Project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L9">class Project</a>
</h2>

Provides a CodeBuild Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L73">constructor</a>
</h3>

```typescript
new Project(name: string, args: ProjectArgs, opts?: pulumi.ResourceOptions)
```


Create a Project resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState): Project
```


Get an existing Project resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L25">property artifacts</a>
</h3>

```typescript
public artifacts: pulumi.Output<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L29">property badgeEnabled</a>
</h3>

```typescript
public badgeEnabled: pulumi.Output<boolean | undefined>;
```


Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L33">property badgeUrl</a>
</h3>

```typescript
public badgeUrl: pulumi.Output<string>;
```


The URL of the build badge when `badge_enabled` is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L37">property buildTimeout</a>
</h3>

```typescript
public buildTimeout: pulumi.Output<number | undefined>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L41">property cache</a>
</h3>

```typescript
public cache: pulumi.Output<{ ... } | undefined>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L49">property encryptionKey</a>
</h3>

```typescript
public encryptionKey: pulumi.Output<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L53">property environment</a>
</h3>

```typescript
public environment: pulumi.Output<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L61">property serviceRole</a>
</h3>

```typescript
public serviceRole: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L65">property source</a>
</h3>

```typescript
public source: pulumi.Output<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L69">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L73">property vpcConfig</a>
</h3>

```typescript
public vpcConfig: pulumi.Output<{ ... } | undefined>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

<h2 class="pdoc-module-header" id="Webhook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L9">class Webhook</a>
</h2>

Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L41">constructor</a>
</h3>

```typescript
new Webhook(name: string, args: WebhookArgs, opts?: pulumi.ResourceOptions)
```


Create a Webhook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebhookState): Webhook
```


Get an existing Webhook resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L25">property branchFilter</a>
</h3>

```typescript
public branchFilter: pulumi.Output<string | undefined>;
```


A regular expression used to determine which branches get built. Default is all branches are built.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L29">property payloadUrl</a>
</h3>

```typescript
public payloadUrl: pulumi.Output<string>;
```


The CodeBuild endpoint where webhook events are sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L33">property projectName</a>
</h3>

```typescript
public projectName: pulumi.Output<string>;
```


The name of the build project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L37">property secret</a>
</h3>

```typescript
public secret: pulumi.Output<string>;
```


The secret token of the associated repository. Not returned by the CodeBuild API for all source types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L41">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL to the webhook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L190">interface ProjectArgs</a>
</h2>

The set of arguments for constructing a Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L194">property artifacts</a>
</h3>

```typescript
artifacts: pulumi.Input<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L198">property badgeEnabled</a>
</h3>

```typescript
badgeEnabled?: pulumi.Input<boolean>;
```


Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L202">property buildTimeout</a>
</h3>

```typescript
buildTimeout?: pulumi.Input<number>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L206">property cache</a>
</h3>

```typescript
cache?: pulumi.Input<{ ... }>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L210">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L214">property encryptionKey</a>
</h3>

```typescript
encryptionKey?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L218">property environment</a>
</h3>

```typescript
environment: pulumi.Input<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L222">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L226">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L230">property source</a>
</h3>

```typescript
source: pulumi.Input<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L234">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L238">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

<h2 class="pdoc-module-header" id="ProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L132">interface ProjectState</a>
</h2>

Input properties used for looking up and filtering Project resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L136">property artifacts</a>
</h3>

```typescript
artifacts?: pulumi.Input<{ ... }>;
```


Information about the project's build output artifacts. Artifact blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L140">property badgeEnabled</a>
</h3>

```typescript
badgeEnabled?: pulumi.Input<boolean>;
```


Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L144">property badgeUrl</a>
</h3>

```typescript
badgeUrl?: pulumi.Input<string>;
```


The URL of the build badge when `badge_enabled` is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L148">property buildTimeout</a>
</h3>

```typescript
buildTimeout?: pulumi.Input<number>;
```


How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L152">property cache</a>
</h3>

```typescript
cache?: pulumi.Input<{ ... }>;
```


Information about the cache storage for the project. Cache blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L156">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A short description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L160">property encryptionKey</a>
</h3>

```typescript
encryptionKey?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L164">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


Information about the project's build environment. Environment blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The environment variable's name or key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L172">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L176">property source</a>
</h3>

```typescript
source?: pulumi.Input<{ ... }>;
```


Information about the project's input source code. Source blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L180">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/project.ts#L184">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

<h2 class="pdoc-module-header" id="WebhookArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L104">interface WebhookArgs</a>
</h2>

The set of arguments for constructing a Webhook resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L108">property branchFilter</a>
</h3>

```typescript
branchFilter?: pulumi.Input<string>;
```


A regular expression used to determine which branches get built. Default is all branches are built.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L112">property projectName</a>
</h3>

```typescript
projectName: pulumi.Input<string>;
```


The name of the build project.

<h2 class="pdoc-module-header" id="WebhookState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L78">interface WebhookState</a>
</h2>

Input properties used for looking up and filtering Webhook resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L82">property branchFilter</a>
</h3>

```typescript
branchFilter?: pulumi.Input<string>;
```


A regular expression used to determine which branches get built. Default is all branches are built.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L86">property payloadUrl</a>
</h3>

```typescript
payloadUrl?: pulumi.Input<string>;
```


The CodeBuild endpoint where webhook events are sent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L90">property projectName</a>
</h3>

```typescript
projectName?: pulumi.Input<string>;
```


The name of the build project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L94">property secret</a>
</h3>

```typescript
secret?: pulumi.Input<string>;
```


The secret token of the associated repository. Not returned by the CodeBuild API for all source types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codebuild/webhook.ts#L98">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL to the webhook.

