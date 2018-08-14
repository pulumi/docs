---
title: Module role
---

<a href="../index.html">@pulumi/azure</a> &gt; role

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Definition">class Definition</a>
* <a href="#assignment">class assignment</a>
* <a href="#getBuiltinRoleDefinition">function getBuiltinRoleDefinition</a>
* <a href="#getRoleDefinition">function getRoleDefinition</a>
* <a href="#DefinitionArgs">interface DefinitionArgs</a>
* <a href="#DefinitionState">interface DefinitionState</a>
* <a href="#GetBuiltinRoleDefinitionArgs">interface GetBuiltinRoleDefinitionArgs</a>
* <a href="#GetBuiltinRoleDefinitionResult">interface GetBuiltinRoleDefinitionResult</a>
* <a href="#GetRoleDefinitionArgs">interface GetRoleDefinitionArgs</a>
* <a href="#GetRoleDefinitionResult">interface GetRoleDefinitionResult</a>
* <a href="#assignmentArgs">interface assignmentArgs</a>
* <a href="#assignmentState">interface assignmentState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts">role/assignment.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts">role/definition.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts">role/getBuiltinRoleDefinition.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts">role/getRoleDefinition.ts</a> 


<h2 class="pdoc-module-header" id="Definition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L9">class Definition</a>
</h2>

Manages a custom Role Definition, used to assign Roles to Users/Principals.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L45">constructor</a>
</h3>

```typescript
new Definition(name: string, args: DefinitionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Definition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L25">property assignableScopes</a>
</h3>

```typescript
public assignableScopes: pulumi.Output<string[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the Role Definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L37">property permissions</a>
</h3>

```typescript
public permissions: pulumi.Output<{ ... }[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L41">property roleDefinitionId</a>
</h3>

```typescript
public roleDefinitionId: pulumi.Output<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L45">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```


The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="assignment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L9">class assignment</a>
</h2>

Assigns a given Principal (User or Application) to a given Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L41">constructor</a>
</h3>

```typescript
new assignment(name: string, args: assignmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a assignment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: assignmentState): assignment
```


Get an existing assignment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L29">property principalId</a>
</h3>

```typescript
public principalId: pulumi.Output<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L33">property roleDefinitionId</a>
</h3>

```typescript
public roleDefinitionId: pulumi.Output<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L37">property roleDefinitionName</a>
</h3>

```typescript
public roleDefinitionName: pulumi.Output<string | undefined>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L41">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```


The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getBuiltinRoleDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L9">function getBuiltinRoleDefinition</a>
</h2>

```typescript
getBuiltinRoleDefinition(args: GetBuiltinRoleDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetBuiltinRoleDefinitionResult>
```


Use this data source to access the properties of a built-in Role Definition. To access information about a custom Role Definition, [please see the `azurerm_role_definition` data source](role_definition.html) instead.

<h2 class="pdoc-module-header" id="getRoleDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L9">function getRoleDefinition</a>
</h2>

```typescript
getRoleDefinition(args: GetRoleDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleDefinitionResult>
```


Use this data source to access the properties of a custom Role Definition. To access information about a built-in Role Definition, [please see the `azurerm_builtin_role_definition` data source](builtin_role_definition.html) instead.

<h2 class="pdoc-module-header" id="DefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L120">interface DefinitionArgs</a>
</h2>

The set of arguments for constructing a Definition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L124">property assignableScopes</a>
</h3>

```typescript
assignableScopes: pulumi.Input<pulumi.Input<string>[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L128">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the Role Definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L136">property permissions</a>
</h3>

```typescript
permissions: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L140">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L144">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L90">interface DefinitionState</a>
</h2>

Input properties used for looking up and filtering Definition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L94">property assignableScopes</a>
</h3>

```typescript
assignableScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the Role Definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L106">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L110">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L114">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetBuiltinRoleDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L18">interface GetBuiltinRoleDefinitionArgs</a>
</h2>

A collection of arguments for invoking getBuiltinRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L22">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the built-in Role Definition. Possible values are: `Contributor`, `Owner`, `Reader` and `VirtualMachineContributor`.

<h2 class="pdoc-module-header" id="GetBuiltinRoleDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L28">interface GetBuiltinRoleDefinitionResult</a>
</h2>

A collection of values returned by getBuiltinRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L32">property assignableScopes</a>
</h3>

```typescript
assignableScopes: string[];
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L36">property description</a>
</h3>

```typescript
description: string;
```


the Description of the built-in Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L48">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L40">property permissions</a>
</h3>

```typescript
permissions: { ... }[];
```


a `permissions` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L44">property type</a>
</h3>

```typescript
type: string;
```


the Type of the Role.

<h2 class="pdoc-module-header" id="GetRoleDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L19">interface GetRoleDefinitionArgs</a>
</h2>

A collection of arguments for invoking getRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L23">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId: string;
```


Specifies the ID of the Role Definition as a UUID/GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L27">property scope</a>
</h3>

```typescript
scope: string;
```


Specifies the Scope at which the Custom Role Definition exists.

<h2 class="pdoc-module-header" id="GetRoleDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L33">interface GetRoleDefinitionResult</a>
</h2>

A collection of values returned by getRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L37">property assignableScopes</a>
</h3>

```typescript
assignableScopes: string[];
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L41">property description</a>
</h3>

```typescript
description: string;
```


the Description of the built-in Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L42">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L46">property permissions</a>
</h3>

```typescript
permissions: { ... }[];
```


a `permissions` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L50">property type</a>
</h3>

```typescript
type: string;
```


the Type of the Role.

<h2 class="pdoc-module-header" id="assignmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L107">interface assignmentArgs</a>
</h2>

The set of arguments for constructing a assignment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L115">property principalId</a>
</h3>

```typescript
principalId: pulumi.Input<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L119">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L123">property roleDefinitionName</a>
</h3>

```typescript
roleDefinitionName?: pulumi.Input<string>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L127">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="assignmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L81">interface assignmentState</a>
</h2>

Input properties used for looking up and filtering assignment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L89">property principalId</a>
</h3>

```typescript
principalId?: pulumi.Input<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L93">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L97">property roleDefinitionName</a>
</h3>

```typescript
roleDefinitionName?: pulumi.Input<string>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L101">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

