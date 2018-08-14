---
title: Module mediastore
---

<a href="../index.html">@pulumi/aws</a> &gt; mediastore

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Container">class Container</a>
* <a href="#ContainerPolicy">class ContainerPolicy</a>
* <a href="#ContainerArgs">interface ContainerArgs</a>
* <a href="#ContainerPolicyArgs">interface ContainerPolicyArgs</a>
* <a href="#ContainerPolicyState">interface ContainerPolicyState</a>
* <a href="#ContainerState">interface ContainerState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts">mediastore/container.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts">mediastore/containerPolicy.ts</a> 


<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L9">class Container</a>
</h2>

Provides a MediaStore Container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L33">constructor</a>
</h3>

```typescript
new Container(name: string, args?: ContainerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerState): Container
```


Get an existing Container resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L29">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The DNS endpoint of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the container. Must contain alphanumeric characters or underscores.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ContainerPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L9">class ContainerPolicy</a>
</h2>

Provides a MediaStore Container Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L29">constructor</a>
</h3>

```typescript
new ContainerPolicy(name: string, args: ContainerPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ContainerPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerPolicyState): ContainerPolicy
```


Get an existing ContainerPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L25">property containerName</a>
</h3>

```typescript
public containerName: pulumi.Output<string>;
```


The name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L29">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The contents of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ContainerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L81">interface ContainerArgs</a>
</h2>

The set of arguments for constructing a Container resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the container. Must contain alphanumeric characters or underscores.

<h2 class="pdoc-module-header" id="ContainerPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L77">interface ContainerPolicyArgs</a>
</h2>

The set of arguments for constructing a ContainerPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L81">property containerName</a>
</h3>

```typescript
containerName: pulumi.Input<string>;
```


The name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L85">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The contents of the policy.

<h2 class="pdoc-module-header" id="ContainerPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L63">interface ContainerPolicyState</a>
</h2>

Input properties used for looking up and filtering ContainerPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L67">property containerName</a>
</h3>

```typescript
containerName?: pulumi.Input<string>;
```


The name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/containerPolicy.ts#L71">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The contents of the policy.

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L63">interface ContainerState</a>
</h2>

Input properties used for looking up and filtering Container resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L67">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L71">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The DNS endpoint of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mediastore/container.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the container. Must contain alphanumeric characters or underscores.

