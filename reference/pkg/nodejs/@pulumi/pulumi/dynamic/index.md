---
title: Module dynamic
---

<a href="../index.html">@pulumi/pulumi</a> &gt; dynamic

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Resource">class Resource</a>
* <a href="#CheckFailure">interface CheckFailure</a>
* <a href="#CheckResult">interface CheckResult</a>
* <a href="#CreateResult">interface CreateResult</a>
* <a href="#DiffResult">interface DiffResult</a>
* <a href="#ReadResult">interface ReadResult</a>
* <a href="#ResourceProvider">interface ResourceProvider</a>
* <a href="#UpdateResult">interface UpdateResult</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts">dynamic/index.ts</a> 


<h2 class="pdoc-module-header" id="Resource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L166">class Resource</a>
</h2>

Resource represents a Pulumi Resource that incorporates an inline implementation of the Resource's CRUD operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L166">constructor</a>
</h3>

```typescript
new Resource(provider: ResourceProvider, name: string, props: resource.Inputs, opts?: resource.CustomResourceOptions)
```


Creates a new dynamic resource.

* `provider` The implementation of the resource&#39;s CRUD operations.
* `name` The name of the resource.
* `props` The arguments to use to populate the new resource. Must not define the reserved
             property &#34;__provider&#34;.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L60">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L205">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L199">property id</a>
</h3>

```typescript
public id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L41">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CheckFailure">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L36">interface CheckFailure</a>
</h2>

CheckFailure represents a single failure in the results of a call to `ResourceProvider.check`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L40">property property</a>
</h3>

```typescript
property: string;
```


The property that failed validation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L45">property reason</a>
</h3>

```typescript
reason: string;
```


The reason that the property failed validation.

<h2 class="pdoc-module-header" id="CheckResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L21">interface CheckResult</a>
</h2>

CheckResult represents the results of a call to `ResourceProvider.check`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L30">property failures</a>
</h3>

```typescript
failures?: CheckFailure[];
```


Any validation failures that occurred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L25">property inputs</a>
</h3>

```typescript
inputs?: any;
```


The inputs to use, if any.

<h2 class="pdoc-module-header" id="CreateResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L77">interface CreateResult</a>
</h2>

CreateResult represents the results of a call to `ResourceProvider.create`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L81">property id</a>
</h3>

```typescript
id: resource.ID;
```


The ID of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L86">property outs</a>
</h3>

```typescript
outs?: any;
```


Any properties that were computed during creation.

<h2 class="pdoc-module-header" id="DiffResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L51">interface DiffResult</a>
</h2>

DiffResult represents the results of a call to `ResourceProvider.diff`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L55">property changes</a>
</h3>

```typescript
changes?: undefined | false | true;
```


If true, this diff detected changes and suggests an update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L71">property deleteBeforeReplace</a>
</h3>

```typescript
deleteBeforeReplace?: undefined | false | true;
```


If true, and a replacement occurs, the resource will first be deleted before being recreated.  This is to
void potential side-by-side issues with the default create before delete behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L60">property replaces</a>
</h3>

```typescript
replaces?: string[];
```


If this update requires a replacement, the set of properties triggering it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L65">property stables</a>
</h3>

```typescript
stables?: string[];
```


An optional list of properties that will not ever change.

<h2 class="pdoc-module-header" id="ReadResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L89">interface ReadResult</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L93">property props</a>
</h3>

```typescript
props?: any;
```


The current property state read from the live environment.

<h2 class="pdoc-module-header" id="ResourceProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L109">interface ResourceProvider</a>
</h2>

ResourceProvider represents an object that provides CRUD operations for a particular type of resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L116">property check</a>
</h3>

```typescript
check?: undefined | { ... };
```


Check validates that the given property bag is valid for a resource of the given type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L133">property create</a>
</h3>

```typescript
create: { ... };
```


Create allocates a new instance of the provided resource and returns its unique ID afterwards.
If this call fails, the resource must not have been created (i.e., it is "transacational").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L156">property delete</a>
</h3>

```typescript
delete?: undefined | { ... };
```


Delete tears down an existing resource with the given ID.  If it fails, the resource is assumed to still exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L125">property diff</a>
</h3>

```typescript
diff?: undefined | { ... };
```


Diff checks what impacts a hypothetical update will have on the resource's properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L139">property read</a>
</h3>

```typescript
read?: undefined | { ... };
```


Reads the current live state associated with a resource.  Enough state must be included in the inputs to uniquely
identify the resource; this is typically just the resource ID, but it may also include some properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L148">property update</a>
</h3>

```typescript
update?: undefined | { ... };
```


Update updates an existing resource with new values.

<h2 class="pdoc-module-header" id="UpdateResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L99">interface UpdateResult</a>
</h2>

UpdateResult represents the results of a call to `ResourceProvider.update`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/dynamic/index.ts#L103">property outs</a>
</h3>

```typescript
outs?: any;
```


Any properties that were computed during updating.

