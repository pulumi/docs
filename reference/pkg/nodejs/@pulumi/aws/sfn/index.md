---
title: Module sfn
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Activity">class Activity</a>
* <a href="#StateMachine">class StateMachine</a>
* <a href="#ActivityArgs">interface ActivityArgs</a>
* <a href="#ActivityState">interface ActivityState</a>
* <a href="#StateMachineArgs">interface StateMachineArgs</a>
* <a href="#StateMachineState">interface StateMachineState</a>

<a href="/sfn/activity.ts">sfn/activity.ts</a> <a href="/sfn/stateMachine.ts">sfn/stateMachine.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Activity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L9">class Activity</a>
</h2>

Provides a Step Function Activity resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L29">constructor</a>
</h3>

```typescript
new Activity(name: string, args?: ActivityArgs, opts?: pulumi.ResourceOptions)
```


Create a Activity resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Activity(name: string, state?: ActivityState, opts?: pulumi.ResourceOptions)
```


Create a Activity resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActivityState): Activity
```


Get an existing Activity resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L25">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The date the activity was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the activity to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StateMachine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L9">class StateMachine</a>
</h2>

Provides a Step Function State Machine resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L41">constructor</a>
</h3>

```typescript
new StateMachine(name: string, args: StateMachineArgs, opts?: pulumi.ResourceOptions)
```


Create a StateMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new StateMachine(name: string, state?: StateMachineState, opts?: pulumi.ResourceOptions)
```


Create a StateMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StateMachineState): StateMachine
```


Get an existing StateMachine resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L25">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The date the state machine was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L29">property definition</a>
</h3>

```typescript
public definition: pulumi.Output<string>;
```


The Amazon States Language definition of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L37">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the IAM role to use for this state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L41">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The current status of the state machine. Either "ACTIVE" or "DELETING".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ActivityArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L73">interface ActivityArgs</a>
</h2>

The set of arguments for constructing a Activity resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L77">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the activity to create.

<h2 class="pdoc-module-header" id="ActivityState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L59">interface ActivityState</a>
</h2>

Input properties used for looking up and filtering Activity resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L63">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The date the activity was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/activity.ts#L67">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the activity to create.

<h2 class="pdoc-module-header" id="StateMachineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L109">interface StateMachineArgs</a>
</h2>

The set of arguments for constructing a StateMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L113">property definition</a>
</h3>

```typescript
definition: pulumi.Input<string>;
```


The Amazon States Language definition of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L121">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to use for this state machine.

<h2 class="pdoc-module-header" id="StateMachineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L83">interface StateMachineState</a>
</h2>

Input properties used for looking up and filtering StateMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L87">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The date the state machine was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L91">property definition</a>
</h3>

```typescript
definition?: pulumi.Input<string>;
```


The Amazon States Language definition of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L99">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the IAM role to use for this state machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sfn/stateMachine.ts#L103">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The current status of the state machine. Either "ACTIVE" or "DELETING".

