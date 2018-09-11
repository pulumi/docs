---
title: Module resourcemanager
---

<a href="../index.html">@pulumi/gcp</a> &gt; resourcemanager

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Lien">class Lien</a>
* <a href="#LienArgs">interface LienArgs</a>
* <a href="#LienState">interface LienState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts">resourcemanager/lien.ts</a> 


<h2 class="pdoc-module-header" id="Lien">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L7">class Lien</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L25">constructor</a>
</h3>

```typescript
new Lien(name: string, args: LienArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Lien resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LienState): Lien
```


Get an existing Lien resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L20">property createTime</a>
</h3>

```typescript
public createTime: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L21">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L22">property origin</a>
</h3>

```typescript
public origin: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L23">property parent</a>
</h3>

```typescript
public parent: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L24">property reason</a>
</h3>

```typescript
public reason: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L25">property restrictions</a>
</h3>

```typescript
public restrictions: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LienArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L85">interface LienArgs</a>
</h2>

The set of arguments for constructing a Lien resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L86">property origin</a>
</h3>

```typescript
origin: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L87">property parent</a>
</h3>

```typescript
parent: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L88">property reason</a>
</h3>

```typescript
reason: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L89">property restrictions</a>
</h3>

```typescript
restrictions: pulumi.Input<pulumi.Input<string>[]>;
```

<h2 class="pdoc-module-header" id="LienState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L73">interface LienState</a>
</h2>

Input properties used for looking up and filtering Lien resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L74">property createTime</a>
</h3>

```typescript
createTime?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L76">property origin</a>
</h3>

```typescript
origin?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L77">property parent</a>
</h3>

```typescript
parent?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L78">property reason</a>
</h3>

```typescript
reason?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/resourcemanager/lien.ts#L79">property restrictions</a>
</h3>

```typescript
restrictions?: pulumi.Input<pulumi.Input<string>[]>;
```

