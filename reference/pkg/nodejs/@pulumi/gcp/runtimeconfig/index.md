---
title: Module runtimeconfig
---

<a href="../index.html">@pulumi/gcp</a> &gt; runtimeconfig

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Config">class Config</a>
* <a href="#Variavble">class Variavble</a>
* <a href="#ConfigArgs">interface ConfigArgs</a>
* <a href="#ConfigState">interface ConfigState</a>
* <a href="#VariavbleArgs">interface VariavbleArgs</a>
* <a href="#VariavbleState">interface VariavbleState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts">runtimeconfig/config.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts">runtimeconfig/variavble.ts</a> 


<h2 class="pdoc-module-header" id="Config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L12">class Config</a>
</h2>

Manages a RuntimeConfig resource in Google Cloud. For more information, see the
[official documentation](https://cloud.google.com/deployment-manager/runtime-configurator/),
or the
[JSON API](https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L38">constructor</a>
</h3>

```typescript
new Config(name: string, args?: ConfigArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Config resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigState): Config
```


Get an existing Config resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description to associate with the runtime
config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the runtime config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L38">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Variavble">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L12">class Variavble</a>
</h2>

Manages a RuntimeConfig variable in Google Cloud. For more information, see the
[official documentation](https://cloud.google.com/deployment-manager/runtime-configurator/),
or the
[JSON API](https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L47">constructor</a>
</h3>

```typescript
new Variavble(name: string, args: VariavbleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Variavble resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VariavbleState): Variavble
```


Get an existing Variavble resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the variable to manage. Note that variable
names can be hierarchical using slashes (e.g. "prod-variables/hostname").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L34">property parent</a>
</h3>

```typescript
public parent: pulumi.Output<string>;
```


The name of the RuntimeConfig resource containing this
variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L39">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L40">property text</a>
</h3>

```typescript
public text: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L46">property updateTime</a>
</h3>

```typescript
public updateTime: pulumi.Output<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format,
accurate to nanoseconds, representing when the variable was last updated.
Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L47">property value</a>
</h3>

```typescript
public value: pulumi.Output<string | undefined>;
```

<h2 class="pdoc-module-header" id="ConfigArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L88">interface ConfigArgs</a>
</h2>

The set of arguments for constructing a Config resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L93">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description to associate with the runtime
config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the runtime config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L102">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="ConfigState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L68">interface ConfigState</a>
</h2>

Input properties used for looking up and filtering Config resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L73">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description to associate with the runtime
config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L77">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the runtime config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/config.ts#L82">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="VariavbleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L115">interface VariavbleArgs</a>
</h2>

The set of arguments for constructing a Variavble resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the variable to manage. Note that variable
names can be hierarchical using slashes (e.g. "prod-variables/hostname").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L125">property parent</a>
</h3>

```typescript
parent: pulumi.Input<string>;
```


The name of the RuntimeConfig resource containing this
variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L130">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L131">property text</a>
</h3>

```typescript
text?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L132">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="VariavbleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L86">interface VariavbleState</a>
</h2>

Input properties used for looking up and filtering Variavble resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the variable to manage. Note that variable
names can be hierarchical using slashes (e.g. "prod-variables/hostname").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L96">property parent</a>
</h3>

```typescript
parent?: pulumi.Input<string>;
```


The name of the RuntimeConfig resource containing this
variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L101">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L102">property text</a>
</h3>

```typescript
text?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L108">property updateTime</a>
</h3>

```typescript
updateTime?: pulumi.Input<string>;
```


(Computed) The timestamp in RFC3339 UTC "Zulu" format,
accurate to nanoseconds, representing when the variable was last updated.
Example: "2016-10-09T12:33:37.578138407Z".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/runtimeconfig/variavble.ts#L109">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```

