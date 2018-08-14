---
title: Module relay
---

<a href="../index.html">@pulumi/azure</a> &gt; relay

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Namespace">class Namespace</a>
* <a href="#NamespaceArgs">interface NamespaceArgs</a>
* <a href="#NamespaceState">interface NamespaceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts">relay/namespace.ts</a> 


<h2 class="pdoc-module-header" id="Namespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L9">class Namespace</a>
</h2>

Manages an Azure Relay Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L61">constructor</a>
</h3>

```typescript
new Namespace(name: string, args: NamespaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Namespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceState): Namespace
```


Get an existing Namespace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L29">property metricId</a>
</h3>

```typescript
public metricId: pulumi.Output<string>;
```


The Identifier for Azure Insights metrics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the SKU to use. At this time the only supported value is `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L37">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The primary connection string for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L41">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Azure Relay Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L49">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The secondary connection string for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L53">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L57">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L61">property tags</a>
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

<h2 class="pdoc-module-header" id="NamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L160">interface NamespaceArgs</a>
</h2>

The set of arguments for constructing a Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L164">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SKU to use. At this time the only supported value is `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L172">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Azure Relay Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L176">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L180">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L114">interface NamespaceState</a>
</h2>

Input properties used for looking up and filtering Namespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L118">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L122">property metricId</a>
</h3>

```typescript
metricId?: pulumi.Input<string>;
```


The Identifier for Azure Insights metrics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SKU to use. At this time the only supported value is `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L130">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The primary connection string for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L134">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L138">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Azure Relay Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L142">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The secondary connection string for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L146">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L150">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/relay/namespace.ts#L154">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

