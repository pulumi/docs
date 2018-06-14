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
* <a href="#ConfigMissingError">class ConfigMissingError</a>
* <a href="#ConfigTypeError">class ConfigTypeError</a>
* <a href="#CustomResource">class CustomResource</a>
* <a href="#Output">class Output</a>
* <a href="#Resource">class Resource</a>
* <a href="#RunError">class RunError</a>
* <a href="#version">const version</a>
* <a href="#all">function all</a>
* <a href="#getProject">function getProject</a>
* <a href="#getStack">function getStack</a>
* <a href="#output">function output</a>
* <a href="#ResourceOptions">interface ResourceOptions</a>
* <a href="#ID">type ID</a>
* <a href="#Input">type Input</a>
* <a href="#Inputs">type Inputs</a>
* <a href="#URN">type URN</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts">config.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts">errors.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/metadata.ts">metadata.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts">resource.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/version.ts">version.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="asset">asset</a>
* <a href="cmd">cmd</a>
* <a href="dynamic">dynamic</a>
* <a href="log">log</a>
* <a href="runtime">runtime</a>
* <a href="tests">tests</a>

<h2 class="pdoc-module-header" id="ComponentResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L168">class ComponentResource</a>
</h2>

ComponentResource is a resource that aggregates one or more other child resources into a higher
level abstraction. The component resource itself is a resource, but does not require custom CRUD
operations for provisioning.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L168">constructor</a>
</h3>

