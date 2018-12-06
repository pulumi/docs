---
title: Package @pulumi/pulumi
---


Node.js:

```javascript
var pulumi = require("@pulumi/pulumi");
```

ES6 modules:

```typescript
import * as pulumi from "@pulumi/pulumi";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ComponentResource">class ComponentResource</a>
* <a href="#Config">class Config</a>
* <a href="#CustomResource">class CustomResource</a>
* <a href="#Output">class Output</a>
* <a href="#ProviderResource">class ProviderResource</a>
* <a href="#Resource">class Resource</a>
* <a href="#ResourceError">class ResourceError</a>
* <a href="#RunError">class RunError</a>
* <a href="#StackReference">class StackReference</a>
* <a href="#deploymentOnlyModule">const deploymentOnlyModule</a>
* <a href="#testingOptions">const testingOptions</a>
* <a href="#version">const version</a>
* <a href="#all">function all</a>
* <a href="#getProject">function getProject</a>
* <a href="#getStack">function getStack</a>
* <a href="#output">function output</a>
* <a href="#ComponentResourceOptions">interface ComponentResourceOptions</a>
* <a href="#CustomResourceOptions">interface CustomResourceOptions</a>
* <a href="#ResourceOptions">interface ResourceOptions</a>
* <a href="#StackReferenceArgs">interface StackReferenceArgs</a>
* <a href="#UnwrappedArray">interface UnwrappedArray</a>
* <a href="#ID">type ID</a>
* <a href="#Input">type Input</a>
* <a href="#Inputs">type Inputs</a>
* <a href="#URN">type URN</a>
* <a href="#Unwrap">type Unwrap</a>
* <a href="#UnwrapSimple">type UnwrapSimple</a>
* <a href="#UnwrappedObject">type UnwrappedObject</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts">config.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts">errors.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/index.ts">index.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/metadata.ts">metadata.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts">resource.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts">stackReference.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/version.ts">version.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="asset">asset</a>
* <a href="cmd">cmd</a>
* <a href="dynamic">dynamic</a>
* <a href="iterable">iterable</a>
* <a href="log">log</a>
* <a href="runtime">runtime</a>
* <a href="tests">tests</a>

<h2 class="pdoc-module-header" id="ComponentResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L258">class ComponentResource</a>
</h2>

ComponentResource is a resource that aggregates one or more other child resources into a higher
level abstraction. The component resource itself is a resource, but does not require custom CRUD
operations for provisioning.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L258">constructor</a>
</h3>

```typescript
new ComponentResource(t: string, name: string, props?: Inputs, opts: ComponentResourceOptions)
```


Creates and registers a new component resource.  t is the fully qualified type token and name
is the "name" part to use in creating a stable and globally unique URN for the object. parent
is the optional parent for this component, and dependsOn is an optional list of other
resources that this resource depends on, controlling the order in which we perform resource
operations.

* `t` The type of the resource.
* `name` The _unique_ name of the resource.
* `props` The arguments to use to populate the new resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L55">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L50">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L281">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L36">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L27">class Config</a>
</h2>

Config is a bag of related configuration state.  Each bag contains any number of configuration variables, indexed by
simple keys, and each has a name that uniquely identifies it; two bags with different names do not share values for
variables that otherwise share the same key.  For example, a bag whose name is `pulumi:foo`, with keys `a`, `b`,
and `c`, is entirely separate from a bag whose name is `pulumi:bar` with the same simple key names.  Each key has a
fully qualified names, such as `pulumi:foo:a`, ..., and `pulumi:bar:a`, respectively.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L32">constructor</a>
</h3>

```typescript
new Config(name?: undefined | string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L52">method get</a>
</h3>

```typescript
public get(key: string, opts?: StringConfigOptions): string | undefined
```


get loads an optional configuration value by its key, or undefined if it doesn't exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L83">method getBoolean</a>
</h3>

```typescript
public getBoolean(key: string): boolean | undefined
```


getBoolean loads an optional configuration value, as a boolean, by its key, or undefined if it doesn't exist.
If the configuration value isn't a legal boolean, this function will throw an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L102">method getNumber</a>
</h3>

```typescript
public getNumber(key: string, opts?: NumberConfigOptions): number | undefined
```


getNumber loads an optional configuration value, as a number, by its key, or undefined if it doesn't exist.
If the configuration value isn't a legal number, this function will throw an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L127">method getObject</a>
</h3>

```typescript
public getObject<T>(key: string): T | undefined
```


getObject loads an optional configuration value, as an object, by its key, or undefined if it doesn't exist.
This routine simply JSON parses and doesn't validate the shape of the contents.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L146">method require</a>
</h3>

```typescript
public require(key: string, opts?: StringConfigOptions): string
```


require loads a configuration value by its given key.  If it doesn't exist, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L160">method requireBoolean</a>
</h3>

```typescript
public requireBoolean(key: string): boolean
```


requireBoolean loads a configuration value, as a boolean, by its given key.  If it doesn't exist, or the
configuration value is not a legal boolean, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L175">method requireNumber</a>
</h3>

```typescript
public requireNumber(key: string, opts?: NumberConfigOptions): number
```


requireNumber loads a configuration value, as a number, by its given key.  If it doesn't exist, or the
configuration value is not a legal number, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L189">method requireObject</a>
</h3>

```typescript
public requireObject<T>(key: string): T
```


requireObject loads a configuration value as a JSON string and deserializes the JSON into a JavaScript object. If
it doesn't exist, or the configuration value is not a legal JSON string, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L32">property name</a>
</h3>

```typescript
public name: string;
```


name is the configuration bag's logical name and uniquely identifies it.  The default is the name of the current
project.

<h2 class="pdoc-module-header" id="CustomResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L190">class CustomResource</a>
</h2>

CustomResource is a resource whose create, read, update, and delete (CRUD) operations are managed
by performing external operations on some physical entity.  The engine understands how to diff
and perform partial updates of them, and these CRUD operations are implemented in a dynamically
loaded plugin for the defining package.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L209">constructor</a>
</h3>

```typescript
new CustomResource(t: string, name: string, props?: Inputs, opts?: CustomResourceOptions)
```


Creates and registers a new managed resource.  t is the fully qualified type token and name
is the "name" part to use in creating a stable and globally unique URN for the object.
dependsOn is an optional list of other resources that this resource depends on, controlling
the order in which we perform resource operations. Creating an instance does not necessarily
perform a create on the physical entity which it represents, and instead, this is dependent
upon the diffing of the new goal state compared to the current known resource state.

* `t` The type of the resource.
* `name` The _unique_ name of the resource.
* `props` The arguments to use to populate the new resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L55">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L207">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L201">property id</a>
</h3>

```typescript
public id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L36">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Output">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L303">class Output</a>
</h2>

Output helps encode the relationship between Resources in a Pulumi application. Specifically an
Output holds onto a piece of Data and the Resource it was generated from. An Output value can
then be provided when constructing new Resources, allowing that new Resource to know both the
value as well as the Resource the value came from.  This allows for a precise 'Resource
dependency graph' to be created, which properly tracks the relationship between resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L393">constructor</a>
</h3>

```typescript
public new Output(resources: Set<Resource> | Resource[] | Resource, promise: Promise<T>, isKnown: Promise<boolean>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L381">method create</a>
</h3>

```typescript
public static create<T>(val: Input<T>): Output<Unwrap<T>>
```


create takes any Input value and converts it into an Output, deeply unwrapping nested Input
values as necessary.


```typescript
public static create<T>(val: Input<T> | undefined): Output<Unwrap<T | undefined>>
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L391">method isInstance</a>
</h3>

```typescript
public static isInstance<T>(obj: any): boolean
```


Returns true if the given object is an instance of Output<T>.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L310">property __pulumiOutput</a>
</h3>

```typescript
public __pulumiOutput?: undefined | false | true = true;
```


A private field to help with RTTI that works in SxS scenarios.

This is internal instead of being truly private, to support mixins and our serialization model.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L362">property apply</a>
</h3>

```typescript
public apply: { ... };
```


Transforms the data of the output with the provided func.  The result remains a
Output so that dependent resources can be properly tracked.

'func' is not allowed to make resources.

'func' can return other Outputs.  This can be handy if you have a Output<SomeVal>
and you want to get a transitive dependency of it.  i.e.

```ts
var d1: Output<SomeVal>;
var d2 = d1.apply(v => v.x.y.OtherOutput); // getting an output off of 'v'.
```

In this example, taking a dependency on d2 means a resource will depend on all the resources
of d1.  It will *not* depend on the resources of v.x.y.OtherDep.

Importantly, the Resources that d2 feels like it will depend on are the same resources as d1.
If you need have multiple Outputs and a single Output is needed that combines both
set of resources, then 'pulumi.all' should be used instead.

This function will only be called execution of a 'pulumi update' request.  It will not run
during 'pulumi preview' (as the values of resources are of course not known then). It is not
available for functions that end up executing in the cloud during runtime.  To get the value
of the Output during cloud runtime execution, use `get()`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L373">property get</a>
</h3>

```typescript
public get: { ... };
```


Retrieves the underlying value of this dependency.

This function is only callable in code that runs in the cloud post-deployment.  At this
point all Output values will be known and can be safely retrieved. During pulumi deployment
or preview execution this must not be called (and will throw).  This is because doing so
would allow Output values to flow into Resources while losing the data that would allow
the dependency graph to be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L319">property isKnown</a>
</h3>

```typescript
public isKnown: Promise<boolean>;
```


Whether or not this 'Output' should actually perform .apply calls.  During a preview,
an Output value may not be known (because it would have to actually be computed by doing an
'update').  In that case, we don't want to perform any .apply calls as the callbacks
may not expect an undefined value.  So, instead, we just transition to another Output
value that itself knows it should not perform .apply calls.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L327">property promise</a>
</h3>

```typescript
public promise: { ... };
```


Method that actually produces the concrete value of this output, as well as the total
deployment-time set of resources this output depends on.

Only callable on the outside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L334">property resources</a>
</h3>

```typescript
public resources: { ... };
```


The list of resource that this output value depends on.

Only callable on the outside.

<h2 class="pdoc-module-header" id="ProviderResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L235">class ProviderResource</a>
</h2>

ProviderResource is a resource that implements CRUD operations for other custom resources. These resources are
managed similarly to other resources, including the usual diffing and update semantics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L235">constructor</a>
</h3>

```typescript
new ProviderResource(pkg: string, name: string, props?: Inputs, opts: ResourceOptions)
```


Creates and registers a new provider resource for a particular package.

* `pkg` The package associated with this provider.
* `name` The _unique_ name of the provider.
* `props` The configuration to use for this provider.
* `opts` A bag of options that control this provider&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L55">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L207">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L201">property id</a>
</h3>

```typescript
public id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L36">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Resource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L25">class Resource</a>
</h2>

Resource represents a class whose CRUD operations are implemented by a provider plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L63">constructor</a>
</h3>

```typescript
new Resource(t: string, name: string, custom: boolean, props: Inputs, opts: ResourceOptions)
```


Creates and registers a new resource object.  t is the fully qualified type token and name is
the "name" part to use in creating a stable and globally unique URN for the object.
dependsOn is an optional list of other resources that this resource depends on, controlling
the order in which we perform resource operations.

* `t` The type of the resource.
* `name` The _unique_ name of the resource.
* `custom` True to indicate that this is a custom resource, managed by a plugin.
* `props` The arguments to use to populate the new resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L55">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L50">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L36">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ResourceError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L49">class ResourceError</a>
</h2>

ResourceError can be used for terminating a program abruptly, specifically associating the
problem with a Resource.  Depending on the nature of the problem, clients can choose whether or
not a call stack should be returned as well.  This should be very rare, and would only indicate
no usefulness of presenting that stack to the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L62">constructor</a>
</h3>

```typescript
new ResourceError(message: string, resource: Resource | undefined, hideStack?: undefined | false | true)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L60">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of a ResourceError.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L914">property Error</a>
</h3>

```typescript
static Error: ErrorConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L64">property hideStack</a>
</h3>

```typescript
public hideStack?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L904">property message</a>
</h3>

```typescript
message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L903">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L64">property resource</a>
</h3>

```typescript
public resource: Resource | undefined;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L905">property stack</a>
</h3>

```typescript
stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="RunError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L23">class RunError</a>
</h2>

RunError can be used for terminating a program abruptly, but resulting in a clean exit rather
than the usual verbose unhandled error logic which emits the source program text and complete
stack trace.  This type should be rarely used.  Ideally ResourceError should always be used so
that as many errors as possible can be associated with a Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L36">constructor</a>
</h3>

```typescript
new RunError(message: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L34">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of a RunError.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L914">property Error</a>
</h3>

```typescript
static Error: ErrorConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L904">property message</a>
</h3>

```typescript
message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L903">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L905">property stack</a>
</h3>

```typescript
stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="StackReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L21">class StackReference</a>
</h2>

Manages a reference to a Pulumi stack. The referenced stack's outputs are available via the
`outputs` property or the `output` method.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L30">constructor</a>
</h3>

```typescript
new StackReference(name: string, args?: StackReferenceArgs, opts?: CustomResourceOptions)
```


Create a StackReference resource with the given unique name, arguments, and options.

If args is not specified, the name of the referenced stack will be the name of the StackReference resource.

* `name` The _unique_ name of the stack reference.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L55">method getOutput</a>
</h3>

```typescript
public getOutput(name: Input<string>): Output<any>
```


Fetches the value of the named stack output.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L55">method getProvider</a>
</h3>

```typescript
public getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L207">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L201">property id</a>
</h3>

```typescript
public id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L25">property name</a>
</h3>

```typescript
public name: Output<string>;
```


The name of the referenced stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L30">property outputs</a>
</h3>

```typescript
public outputs: Output<{ ... }>;
```


The outputs of the referenced stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L36">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="deploymentOnlyModule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/index.ts#L39">const deploymentOnlyModule</a>
</h2>

```typescript
const deploymentOnlyModule: true = true;
```

<h2 class="pdoc-module-header" id="testingOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L292">const testingOptions</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L293">let isDryRun</a>
</h3>

```typescript
let isDryRun: boolean = false;
```

<h2 class="pdoc-module-header" id="version">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/version.ts#L15">const version</a>
</h2>

```typescript
const version: ${VERSION} = "${VERSION}";
```

<h2 class="pdoc-module-header" id="all">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L546">function all</a>
</h2>

```typescript
all<T>(val: Record<string, Input<T>>): Output<Record<string, Unwrap<T>>>
```


Allows for multiple Output objects to be combined into a single Output object.  The single Output
will depend on the union of Resources that the individual dependencies depend on.

This can be used in the following manner:

```ts
var d1: Output<string>;
var d2: Output<number>;

var d3: Output<ResultType> = Output.all([d1, d2]).apply(([s, n]) => ...);
```

In this example, taking a dependency on d3 means a resource will depend on all the resources of
d1 and d2.


```typescript
all<T1,T2,T3,T4,T5,T6,T7,T8>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined, Input<T7> | undefined, Input<T8> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>, Unwrap<T4>, Unwrap<T5>, Unwrap<T6>, Unwrap<T7>, Unwrap<T8>]>
```


```typescript
all<T1,T2,T3,T4,T5,T6,T7>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined, Input<T7> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>, Unwrap<T4>, Unwrap<T5>, Unwrap<T6>, Unwrap<T7>]>
```


```typescript
all<T1,T2,T3,T4,T5,T6>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>, Unwrap<T4>, Unwrap<T5>, Unwrap<T6>]>
```


```typescript
all<T1,T2,T3,T4,T5>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>, Unwrap<T4>, Unwrap<T5>]>
```


```typescript
all<T1,T2,T3,T4>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>, Unwrap<T4>]>
```


```typescript
all<T1,T2,T3>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>, Unwrap<T3>]>
```


```typescript
all<T1,T2>(values: [, Input<T1> | undefined, Input<T2> | undefined]): Output<[, Unwrap<T1>, Unwrap<T2>]>
```


```typescript
all<T>(ds: undefined | T | Promise<T> | Output<T>[]): Output<Unwrap<T>[]>
```

<h2 class="pdoc-module-header" id="getProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/metadata.ts#L22">function getProject</a>
</h2>

```typescript
getProject(): string
```


getProject returns the current project name.  It throws an exception if none is registered.

<h2 class="pdoc-module-header" id="getStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/metadata.ts#L32">function getStack</a>
</h2>

```typescript
getStack(): string
```


getStack returns the current stack name.  It throws an exception if none is registered.

<h2 class="pdoc-module-header" id="output">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L489">function output</a>
</h2>

```typescript
output<T>(val: Input<T>): Output<Unwrap<T>>
```


[output] takes any Input value and converts it into an Output, deeply unwrapping nested Input
values as necessary.

The expected way to use this function is like so:

```ts
     var transformed = pulumi.output(someVal).apply(unwrapped => {
         // Do whatever you want now.  'unwrapped' will contain no outputs/promises inside
         // here, so you can easily do whatever sort of transformation is most convenient.
     });

     // the result can be passed to another Resource.  The dependency information will be
     // properly maintained.
     var someResource = new SomeResource(name, { data: transformed ... });
```


```typescript
output<T>(val: Input<T> | undefined): Output<Unwrap<T | undefined>>
```

<h2 class="pdoc-module-header" id="ComponentResourceOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L177">interface ComponentResourceOptions</a>
</h2>

ComponentResourceOptions is a bag of optional settings that control a component resource's behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L155">property dependsOn</a>
</h3>

```typescript
dependsOn?: Input<Input<Resource>[]> | Input<Resource>;
```


An optional additional explicit dependencies on other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L147">property id</a>
</h3>

```typescript
id?: Input<ID>;
```


An optional existing ID to load, rather than create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L151">property parent</a>
</h3>

```typescript
parent?: Resource;
```


An optional parent resource to which this resource belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L159">property protect</a>
</h3>

```typescript
protect?: undefined | false | true;
```


When set to true, protect ensures this resource cannot be deleted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L181">property providers</a>
</h3>

```typescript
providers?: Record<string, ProviderResource>;
```


An optional set of providers to use for child resources. Keyed by package name (e.g. "aws")

<h2 class="pdoc-module-header" id="CustomResourceOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L165">interface CustomResourceOptions</a>
</h2>

CustomResourceOptions is a bag of optional settings that control a custom resource's behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L155">property dependsOn</a>
</h3>

```typescript
dependsOn?: Input<Input<Resource>[]> | Input<Resource>;
```


An optional additional explicit dependencies on other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L147">property id</a>
</h3>

```typescript
id?: Input<ID>;
```


An optional existing ID to load, rather than create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L151">property parent</a>
</h3>

```typescript
parent?: Resource;
```


An optional parent resource to which this resource belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L159">property protect</a>
</h3>

```typescript
protect?: undefined | false | true;
```


When set to true, protect ensures this resource cannot be deleted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L171">property provider</a>
</h3>

```typescript
provider?: ProviderResource;
```


An optional provider to use for this resource's CRUD operations. If no provider is supplied, the default
provider for the resource's package will be used. The default provider is pulled from the parent's
provider bag (see also ComponentResourceOptions.providers).

<h2 class="pdoc-module-header" id="ResourceOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L143">interface ResourceOptions</a>
</h2>

ResourceOptions is a bag of optional settings that control a resource's behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L155">property dependsOn</a>
</h3>

```typescript
dependsOn?: Input<Input<Resource>[]> | Input<Resource>;
```


An optional additional explicit dependencies on other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L147">property id</a>
</h3>

```typescript
id?: Input<ID>;
```


An optional existing ID to load, rather than create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L151">property parent</a>
</h3>

```typescript
parent?: Resource;
```


An optional parent resource to which this resource belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L159">property protect</a>
</h3>

```typescript
protect?: undefined | false | true;
```


When set to true, protect ensures this resource cannot be deleted.

<h2 class="pdoc-module-header" id="StackReferenceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L63">interface StackReferenceArgs</a>
</h2>

The set of arguments for constructing a StackReference resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/stackReference.ts#L67">property name</a>
</h3>

```typescript
name?: Input<string>;
```


The name of the stack to reference.

<h2 class="pdoc-module-header" id="UnwrappedArray">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L657">interface UnwrappedArray</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L52">method __@iterator</a>
</h3>

```typescript
__@iterator(): IterableIterator<Unwrap<T>>
```


Iterator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.symbol.wellknown.d.ts#L94">method __@unscopables</a>
</h3>

```typescript
__@unscopables(): { ... }
```


Returns an object whose properties have the value 'true'
when they will be absent when used in a 'with' statement.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1161">method concat</a>
</h3>

```typescript
concat(items: ConcatArray<Unwrap<T>>[]): Unwrap<T>[]
```


Combines two or more arrays.


```typescript
concat(items: T | ConcatArray<T>[]): Unwrap<T>[]
```


Combines two or more arrays.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.core.d.ts#L64">method copyWithin</a>
</h3>

```typescript
copyWithin(target: number, start: number, end?: undefined | number): this
```


Returns the this object after copying a section of the array identified by start and end
to the same array starting at position target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L57">method entries</a>
</h3>

```typescript
entries(): IterableIterator<[, number, Unwrap<T>]>
```


Returns an iterable of key, value pairs for every entry in the array

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1226">method every</a>
</h3>

```typescript
every(callbackfn: { ... }, thisArg?: any): boolean
```


Determines whether all the members of an array satisfy the specified test.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.core.d.ts#L53">method fill</a>
</h3>

```typescript
fill(value: Unwrap<T>, start?: undefined | number, end?: undefined | number): this
```


Returns the this object after filling the section identified by start and end with value

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1250">method filter</a>
</h3>

```typescript
filter<S>(callbackfn: { ... }, thisArg?: any): S[]
```


Returns the elements of an array that meet the condition specified in a callback function.


```typescript
filter(callbackfn: { ... }, thisArg?: any): Unwrap<T>[]
```


Returns the elements of an array that meet the condition specified in a callback function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.core.d.ts#L31">method find</a>
</h3>

```typescript
find<S>(predicate: { ... }, thisArg?: any): S | undefined
```


Returns the value of the first element in the array where predicate is true, and undefined
otherwise.


```typescript
find(predicate: { ... }, thisArg?: any): Unwrap<T> | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.core.d.ts#L43">method findIndex</a>
</h3>

```typescript
findIndex(predicate: { ... }, thisArg?: any): number
```


Returns the index of the first element in the array where predicate is true, and -1
otherwise.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1238">method forEach</a>
</h3>

```typescript
forEach(callbackfn: { ... }, thisArg?: any): void
```


Performs the specified action for each element in an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1214">method indexOf</a>
</h3>

```typescript
indexOf(searchElement: Unwrap<T>, fromIndex?: undefined | number): number
```


Returns the index of the first occurrence of a value in an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1171">method join</a>
</h3>

```typescript
join(separator?: undefined | string): string
```


Adds all the elements of an array separated by the specified separator string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L62">method keys</a>
</h3>

```typescript
keys(): IterableIterator<number>
```


Returns an iterable of keys in the array

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1220">method lastIndexOf</a>
</h3>

```typescript
lastIndexOf(searchElement: Unwrap<T>, fromIndex?: undefined | number): number
```


Returns the index of the last occurrence of a specified value in an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1244">method map</a>
</h3>

```typescript
map<U>(callbackfn: { ... }, thisArg?: any): U[]
```


Calls a defined callback function on each element of an array, and returns an array that contains the results.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1151">method pop</a>
</h3>

```typescript
pop(): Unwrap<T> | undefined
```


Removes the last element from an array and returns it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1156">method push</a>
</h3>

```typescript
push(items: Unwrap<T>[]): number
```


Appends new elements to an array, and returns the new length of the array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1262">method reduce</a>
</h3>

```typescript
reduce(callbackfn: { ... }): Unwrap<T>
```


Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.


```typescript
reduce(callbackfn: { ... }, initialValue: Unwrap<T>): Unwrap<T>
```


```typescript
reduce<U>(callbackfn: { ... }, initialValue: U): U
```


Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1275">method reduceRight</a>
</h3>

```typescript
reduceRight(callbackfn: { ... }): Unwrap<T>
```


Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.


```typescript
reduceRight(callbackfn: { ... }, initialValue: Unwrap<T>): Unwrap<T>
```


```typescript
reduceRight<U>(callbackfn: { ... }, initialValue: U): U
```


Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1175">method reverse</a>
</h3>

```typescript
reverse(): Unwrap<T>[]
```


Reverses the elements in an Array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1179">method shift</a>
</h3>

```typescript
shift(): Unwrap<T> | undefined
```


Removes the first element from an array and returns it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1185">method slice</a>
</h3>

```typescript
slice(start?: undefined | number, end?: undefined | number): Unwrap<T>[]
```


Returns a section of an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1232">method some</a>
</h3>

```typescript
some(callbackfn: { ... }, thisArg?: any): boolean
```


Determines whether the specified callback function returns true for any element of an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1190">method sort</a>
</h3>

```typescript
sort(compareFn?: undefined | { ... }): this
```


Sorts an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1196">method splice</a>
</h3>

```typescript
splice(start: number, deleteCount?: undefined | number): Unwrap<T>[]
```


Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.


```typescript
splice(start: number, deleteCount: number, items: Unwrap<T>[]): Unwrap<T>[]
```


Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1147">method toLocaleString</a>
</h3>

```typescript
toLocaleString(): string
```


Returns a string representation of an array. The elements are converted to string using their toLocalString methods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1143">method toString</a>
</h3>

```typescript
toString(): string
```


Returns a string representation of an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1208">method unshift</a>
</h3>

```typescript
unshift(items: Unwrap<T>[]): number
```


Inserts new elements at the start of an array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L67">method values</a>
</h3>

```typescript
values(): IterableIterator<Unwrap<T>>
```


Returns an iterable of values in the array

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1298">property Array</a>
</h3>

```typescript
Array: ArrayConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typedoc/node_modules/typescript/lib/lib.es5.d.ts#L1139">property length</a>
</h3>

```typescript
length: number;
```


Gets or sets the length of the array. This is a number one higher than the highest element defined in an array.

<h2 class="pdoc-module-header" id="ID">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L19">type ID</a>
</h2>

```typescript
type ID = string;
```

<h2 class="pdoc-module-header" id="Input">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L597">type Input</a>
</h2>

```typescript
type Input = T | Promise<T> | Output<T>;
```


Input is a property input for a resource.  It may be a promptly available T, a promise
for one, or the output from a existing Resource.

<h2 class="pdoc-module-header" id="Inputs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L603">type Inputs</a>
</h2>

```typescript
type Inputs = Record<string, Input<any>>;
```


Inputs is a map of property name to property input, one for each resource
property value.

<h2 class="pdoc-module-header" id="URN">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L20">type URN</a>
</h2>

```typescript
type URN = string;
```

<h2 class="pdoc-module-header" id="Unwrap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L629">type Unwrap</a>
</h2>

```typescript
type Unwrap = Unwrap<T>;
```


The 'Unwrap' type allows us to express the operation of taking a type, with potentially deeply
nested Promises and Outputs and to then get that same type with all the Promises and Outputs
replaced with their wrapped type.  Note that this Unwrapping is 'deep'.  So if you had:

     `type X = { A: Promise<{ B: Output<{ c: Input<boolean> }> }> }`

Then `Unwrap<X>` would be equivalent to:

     `...    = { A: { B: { C: boolean } } }`

Unwrapping sees through Promises, Outputs, Arrays and Objects.

Note: due to TypeScript limitations there are some things that cannot be expressed. Specifically,
if you had a `Promise<Output<T>>` then the Unwrap type would not be able to undo both of those
wraps. In practice that should be ok.  Values in an object graph should not wrap Outputs in
Promises.  Instead, any code that needs to work Outputs and also be async should either create
the Output with the Promise (which will collapse into just an Output).  Or, it should start with
an Output and call [apply] on it, passing in an async function.  This will also collapse and just
produce an Output.

In other words, this should not be used as the shape of an object: `{ a: Promise<Output<...>> }`.
It should always either be `{ a: Promise<NonOutput> }` or just `{ a: Output<...> }`.

<h2 class="pdoc-module-header" id="UnwrapSimple">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L642">type UnwrapSimple</a>
</h2>

```typescript
type UnwrapSimple = UnwrapSimple<T>;
```


Handles encountering basic types when unwrapping.

<h2 class="pdoc-module-header" id="UnwrappedObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L659">type UnwrappedObject</a>
</h2>

```typescript
type UnwrappedObject = { ... };
```

