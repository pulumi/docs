---
title: Module databricks
---

<a href="../index.html">@pulumi/azure</a> &gt; databricks

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Workspace">class Workspace</a>
* <a href="#WorkspaceArgs">interface WorkspaceArgs</a>
* <a href="#WorkspaceState">interface WorkspaceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts">databricks/workspace.ts</a> 


<h2 class="pdoc-module-header" id="Workspace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L10">class Workspace</a>
</h2>

Manages a Databricks Workspace

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L50">constructor</a>
</h3>

```typescript
new Workspace(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Workspace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceState, opts?: pulumi.CustomResourceOptions): Workspace
```


Get an existing Workspace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L30">property managedResourceGroupId</a>
</h3>

```typescript
public managedResourceGroupId: pulumi.Output<string>;
```


The ID of the Managed Resource Group created by the Databricks Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L34">property managedResourceGroupName</a>
</h3>

```typescript
public managedResourceGroupName: pulumi.Output<string>;
```


The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L46">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


The `sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="WorkspaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L131">interface WorkspaceArgs</a>
</h2>

The set of arguments for constructing a Workspace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L135">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L139">property managedResourceGroupName</a>
</h3>

```typescript
managedResourceGroupName?: pulumi.Input<string>;
```


The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L147">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L151">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


The `sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L155">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="WorkspaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L97">interface WorkspaceState</a>
</h2>

Input properties used for looking up and filtering Workspace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L101">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L105">property managedResourceGroupId</a>
</h3>

```typescript
managedResourceGroupId?: pulumi.Input<string>;
```


The ID of the Managed Resource Group created by the Databricks Workspace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L109">property managedResourceGroupName</a>
</h3>

```typescript
managedResourceGroupName?: pulumi.Input<string>;
```


The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L117">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L121">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The `sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/databricks/workspace.ts#L125">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