```typescript
new ComponentResource(t: string, name: string, props?: Inputs, opts?: ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L43">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L188">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L41">property urn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L31">constructor</a>
</h3>

```typescript
new Config(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L171">method fullKey</a>
</h3>

```typescript
private fullKey(key: string): string
```


fullKey turns a simple configuration key into a fully resolved one, by prepending the bag's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L52">method get</a>
</h3>

```typescript
public get(key: string): string | undefined
```


get loads an optional configuration value by its key, or undefined if it doesn't exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L62">method getBoolean</a>
</h3>

```typescript
public getBoolean(key: string): boolean | undefined
```


getBoolean loads an optional configuration value, as a boolean, by its key, or undefined if it doesn't exist.
If the configuration value isn't a legal boolean, this function will throw an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L80">method getNumber</a>
</h3>

```typescript
public getNumber(key: string): number | undefined
```


getNumber loads an optional configuration value, as a number, by its key, or undefined if it doesn't exist.
If the configuration value isn't a legal number, this function will throw an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L98">method getObject</a>
</h3>

```typescript
public getObject<T>(key: string): T | undefined
```


getObject loads an optional configuration value, as an object, by its key, or undefined if it doesn't exist.
This routine simply JSON parses and doesn't validate the shape of the contents.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L116">method require</a>
</h3>

```typescript
public require(key: string): string
```


require loads a configuration value by its given key.  If it doesn't exist, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L130">method requireBoolean</a>
</h3>

```typescript
public requireBoolean(key: string): boolean
```


requireBoolean loads a configuration value, as a boolean, by its given key.  If it doesn't exist, or the
configuration value is not a legal boolean, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L144">method requireNumber</a>
</h3>

```typescript
public requireNumber(key: string): number
```


requireNumber loads a configuration value, as a number, by its given key.  If it doesn't exist, or the
configuration value is not a legal number, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L158">method requireObject</a>
</h3>

```typescript
public requireObject<T>(key: string): T
```


requireObject loads a configuration value, as a number, by its given key.  If it doesn't exist, or the
configuration value is not a legal number, an error is thrown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L31">property name</a>
</h3>

```typescript
public name: string;
```


name is the configuration bag's logical name and uniquely identifies it.

<h2 class="pdoc-module-header" id="ConfigMissingError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L188">class ConfigMissingError</a>
</h2>

ConfigMissingError is used when a configuration value is completely missing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L188">constructor</a>
</h3>

```typescript
new ConfigMissingError(key: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L30">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of a RunError.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L189">property key</a>
</h3>

```typescript
public key: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L886">property message</a>
</h3>

```typescript
static message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L885">property name</a>
</h3>

```typescript
static name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L887">property stack</a>
</h3>

```typescript
static stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="ConfigTypeError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L179">class ConfigTypeError</a>
</h2>

ConfigTypeError is used when a configuration value is of the wrong type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/config.ts#L179">constructor</a>
</h3>

```typescript
new ConfigTypeError(key: string, v: any, expectedType: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L30">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of a RunError.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L886">property message</a>
</h3>

```typescript
static message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L885">property name</a>
</h3>

```typescript
static name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L887">property stack</a>
</h3>

```typescript
static stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="CustomResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L122">class CustomResource</a>
</h2>

CustomResource is a resource whose create, read, update, and delete (CRUD) operations are managed
by performing external operations on some physical entity.  The engine understands how to diff
and perform partial updates of them, and these CRUD operations are implemented in a dynamically
loaded plugin for the defining package.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L141">constructor</a>
</h3>

```typescript
new CustomResource(t: string, name: string, props?: Inputs, opts?: ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L139">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L127">property __pulumiCustomResource</a>
</h3>

```typescript
private __pulumiCustomResource: boolean = true;
```


A private field to help with RTTI that works in SxS scenarios.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L133">property id</a>
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

<h2 class="pdoc-module-header" id="Output">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L205">class Output</a>
</h2>

Output helps encode the relationship between Resources in a Pulumi application. Specifically an
Output holds onto a piece of Data and the Resource it was generated from. An Output value can
then be provided when constructing new Resources, allowing that new Resource to know both the
value as well as the Resource the value came from.  This allows for a precise 'Resource
dependency graph' to be created, which properly tracks the relationship between resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L290">constructor</a>
</h3>

```typescript
public new Output(resources: Set<Resource>, promise: Promise<T>, isKnown: Promise<boolean>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L287">method create</a>
</h3>

```typescript
public static create<T>(resource: Resource, promise: Promise<T>, isKnown: Promise<boolean>): Output<T>
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L283">method isInstance</a>
</h3>

```typescript
public static isInstance<T>(obj: any): boolean
```


Returns true if the given object is an instance of Output<T>.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L212">property __pulumiOutput</a>
</h3>

```typescript
public __pulumiOutput?: undefined | true | false = true;
```


A private field to help with RTTI that works in SxS scenarios.

This is internal instead of being truly private, to support mixins and our serialization model.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L264">property apply</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L275">property get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L221">property isKnown</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L229">property promise</a>
</h3>

```typescript
public promise: { ... };
```


Method that actually produces the concrete value of this output, as well as the total
deployment-time set of resources this output depends on.

Only callable on the outside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L236">property resources</a>
</h3>

```typescript
public resources: { ... };
```


The list of resource that this output value depends on.

Only callable on the outside.

<h2 class="pdoc-module-header" id="Resource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L30">class Resource</a>
</h2>

Resource represents a class whose CRUD operations are implemented by a provider plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L45">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L43">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L35">property __pulumiResource</a>
</h3>

```typescript
private __pulumiResource: boolean = true;
```


A private field to help with RTTI that works in SxS scenarios.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L41">property urn</a>
</h3>

```typescript
public urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RunError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L19">class RunError</a>
</h2>

RunError can be used for terminating a program abruptly, but resulting in a clean exit rather than the usual
verbose unhandled error logic which emits the source program text and complete stack trace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L32">constructor</a>
</h3>

```typescript
new RunError(message: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L30">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of a RunError.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L896">property Error</a>
</h3>

```typescript
static Error: ErrorConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/errors.ts#L24">property __pulumiRunError</a>
</h3>

```typescript
private __pulumiRunError: boolean = true;
```


A private field to help with RTTI that works in SxS scenarios.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L886">property message</a>
</h3>

```typescript
static message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L885">property name</a>
</h3>

```typescript
static name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L887">property stack</a>
</h3>

```typescript
static stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="version">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/version.ts#L15">const version</a>
</h2>

```typescript
const version: ${VERSION} = "${VERSION}";
```

<h2 class="pdoc-module-header" id="all">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L357">function all</a>
</h2>

```typescript
all<T>(val: { ... }): Output<{ ... }>
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
all<T1,T2,T3,T4,T5,T6,T7,T8>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined, Input<T7> | undefined, Input<T8> | undefined]): Output<[, T1, T2, T3, T4, T5, T6, T7, T8]>
```


```typescript
all<T1,T2,T3,T4,T5,T6,T7>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined, Input<T7> | undefined]): Output<[, T1, T2, T3, T4, T5, T6, T7]>
```


```typescript
all<T1,T2,T3,T4,T5,T6>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined, Input<T6> | undefined]): Output<[, T1, T2, T3, T4, T5, T6]>
```


```typescript
all<T1,T2,T3,T4,T5>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined, Input<T5> | undefined]): Output<[, T1, T2, T3, T4, T5]>
```


```typescript
all<T1,T2,T3,T4>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined, Input<T4> | undefined]): Output<[, T1, T2, T3, T4]>
```


```typescript
all<T1,T2,T3>(values: [, Input<T1> | undefined, Input<T2> | undefined, Input<T3> | undefined]): Output<[, T1, T2, T3]>
```


```typescript
all<T1,T2>(values: [, Input<T1> | undefined, Input<T2> | undefined]): Output<[, T1, T2]>
```


```typescript
all<T>(ds: undefined | T | Promise<T> | Output<T>[]): Output<T[]>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L331">function output</a>
</h2>

```typescript
output<T>(cv: Input<T>): Output<T>
```


```typescript
output<T>(cv: Input<T> | undefined): Output<T | undefined>
```

<h2 class="pdoc-module-header" id="ResourceOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L97">interface ResourceOptions</a>
</h2>

ResourceOptions is a bag of optional settings that control a resource's behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L109">property dependsOn</a>
</h3>

```typescript
dependsOn?: Resource[];
```


An optional additional explicit dependencies on other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L101">property id</a>
</h3>

```typescript
id?: Input<ID>;
```


An optional existing ID to load, rather than create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L105">property parent</a>
</h3>

```typescript
parent?: Resource;
```


An optional parent resource to which this resource belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L113">property protect</a>
</h3>

```typescript
protect?: undefined | true | false;
```


When set to true, protect ensures this resource cannot be deleted.

<h2 class="pdoc-module-header" id="ID">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L24">type ID</a>
</h2>

```typescript
type ID = string;
```

<h2 class="pdoc-module-header" id="Input">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L396">type Input</a>
</h2>

```typescript
type Input = T | Promise<T> | Output<T>;
```


Input is a property input for a resource.  It may be a promptly available T, a promise
for one, or the output from a existing Resource.

<h2 class="pdoc-module-header" id="Inputs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L402">type Inputs</a>
</h2>

```typescript
type Inputs = Record<string, Input<any>>;
```


Inputs is a map of property name to property input, one for each resource
property value.

<h2 class="pdoc-module-header" id="URN">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/resource.ts#L25">type URN</a>
</h2>

```typescript
type URN = string;
```

