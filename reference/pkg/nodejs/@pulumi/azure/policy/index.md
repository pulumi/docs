---
title: Module policy
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Definition">class Definition</a>
* <a href="#DefinitionArgs">interface DefinitionArgs</a>
* <a href="#DefinitionState">interface DefinitionState</a>

<a href="/policy/definition.ts">policy/definition.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Definition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L9">class Definition</a>
</h2>

Creates a policy for all of the resource groups under the subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L63">constructor</a>
</h3>

```typescript
new Definition(name: string, args: DefinitionArgs, opts?: pulumi.ResourceOptions)
```


Create a Definition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Definition(name: string, state?: DefinitionState, opts?: pulumi.ResourceOptions)
```


Create a Definition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefinitionState): Definition
```


Get an existing Definition resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L29">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L35">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<string | undefined>;
```


The metadata for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L42">property mode</a>
</h3>

```typescript
public mode: pulumi.Output<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L47">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L52">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<string | undefined>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L58">property policyRule</a>
</h3>

```typescript
public policyRule: pulumi.Output<string | undefined>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L63">property policyType</a>
</h3>

```typescript
public policyType: pulumi.Output<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L162">interface DefinitionArgs</a>
</h2>

The set of arguments for constructing a Definition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L166">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L170">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L176">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<string>;
```


The metadata for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L183">property mode</a>
</h3>

```typescript
mode: pulumi.Input<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L193">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L199">property policyRule</a>
</h3>

```typescript
policyRule?: pulumi.Input<string>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L204">property policyType</a>
</h3>

```typescript
policyType: pulumi.Input<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L114">interface DefinitionState</a>
</h2>

Input properties used for looking up and filtering Definition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L122">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L128">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<string>;
```


The metadata for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L135">property mode</a>
</h3>

```typescript
mode?: pulumi.Input<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L145">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L151">property policyRule</a>
</h3>

```typescript
policyRule?: pulumi.Input<string>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/policy/definition.ts#L156">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

