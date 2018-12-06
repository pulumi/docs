---
title: Module devspace
---

<a href="../index.html">@pulumi/azure</a> &gt; devspace

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Controller">class Controller</a>
* <a href="#ControllerArgs">interface ControllerArgs</a>
* <a href="#ControllerState">interface ControllerState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts">devspace/controller.ts</a> 


<h2 class="pdoc-module-header" id="Controller">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L10">class Controller</a>
</h2>

Manages a DevSpace Controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L58">constructor</a>
</h3>

```typescript
new Controller(name: string, args: ControllerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Controller resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ControllerState): Controller
```


Get an existing Controller resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L26">property dataPlaneFqdn</a>
</h3>

```typescript
public dataPlaneFqdn: pulumi.Output<string>;
```


DNS name for accessing DataPlane services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L30">property hostSuffix</a>
</h3>

```typescript
public hostSuffix: pulumi.Output<string>;
```


The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L34">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L46">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as documented below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L54">property targetContainerHostCredentialsBase64</a>
</h3>

```typescript
public targetContainerHostCredentialsBase64: pulumi.Output<string>;
```


Base64 encoding of `kube_config_raw` of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L58">property targetContainerHostResourceId</a>
</h3>

```typescript
public targetContainerHostResourceId: pulumi.Output<string>;
```


The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ControllerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L160">interface ControllerArgs</a>
</h2>

The set of arguments for constructing a Controller resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L164">property hostSuffix</a>
</h3>

```typescript
hostSuffix: pulumi.Input<string>;
```


The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L168">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L172">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L176">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L180">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as documented below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L184">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L188">property targetContainerHostCredentialsBase64</a>
</h3>

```typescript
targetContainerHostCredentialsBase64: pulumi.Input<string>;
```


Base64 encoding of `kube_config_raw` of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L192">property targetContainerHostResourceId</a>
</h3>

```typescript
targetContainerHostResourceId: pulumi.Input<string>;
```


The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ControllerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L118">interface ControllerState</a>
</h2>

Input properties used for looking up and filtering Controller resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L122">property dataPlaneFqdn</a>
</h3>

```typescript
dataPlaneFqdn?: pulumi.Input<string>;
```


DNS name for accessing DataPlane services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L126">property hostSuffix</a>
</h3>

```typescript
hostSuffix?: pulumi.Input<string>;
```


The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L130">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L138">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L142">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as documented below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L146">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L150">property targetContainerHostCredentialsBase64</a>
</h3>

```typescript
targetContainerHostCredentialsBase64?: pulumi.Input<string>;
```


Base64 encoding of `kube_config_raw` of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devspace/controller.ts#L154">property targetContainerHostResourceId</a>
</h3>

```typescript
targetContainerHostResourceId?: pulumi.Input<string>;
```


The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

