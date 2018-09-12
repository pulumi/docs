---
title: Module managementresource
---

<a href="../index.html">@pulumi/azure</a> &gt; managementresource

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ManangementLock">class ManangementLock</a>
* <a href="#ManangementLockArgs">interface ManangementLockArgs</a>
* <a href="#ManangementLockState">interface ManangementLockState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts">managementresource/manangementLock.ts</a> 


<h2 class="pdoc-module-header" id="ManangementLock">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L10">class ManangementLock</a>
</h2>

Manages a Management Lock which is scoped to a Subscription, Resource Group or Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L35">constructor</a>
</h3>

```typescript
new ManangementLock(name: string, args: ManangementLockArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ManangementLock resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManangementLockState): ManangementLock
```


Get an existing ManangementLock resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L26">property lockLevel</a>
</h3>

```typescript
public lockLevel: pulumi.Output<string>;
```


Specifies the Level to be used for this Lock. Possible values are `CanNotDelete` and `ReadOnly`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Management Lock. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L31">property notes</a>
</h3>

```typescript
public notes: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L35">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```


Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ManangementLockArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L92">interface ManangementLockArgs</a>
</h2>

The set of arguments for constructing a ManangementLock resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L96">property lockLevel</a>
</h3>

```typescript
lockLevel: pulumi.Input<string>;
```


Specifies the Level to be used for this Lock. Possible values are `CanNotDelete` and `ReadOnly`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Management Lock. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L101">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L105">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ManangementLockState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L73">interface ManangementLockState</a>
</h2>

Input properties used for looking up and filtering ManangementLock resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L77">property lockLevel</a>
</h3>

```typescript
lockLevel?: pulumi.Input<string>;
```


Specifies the Level to be used for this Lock. Possible values are `CanNotDelete` and `ReadOnly`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Management Lock. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L82">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementresource/manangementLock.ts#L86">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.

