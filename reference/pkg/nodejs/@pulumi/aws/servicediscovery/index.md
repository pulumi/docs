---
title: Module servicediscovery
---

<a href="../index.html">@pulumi/aws</a> &gt; servicediscovery

<h2 class="pdoc-module-header">Index</h2>

* <a href="#PrivateDnsNamespace">class PrivateDnsNamespace</a>
* <a href="#PublicDnsNamespace">class PublicDnsNamespace</a>
* <a href="#Service">class Service</a>
* <a href="#PrivateDnsNamespaceArgs">interface PrivateDnsNamespaceArgs</a>
* <a href="#PrivateDnsNamespaceState">interface PrivateDnsNamespaceState</a>
* <a href="#PublicDnsNamespaceArgs">interface PublicDnsNamespaceArgs</a>
* <a href="#PublicDnsNamespaceState">interface PublicDnsNamespaceState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts">servicediscovery/privateDnsNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts">servicediscovery/publicDnsNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts">servicediscovery/service.ts</a> 


<h2 class="pdoc-module-header" id="PrivateDnsNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L9">class PrivateDnsNamespace</a>
</h2>

Provides a Service Discovery Private DNS Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L41">constructor</a>
</h3>

```typescript
new PrivateDnsNamespace(name: string, args: PrivateDnsNamespaceArgs, opts?: pulumi.ResourceOptions)
```


Create a PrivateDnsNamespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PrivateDnsNamespaceState): PrivateDnsNamespace
```


Get an existing PrivateDnsNamespace resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN that Amazon Route 53 assigns to the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L33">property hostedZone</a>
</h3>

```typescript
public hostedZone: pulumi.Output<string>;
```


The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L41">property vpc</a>
</h3>

```typescript
public vpc: pulumi.Output<string>;
```


The ID of VPC that you want to associate the namespace with.

<h2 class="pdoc-module-header" id="PublicDnsNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L9">class PublicDnsNamespace</a>
</h2>

Provides a Service Discovery Public DNS Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L37">constructor</a>
</h3>

```typescript
new PublicDnsNamespace(name: string, args?: PublicDnsNamespaceArgs, opts?: pulumi.ResourceOptions)
```


Create a PublicDnsNamespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PublicDnsNamespaceState): PublicDnsNamespace
```


Get an existing PublicDnsNamespace resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN that Amazon Route 53 assigns to the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L33">property hostedZone</a>
</h3>

```typescript
public hostedZone: pulumi.Output<string>;
```


The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L9">class Service</a>
</h2>

Provides a Service Discovery Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L45">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L33">property dnsConfig</a>
</h3>

```typescript
public dnsConfig: pulumi.Output<{ ... }>;
```


A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L37">property healthCheckConfig</a>
</h3>

```typescript
public healthCheckConfig: pulumi.Output<{ ... } | undefined>;
```


A complex type that contains settings for an optional health check. Only for Public DNS namespaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L41">property healthCheckCustomConfig</a>
</h3>

```typescript
public healthCheckCustomConfig: pulumi.Output<{ ... } | undefined>;
```


A complex type that contains settings for ECS managed health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PrivateDnsNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L104">interface PrivateDnsNamespaceArgs</a>
</h2>

The set of arguments for constructing a PrivateDnsNamespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L108">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L116">property vpc</a>
</h3>

```typescript
vpc: pulumi.Input<string>;
```


The ID of VPC that you want to associate the namespace with.

<h2 class="pdoc-module-header" id="PrivateDnsNamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L78">interface PrivateDnsNamespaceState</a>
</h2>

Input properties used for looking up and filtering PrivateDnsNamespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L82">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN that Amazon Route 53 assigns to the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L86">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L90">property hostedZone</a>
</h3>

```typescript
hostedZone?: pulumi.Input<string>;
```


The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/privateDnsNamespace.ts#L98">property vpc</a>
</h3>

```typescript
vpc?: pulumi.Input<string>;
```


The ID of VPC that you want to associate the namespace with.

<h2 class="pdoc-module-header" id="PublicDnsNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L91">interface PublicDnsNamespaceArgs</a>
</h2>

The set of arguments for constructing a PublicDnsNamespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the namespace.

<h2 class="pdoc-module-header" id="PublicDnsNamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L69">interface PublicDnsNamespaceState</a>
</h2>

Input properties used for looking up and filtering PublicDnsNamespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L73">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN that Amazon Route 53 assigns to the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L77">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description that you specify for the namespace when you create it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L81">property hostedZone</a>
</h3>

```typescript
hostedZone?: pulumi.Input<string>;
```


The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/publicDnsNamespace.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the namespace.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L114">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L122">property dnsConfig</a>
</h3>

```typescript
dnsConfig: pulumi.Input<{ ... }>;
```


A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L126">property healthCheckConfig</a>
</h3>

```typescript
healthCheckConfig?: pulumi.Input<{ ... }>;
```


A complex type that contains settings for an optional health check. Only for Public DNS namespaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L130">property healthCheckCustomConfig</a>
</h3>

```typescript
healthCheckCustomConfig?: pulumi.Input<{ ... }>;
```


A complex type that contains settings for ECS managed health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L84">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L88">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L96">property dnsConfig</a>
</h3>

```typescript
dnsConfig?: pulumi.Input<{ ... }>;
```


A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L100">property healthCheckConfig</a>
</h3>

```typescript
healthCheckConfig?: pulumi.Input<{ ... }>;
```


A complex type that contains settings for an optional health check. Only for Public DNS namespaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L104">property healthCheckCustomConfig</a>
</h3>

```typescript
healthCheckCustomConfig?: pulumi.Input<{ ... }>;
```


A complex type that contains settings for ECS managed health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicediscovery/service.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service.

