---
title: Module appmesh
---

<a href="../index.html">@pulumi/aws</a> &gt; appmesh

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Mesh">class Mesh</a>
* <a href="#Route">class Route</a>
* <a href="#VirtualNode">class VirtualNode</a>
* <a href="#VirtualRouter">class VirtualRouter</a>
* <a href="#MeshArgs">interface MeshArgs</a>
* <a href="#MeshState">interface MeshState</a>
* <a href="#RouteArgs">interface RouteArgs</a>
* <a href="#RouteState">interface RouteState</a>
* <a href="#VirtualNodeArgs">interface VirtualNodeArgs</a>
* <a href="#VirtualNodeState">interface VirtualNodeState</a>
* <a href="#VirtualRouterArgs">interface VirtualRouterArgs</a>
* <a href="#VirtualRouterState">interface VirtualRouterState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts">appmesh/mesh.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts">appmesh/route.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts">appmesh/virtualNode.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts">appmesh/virtualRouter.ts</a> 


<h2 class="pdoc-module-header" id="Mesh">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L10">class Mesh</a>
</h2>

Provides an AWS App Mesh service mesh resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L38">constructor</a>
</h3>

```typescript
new Mesh(name: string, args?: MeshArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Mesh resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MeshState, opts?: pulumi.CustomResourceOptions): Mesh
```


Get an existing Mesh resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L34">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L10">class Route</a>
</h2>

Provides an AWS App Mesh route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L47">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState, opts?: pulumi.CustomResourceOptions): Route
```


Get an existing Route resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L34">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L38">property meshName</a>
</h3>

```typescript
public meshName: pulumi.Output<string>;
```


The name of the service mesh in which to create the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L46">property spec</a>
</h3>

```typescript
public spec: pulumi.Output<{ ... }>;
```


The route specification to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L47">property virtualRouterName</a>
</h3>

```typescript
public virtualRouterName: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="VirtualNode">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L10">class VirtualNode</a>
</h2>

Provides an AWS App Mesh virtual node resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L46">constructor</a>
</h3>

```typescript
new VirtualNode(name: string, args: VirtualNodeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNode resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNodeState, opts?: pulumi.CustomResourceOptions): VirtualNode
```


Get an existing VirtualNode resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L34">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L38">property meshName</a>
</h3>

```typescript
public meshName: pulumi.Output<string>;
```


The name of the service mesh in which to create the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L46">property spec</a>
</h3>

```typescript
public spec: pulumi.Output<{ ... }>;
```


The virtual node specification to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VirtualRouter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L10">class VirtualRouter</a>
</h2>

Provides an AWS App Mesh virtual router resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L46">constructor</a>
</h3>

```typescript
new VirtualRouter(name: string, args: VirtualRouterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualRouter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualRouterState, opts?: pulumi.CustomResourceOptions): VirtualRouter
```


Get an existing VirtualRouter resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L34">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L38">property meshName</a>
</h3>

```typescript
public meshName: pulumi.Output<string>;
```


The name of the service mesh in which to create the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L46">property spec</a>
</h3>

```typescript
public spec: pulumi.Output<{ ... }>;
```


The virtual router specification to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MeshArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L92">interface MeshArgs</a>
</h2>

The set of arguments for constructing a Mesh resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the service mesh.

<h2 class="pdoc-module-header" id="MeshState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L70">interface MeshState</a>
</h2>

Input properties used for looking up and filtering Mesh resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L74">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L78">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L82">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the service mesh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/mesh.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the service mesh.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L125">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L129">property meshName</a>
</h3>

```typescript
meshName: pulumi.Input<string>;
```


The name of the service mesh in which to create the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L137">property spec</a>
</h3>

```typescript
spec: pulumi.Input<{ ... }>;
```


The route specification to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L138">property virtualRouterName</a>
</h3>

```typescript
virtualRouterName: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L94">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L98">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L102">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L106">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L110">property meshName</a>
</h3>

```typescript
meshName?: pulumi.Input<string>;
```


The name of the service mesh in which to create the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the route.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L118">property spec</a>
</h3>

```typescript
spec?: pulumi.Input<{ ... }>;
```


The route specification to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/route.ts#L119">property virtualRouterName</a>
</h3>

```typescript
virtualRouterName?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="VirtualNodeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L118">interface VirtualNodeArgs</a>
</h2>

The set of arguments for constructing a VirtualNode resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L122">property meshName</a>
</h3>

```typescript
meshName: pulumi.Input<string>;
```


The name of the service mesh in which to create the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L130">property spec</a>
</h3>

```typescript
spec: pulumi.Input<{ ... }>;
```


The virtual node specification to apply.

<h2 class="pdoc-module-header" id="VirtualNodeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L88">interface VirtualNodeState</a>
</h2>

Input properties used for looking up and filtering VirtualNode resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L92">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L96">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L100">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L104">property meshName</a>
</h3>

```typescript
meshName?: pulumi.Input<string>;
```


The name of the service mesh in which to create the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the virtual node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualNode.ts#L112">property spec</a>
</h3>

```typescript
spec?: pulumi.Input<{ ... }>;
```


The virtual node specification to apply.

<h2 class="pdoc-module-header" id="VirtualRouterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L118">interface VirtualRouterArgs</a>
</h2>

The set of arguments for constructing a VirtualRouter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L122">property meshName</a>
</h3>

```typescript
meshName: pulumi.Input<string>;
```


The name of the service mesh in which to create the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L130">property spec</a>
</h3>

```typescript
spec: pulumi.Input<{ ... }>;
```


The virtual router specification to apply.

<h2 class="pdoc-module-header" id="VirtualRouterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L88">interface VirtualRouterState</a>
</h2>

Input properties used for looking up and filtering VirtualRouter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L92">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L96">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L100">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L104">property meshName</a>
</h3>

```typescript
meshName?: pulumi.Input<string>;
```


The name of the service mesh in which to create the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for the virtual router.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appmesh/virtualRouter.ts#L112">property spec</a>
</h3>

```typescript
spec?: pulumi.Input<{ ... }>;
```


The virtual router specification to apply.

