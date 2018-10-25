---
title: Module role
---

<a href="../index.html">@pulumi/azure</a> &gt; role

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Assignment">class Assignment</a>
* <a href="#Definition">class Definition</a>
* <a href="#getBuiltinRoleDefinition">function getBuiltinRoleDefinition</a>
* <a href="#getRoleDefinition">function getRoleDefinition</a>
* <a href="#AssignmentArgs">interface AssignmentArgs</a>
* <a href="#AssignmentState">interface AssignmentState</a>
* <a href="#DefinitionArgs">interface DefinitionArgs</a>
* <a href="#DefinitionState">interface DefinitionState</a>
* <a href="#GetBuiltinRoleDefinitionArgs">interface GetBuiltinRoleDefinitionArgs</a>
* <a href="#GetBuiltinRoleDefinitionResult">interface GetBuiltinRoleDefinitionResult</a>
* <a href="#GetRoleDefinitionArgs">interface GetRoleDefinitionArgs</a>
* <a href="#GetRoleDefinitionResult">interface GetRoleDefinitionResult</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts">role/assignment.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts">role/definition.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts">role/getBuiltinRoleDefinition.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts">role/getRoleDefinition.ts</a> 


<h2 class="pdoc-module-header" id="Assignment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L10">class Assignment</a>
</h2>

Assigns a given Principal (User or Application) to a given Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L42">constructor</a>
</h3>

```typescript
new Assignment(name: string, args: AssignmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Assignment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L30">property principalId</a>
</h3>

```typescript
public principalId: pulumi.Output<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L34">property roleDefinitionId</a>
</h3>

```typescript
public roleDefinitionId: pulumi.Output<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L38">property roleDefinitionName</a>
</h3>

```typescript
public roleDefinitionName: pulumi.Output<string | undefined>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L42">property scope</a>
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

<h2 class="pdoc-module-header" id="Definition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L10">class Definition</a>
</h2>

Manages a custom Role Definition, used to assign Roles to Users/Principals. See ['Understand role definitions'](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions) in the Azure documentation for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L46">constructor</a>
</h3>

```typescript
new Definition(name: string, args: DefinitionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Definition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L26">property assignableScopes</a>
</h3>

```typescript
public assignableScopes: pulumi.Output<string[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L30">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L38">property permissions</a>
</h3>

```typescript
public permissions: pulumi.Output<{ ... }[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L42">property roleDefinitionId</a>
</h3>

```typescript
public roleDefinitionId: pulumi.Output<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L46">property scope</a>
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

<h2 class="pdoc-module-header" id="getBuiltinRoleDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L10">function getBuiltinRoleDefinition</a>
</h2>

```typescript
getBuiltinRoleDefinition(args: GetBuiltinRoleDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetBuiltinRoleDefinitionResult>
```


Use this data source to access information about a built-in Role Definition. To access information about a custom Role Definition, please see the `azurerm_role_definition` data source instead.

<h2 class="pdoc-module-header" id="getRoleDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L10">function getRoleDefinition</a>
</h2>

```typescript
getRoleDefinition(args: GetRoleDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleDefinitionResult>
```


Use this data source to access information about an existing Custom Role Definition. To access information about a built-in Role Definition, please see the `azurerm_builtin_role_definition` data source instead.

<h2 class="pdoc-module-header" id="AssignmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L108">interface AssignmentArgs</a>
</h2>

The set of arguments for constructing a Assignment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L116">property principalId</a>
</h3>

```typescript
principalId: pulumi.Input<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L120">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L124">property roleDefinitionName</a>
</h3>

```typescript
roleDefinitionName?: pulumi.Input<string>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L128">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AssignmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L82">interface AssignmentState</a>
</h2>

Input properties used for looking up and filtering Assignment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L90">property principalId</a>
</h3>

```typescript
principalId?: pulumi.Input<string>;
```


The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L94">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L98">property roleDefinitionName</a>
</h3>

```typescript
roleDefinitionName?: pulumi.Input<string>;
```


The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/assignment.ts#L102">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L121">interface DefinitionArgs</a>
</h2>

The set of arguments for constructing a Definition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L125">property assignableScopes</a>
</h3>

```typescript
assignableScopes: pulumi.Input<pulumi.Input<string>[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L129">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the Role Definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L137">property permissions</a>
</h3>

```typescript
permissions: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L141">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L145">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L91">interface DefinitionState</a>
</h2>

Input properties used for looking up and filtering Definition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L95">property assignableScopes</a>
</h3>

```typescript
assignableScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the Role Definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Role Definition. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L107">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L111">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId?: pulumi.Input<string>;
```


A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/definition.ts#L115">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetBuiltinRoleDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L19">interface GetBuiltinRoleDefinitionArgs</a>
</h2>

A collection of arguments for invoking getBuiltinRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the built-in Role Definition. Possible values are: `Contributor`, `Owner`, `Reader` and `VirtualMachineContributor`.

<h2 class="pdoc-module-header" id="GetBuiltinRoleDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L29">interface GetBuiltinRoleDefinitionResult</a>
</h2>

A collection of values returned by getBuiltinRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L33">property assignableScopes</a>
</h3>

```typescript
assignableScopes: string[];
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L37">property description</a>
</h3>

```typescript
description: string;
```


the Description of the built-in Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L49">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L41">property permissions</a>
</h3>

```typescript
permissions: { ... }[];
```


a `permissions` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getBuiltinRoleDefinition.ts#L45">property type</a>
</h3>

```typescript
type: string;
```


the Type of the Role.

<h2 class="pdoc-module-header" id="GetRoleDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L20">interface GetRoleDefinitionArgs</a>
</h2>

A collection of arguments for invoking getRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L24">property roleDefinitionId</a>
</h3>

```typescript
roleDefinitionId: string;
```


Specifies the ID of the Role Definition as a UUID/GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L28">property scope</a>
</h3>

```typescript
scope: string;
```


Specifies the Scope at which the Custom Role Definition exists.

<h2 class="pdoc-module-header" id="GetRoleDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L34">interface GetRoleDefinitionResult</a>
</h2>

A collection of values returned by getRoleDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L38">property assignableScopes</a>
</h3>

```typescript
assignableScopes: string[];
```


One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L42">property description</a>
</h3>

```typescript
description: string;
```


the Description of the built-in Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L55">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L43">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L47">property permissions</a>
</h3>

```typescript
permissions: { ... }[];
```


a `permissions` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/role/getRoleDefinition.ts#L51">property type</a>
</h3>

```typescript
type: string;
```


the Type of the Role.

