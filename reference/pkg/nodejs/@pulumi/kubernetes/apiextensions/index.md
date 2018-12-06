---
title: Module apiextensions
---

<a href="../index.html">@pulumi/kubernetes</a> &gt; apiextensions

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CustomResource">class CustomResource</a>
* <a href="#CustomResourceArgs">interface CustomResourceArgs</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts">provider.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="v1beta1">apiextensions/v1beta1</a>

<h2 class="pdoc-module-header" id="CustomResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3321">class CustomResource</a>
</h2>

CustomResource represents an instance of a CustomResourceDefinition (CRD). For example, the
CoreOS Prometheus operator exposes a CRD `monitoring.coreos.com/ServiceMonitor`; to
instantiate this as a Pulumi resource, one could call `new CustomResource`, passing the
`ServiceMonitor` resource definition as an argument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3345">constructor</a>
</h3>

```typescript
new CustomResource(name: string, args: CustomResourceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomResource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3344">method getInputs</a>
</h3>

```typescript
public getInputs(): CustomResourceArgs
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3328">property apiVersion</a>
</h3>

```typescript
public apiVersion: pulumi.Output<string>;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3336">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string>;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3342">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<outputApi.meta.v1.ObjectMeta>;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CustomResourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3308">interface CustomResourceArgs</a>
</h2>

CustomResourceArgs represents a resource definiton we'd use to create an instance of a
Kubernetes CustomResourceDefinition (CRD). For example, the CoreOS Prometheus operator
exposes a CRD `monitoring.coreos.com/ServiceMonitor`; to create a `ServiceMonitor`, we'd
pass a `CustomResourceArgs` containing the `ServiceMonitor` definition to
`apiextensions.CustomResource`.

NOTE: This type is fairly loose, since other than `apiVersion` and `kind`, there are no
fields required across all CRDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3309">property apiVersion</a>
</h3>

```typescript
apiVersion: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3310">property kind</a>
</h3>

```typescript
kind: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L3311">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<inputApi.meta.v1.ObjectMeta>;
```

