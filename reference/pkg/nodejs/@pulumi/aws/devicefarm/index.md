---
title: Module devicefarm
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Project">class Project</a>
* <a href="#ProjectArgs">interface ProjectArgs</a>
* <a href="#ProjectState">interface ProjectState</a>

<a href="/devicefarm/project.ts">devicefarm/project.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L14">class Project</a>
</h2>

Provides a resource to manage AWS Device Farm Projects.
Please keep in mind that this feature is only supported on the "us-west-2" region.
This resource will error if you try to create a project in another region.

For more information about Device Farm Projects, see the AWS Documentation on
[Device Farm Projects][aws-get-project].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L34">constructor</a>
</h3>

```typescript
new Project(name: string, args?: ProjectArgs, opts?: pulumi.ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L23">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name of this project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L78">interface ProjectArgs</a>
</h2>

The set of arguments for constructing a Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the project

<h2 class="pdoc-module-header" id="ProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L64">interface ProjectState</a>
</h2>

Input properties used for looking up and filtering Project resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L68">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name of this project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/devicefarm/project.ts#L72">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the project

