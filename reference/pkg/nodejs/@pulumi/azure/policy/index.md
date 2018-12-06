---
title: Module policy
---

<a href="../index.html">@pulumi/azure</a> &gt; policy

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Assignment">class Assignment</a>
* <a href="#Definition">class Definition</a>
* <a href="#AssignmentArgs">interface AssignmentArgs</a>
* <a href="#AssignmentState">interface AssignmentState</a>
* <a href="#DefinitionArgs">interface DefinitionArgs</a>
* <a href="#DefinitionState">interface DefinitionState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts">policy/assignment.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts">policy/definition.ts</a> 


<h2 class="pdoc-module-header" id="Assignment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L10">class Assignment</a>
</h2>

Configures the specified Policy Definition at the specified Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L43">constructor</a>
</h3>

```typescript
new Assignment(name: string, args: AssignmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Assignment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AssignmentState): Assignment
```


Get an existing Assignment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L30">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string | undefined>;
```


A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L38">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<string | undefined>;
```


Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L42">property policyDefinitionId</a>
</h3>

```typescript
public policyDefinitionId: pulumi.Output<string>;
```


The ID of the Policy Definition to be applied at the specified Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L43">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Definition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L10">class Definition</a>
</h2>

Manages a policy rule definition. Policy definitions do not take effect until they are assigned to a scope using a Policy Assignment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L64">constructor</a>
</h3>

```typescript
new Definition(name: string, args: DefinitionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Definition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefinitionState): Definition
```


Get an existing Definition resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L30">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L36">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<string | undefined>;
```


The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L43">property mode</a>
</h3>

```typescript
public mode: pulumi.Output<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L53">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<string | undefined>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L59">property policyRule</a>
</h3>

```typescript
public policyRule: pulumi.Output<string | undefined>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L64">property policyType</a>
</h3>

```typescript
public policyType: pulumi.Output<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AssignmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L112">interface AssignmentArgs</a>
</h2>

The set of arguments for constructing a Assignment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L120">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L128">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L132">property policyDefinitionId</a>
</h3>

```typescript
policyDefinitionId: pulumi.Input<string>;
```


The ID of the Policy Definition to be applied at the specified Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L133">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="AssignmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L85">interface AssignmentState</a>
</h2>

Input properties used for looking up and filtering Assignment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L89">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L93">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Policy Assignment. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L101">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L105">property policyDefinitionId</a>
</h3>

```typescript
policyDefinitionId?: pulumi.Input<string>;
```


The ID of the Policy Definition to be applied at the specified Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/assignment.ts#L106">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="DefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L161">interface DefinitionArgs</a>
</h2>

The set of arguments for constructing a Definition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L165">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L169">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L175">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<string>;
```


The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L182">property mode</a>
</h3>

```typescript
mode: pulumi.Input<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L187">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L192">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L198">property policyRule</a>
</h3>

```typescript
policyRule?: pulumi.Input<string>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L203">property policyType</a>
</h3>

```typescript
policyType: pulumi.Input<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L113">interface DefinitionState</a>
</h2>

Input properties used for looking up and filtering Definition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L121">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name of the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L127">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<string>;
```


The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L134">property mode</a>
</h3>

```typescript
mode?: pulumi.Input<string>;
```


The policy mode that allows you to specify which resource
types will be evaluated.  The value can be "All", "Indexed" or
"NotSpecified". Changing this resource forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy definition. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L144">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<string>;
```


Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L150">property policyRule</a>
</h3>

```typescript
policyRule?: pulumi.Input<string>;
```


The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/policy/definition.ts#L155">property policyType</a>
</h3>

```typescript
policyType?: pulumi.Input<string>;
```


The policy type.  The value can be "BuiltIn", "Custom"
or "NotSpecified". Changing this forces a new resource to be created.

