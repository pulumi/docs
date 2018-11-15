---
title: Module runtime
---

<a href="../index.html">@pulumi/pulumi</a> &gt; runtime

<h2 class="pdoc-module-header">Index</h2>

* <a href="#getFunctionLocationAsync">const getFunctionLocationAsync</a>
* <a href="#lookupCapturedVariableValueAsync">const lookupCapturedVariableValueAsync</a>
* <a href="#rootPulumiStackTypeName">const rootPulumiStackTypeName</a>
* <a href="#specialArchiveSig">const specialArchiveSig</a>
* <a href="#specialAssetSig">const specialAssetSig</a>
* <a href="#specialSigKey">const specialSigKey</a>
* <a href="#unknownValue">const unknownValue</a>
* <a href="#allConfig">function allConfig</a>
* <a href="#createFunctionInfoAsync">function createFunctionInfoAsync</a>
* <a href="#debuggablePromise">function debuggablePromise</a>
* <a href="#deserializeProperties">function deserializeProperties</a>
* <a href="#deserializeProperty">function deserializeProperty</a>
* <a href="#disconnect">function disconnect</a>
* <a href="#disconnectSync">function disconnectSync</a>
* <a href="#errorString">function errorString</a>
* <a href="#getConfig">function getConfig</a>
* <a href="#getEngine">function getEngine</a>
* <a href="#getMonitor">function getMonitor</a>
* <a href="#getProject">function getProject</a>
* <a href="#getRootResource">function getRootResource</a>
* <a href="#getStack">function getStack</a>
* <a href="#hasMonitor">function hasMonitor</a>
* <a href="#invoke">function invoke</a>
* <a href="#isDryRun">function isDryRun</a>
* <a href="#parseFunction">function parseFunction</a>
* <a href="#readResource">function readResource</a>
* <a href="#registerResource">function registerResource</a>
* <a href="#registerResourceOutputs">function registerResourceOutputs</a>
* <a href="#resolveProperties">function resolveProperties</a>
* <a href="#rewriteSuperReferences">function rewriteSuperReferences</a>
* <a href="#rpcKeepAlive">function rpcKeepAlive</a>
* <a href="#runInPulumiStack">function runInPulumiStack</a>
* <a href="#serialize">function serialize</a>
* <a href="#serializeFunction">function serializeFunction</a>
* <a href="#serializeFunctionAsync">function serializeFunctionAsync</a>
* <a href="#serializeProperties">function serializeProperties</a>
* <a href="#serializeProperty">function serializeProperty</a>
* <a href="#serializeResourceProperties">function serializeResourceProperties</a>
* <a href="#setConfig">function setConfig</a>
* <a href="#setIsDryRun">function setIsDryRun</a>
* <a href="#setRootResource">function setRootResource</a>
* <a href="#transferProperties">function transferProperties</a>
* <a href="#CapturedPropertyChain">interface CapturedPropertyChain</a>
* <a href="#CapturedPropertyInfo">interface CapturedPropertyInfo</a>
* <a href="#CapturedVariables">interface CapturedVariables</a>
* <a href="#Entry">interface Entry</a>
* <a href="#FunctionInfo">interface FunctionInfo</a>
* <a href="#ObjectInfo">interface ObjectInfo</a>
* <a href="#Options">interface Options</a>
* <a href="#ParsedFunction">interface ParsedFunction</a>
* <a href="#ParsedFunctionCode">interface ParsedFunctionCode</a>
* <a href="#PropertyInfo">interface PropertyInfo</a>
* <a href="#PropertyInfoAndValue">interface PropertyInfoAndValue</a>
* <a href="#PropertyMap">interface PropertyMap</a>
* <a href="#SerializeFunctionArgs">interface SerializeFunctionArgs</a>
* <a href="#SerializedFunction">interface SerializedFunction</a>
* <a href="#excessiveDebugOutput">let excessiveDebugOutput</a>
* <a href="#CapturedVariableMap">type CapturedVariableMap</a>
* <a href="#OutputResolvers">type OutputResolvers</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts">runtime/closure/createClosure.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts">runtime/closure/parseFunction.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/rewriteSuper.ts">runtime/closure/rewriteSuper.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts">runtime/closure/serializeClosure.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts">runtime/closure/v8.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts">runtime/config.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts">runtime/debuggable.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts">runtime/invoke.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts">runtime/resource.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts">runtime/rpc.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts">runtime/settings.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts">runtime/stack.ts</a> 


<h2 class="pdoc-module-header" id="getFunctionLocationAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L51">const getFunctionLocationAsync</a>
</h2>

```typescript
const getFunctionLocationAsync: getFunctionLocationAsync =  versionSpecificV8Module.getFunctionLocationAsync;
```


Given a function, returns the file, line and column number in the file where this function was
defined. Returns { "", 0, 0 } if the location cannot be found or if the given function has no Script.

<h2 class="pdoc-module-header" id="lookupCapturedVariableValueAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L45">const lookupCapturedVariableValueAsync</a>
</h2>

```typescript
const lookupCapturedVariableValueAsync: lookupCapturedVariableValueAsync =  versionSpecificV8Module.lookupCapturedVariableValueAsync;
```


Given a function and a free variable name, lookupCapturedVariableValue looks up the value of that free variable
in the scope chain of the provided function. If the free variable is not found, `throwOnFailure` indicates
whether or not this function should throw or return `undefined.

<h2 class="pdoc-module-header" id="rootPulumiStackTypeName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L24">const rootPulumiStackTypeName</a>
</h2>

```typescript
const rootPulumiStackTypeName: pulumi:pulumi:Stack = "pulumi:pulumi:Stack";
```


rootPulumiStackTypeName is the type name that should be used to construct the root component in the tree of Pulumi
resources allocated by a deployment.  This must be kept up to date with
`github.com/pulumi/pulumi/pkg/resource/stack.RootPulumiStackTypeName`.

<h2 class="pdoc-module-header" id="specialArchiveSig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L216">const specialArchiveSig</a>
</h2>

```typescript
const specialArchiveSig: 0def7320c3a5731c473e5ecbe6d01bc7 = "0def7320c3a5731c473e5ecbe6d01bc7";
```


specialArchiveSig is a randomly assigned hash used to identify archives in maps.  See pkg/resource/asset.go.

<h2 class="pdoc-module-header" id="specialAssetSig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L212">const specialAssetSig</a>
</h2>

```typescript
const specialAssetSig: c44067f5952c0a294b673a41bacd8c17 = "c44067f5952c0a294b673a41bacd8c17";
```


specialAssetSig is a randomly assigned hash used to identify assets in maps.  See pkg/resource/asset.go.

<h2 class="pdoc-module-header" id="specialSigKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L208">const specialSigKey</a>
</h2>

```typescript
const specialSigKey: 4dabf18193072939515e22adb298388d = "4dabf18193072939515e22adb298388d";
```


specialSigKey is sometimes used to encode type identity inside of a map.  See pkg/resource/properties.go.

<h2 class="pdoc-module-header" id="unknownValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L204">const unknownValue</a>
</h2>

```typescript
const unknownValue: 04da6b54-80e4-46f7-96ec-b56ff0331ba9 = "04da6b54-80e4-46f7-96ec-b56ff0331ba9";
```


Unknown values are encoded as a distinguished string value.

<h2 class="pdoc-module-header" id="allConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L25">function allConfig</a>
</h2>

```typescript
allConfig(): { ... }
```


allConfig returns a copy of the full config map.

<h2 class="pdoc-module-header" id="createFunctionInfoAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L217">function createFunctionInfoAsync</a>
</h2>

```typescript
createFunctionInfoAsync(func: Function, serialize: { ... }, logResource: resource.Resource | undefined): Promise<FunctionInfo>
```


createFunctionInfo serializes a function and its closure environment into a form that is
amenable to persistence as simple JSON.  Like toString, it includes the full text of the
function's source code, suitable for execution. Unlike toString, it actually includes information
about the captured environment.

<h2 class="pdoc-module-header" id="debuggablePromise">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L40">function debuggablePromise</a>
</h2>

```typescript
debuggablePromise<T>(p: Promise<T>, ctx?: any): Promise<T>
```


debuggablePromise optionally wraps a promise with some goo to make it easier to debug common problems.

<h2 class="pdoc-module-header" id="deserializeProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L115">function deserializeProperties</a>
</h2>

```typescript
deserializeProperties(outputsStruct: any): any
```


deserializeProperties fetches the raw outputs and deserializes them from a gRPC call result.

<h2 class="pdoc-module-header" id="deserializeProperty">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L310">function deserializeProperty</a>
</h2>

```typescript
deserializeProperty(prop: any): any
```


deserializeProperty unpacks some special types, reversing the above process.

<h2 class="pdoc-module-header" id="disconnect">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L162">function disconnect</a>
</h2>

```typescript
disconnect(): void
```


disconnect permanently disconnects from the server, closing the connections.  It waits for the existing RPC
queue to drain.  If any RPCs come in afterwards, however, they will crash the process.

<h2 class="pdoc-module-header" id="disconnectSync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L180">function disconnectSync</a>
</h2>

```typescript
disconnectSync(): void
```


disconnectSync permanently disconnects from the server, closing the connections. Unlike `disconnect`. it does not
wait for the existing RPC queue to drain. Any RPCs that come in after this call will crash the process.

<h2 class="pdoc-module-header" id="errorString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L102">function errorString</a>
</h2>

```typescript
errorString(err: Error): string
```


errorString produces a string from an error, conditionally including additional diagnostics.

<h2 class="pdoc-module-header" id="getConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L39">function getConfig</a>
</h2>

```typescript
getConfig(k: string): string | undefined
```


getConfig returns a configuration variable's value or undefined if it is unset.

<h2 class="pdoc-module-header" id="getEngine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L111">function getEngine</a>
</h2>

```typescript
getEngine(): Object | undefined
```


getEngine returns the current engine, if any, for RPC communications back to the resource engine.

<h2 class="pdoc-module-header" id="getMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L88">function getMonitor</a>
</h2>

```typescript
getMonitor(): Object
```


getMonitor returns the current resource monitoring service client for RPC communications.

<h2 class="pdoc-module-header" id="getProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L62">function getProject</a>
</h2>

```typescript
getProject(): string | undefined
```


Get the project being run by the current update.

<h2 class="pdoc-module-header" id="getRootResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L224">function getRootResource</a>
</h2>

```typescript
getRootResource(): Promise<URN | undefined>
```


getRootResource returns a root resource URN that will automatically become the default parent of all resources.  This
can be used to ensure that all resources without explicit parents are parented to a common parent resource.

<h2 class="pdoc-module-header" id="getStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L69">function getStack</a>
</h2>

```typescript
getStack(): string | undefined
```


Get the stack being targeted by the current update.

<h2 class="pdoc-module-header" id="hasMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L81">function hasMonitor</a>
</h2>

```typescript
hasMonitor(): boolean
```


hasMonitor returns true if we are currently connected to a resource monitoring service.

<h2 class="pdoc-module-header" id="invoke">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L31">function invoke</a>
</h2>

```typescript
invoke(tok: string, props: Inputs, opts?: InvokeOptions): Promise<any>
```


invoke dynamically invokes the function, tok, which is offered by a provider plugin.  The inputs
can be a bag of computed values (Ts or Promise<T>s), and the result is a Promise<any> that
resolves when the invoke finishes.

<h2 class="pdoc-module-header" id="isDryRun">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L55">function isDryRun</a>
</h2>

```typescript
isDryRun(): boolean
```


Returns true if we're currently performing a dry-run, or false if this is a true update.

<h2 class="pdoc-module-header" id="parseFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L97">function parseFunction</a>
</h2>

```typescript
parseFunction(funcString: string): [, string, ParsedFunction]
```

<h2 class="pdoc-module-header" id="readResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L56">function readResource</a>
</h2>

```typescript
readResource(res: Resource, t: string, name: string, props: Inputs, opts: ResourceOptions): void
```


Reads an existing custom resource's state from the resource monitor.  Note that resources read in this way
will not be part of the resulting stack's state, as they are presumed to belong to another.

<h2 class="pdoc-module-header" id="registerResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L112">function registerResource</a>
</h2>

```typescript
registerResource(res: Resource, t: string, name: string, custom: boolean, props: Inputs, opts: ResourceOptions): void
```


registerResource registers a new resource object with a given type t and name.  It returns the auto-generated
URN and the ID that will resolve after the deployment has completed.  All properties will be initialized to property
objects that the registration operation will resolve at the right time (or remain unresolved for deployments).

<h2 class="pdoc-module-header" id="registerResourceOutputs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L297">function registerResourceOutputs</a>
</h2>

```typescript
registerResourceOutputs(res: Resource, outputs: Inputs | Promise<Inputs> | Output<Inputs>): void
```


registerResourceOutputs completes the resource registration, attaching an optional set of computed outputs.

<h2 class="pdoc-module-header" id="resolveProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L135">function resolveProperties</a>
</h2>

```typescript
resolveProperties(res: Resource, resolvers: Record<string, { ... }>, t: string, name: string, allProps: any): void
```


resolveProperties takes as input a gRPC serialized proto.google.protobuf.Struct and resolves all
of the resource's matching properties to the values inside.

NOTE: it is imperative that the properties in `allProps` were produced by `deserializeProperties` in order for
output properties to work correctly w.r.t. knowns/unknowns: this function assumes that any undefined value in
`allProps`represents an unknown value that was returned by an engine operation.

<h2 class="pdoc-module-header" id="rewriteSuperReferences">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/rewriteSuper.ts#L19">function rewriteSuperReferences</a>
</h2>

```typescript
rewriteSuperReferences(code: string, isStatic: boolean): string
```

<h2 class="pdoc-module-header" id="rpcKeepAlive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L211">function rpcKeepAlive</a>
</h2>

```typescript
rpcKeepAlive(): { ... }
```


rpcKeepAlive registers a pending call to ensure that we don't prematurely disconnect from the server.  It returns
a function that, when invoked, signals that the RPC has completed.

<h2 class="pdoc-module-header" id="runInPulumiStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L30">function runInPulumiStack</a>
</h2>

```typescript
runInPulumiStack(init: { ... }): Promise<Inputs | undefined>
```


runInPulumiStack creates a new Pulumi stack resource and executes the callback inside of it.  Any outputs
returned by the callback will be stored as output properties on this resulting Stack object.

<h2 class="pdoc-module-header" id="serialize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L125">function serialize</a>
</h2>

```typescript
serialize(): boolean
```


serialize returns true if resource operations should be serialized.

<h2 class="pdoc-module-header" id="serializeFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L84">function serializeFunction</a>
</h2>

```typescript
serializeFunction(func: Function, args: SerializeFunctionArgs): Promise<SerializedFunction>
```


serializeFunction serializes a JavaScript function into a text form that can be loaded in another execution context,
for example as part of a function callback associated with an AWS Lambda.  The function serialization captures any
variables captured by the function body and serializes those values into the generated text along with the function
body.  This process is recursive, so that functions referenced by the body of the serialized function will themselves
be serialized as well.  This process also deeply serializes captured object values, including prototype chains and
property descriptors, such that the semantics of the function when deserialized should match the original function.

There are several known limitations:
- If a native function is captured either directly or indirectly, closure serialization will return an error.
- Captured values will be serialized based on their values at the time that `serializeFunction` is called.  Mutations
  to these values after that (but before the deserialized function is used) will not be observed by the deserialized
  function.

<h2 class="pdoc-module-header" id="serializeFunctionAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L100">function serializeFunctionAsync</a>
</h2>

```typescript
serializeFunctionAsync(func: Function, serialize?: undefined | { ... }): Promise<string>
```

<h2 class="pdoc-module-header" id="serializeProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L107">function serializeProperties</a>
</h2>

```typescript
serializeProperties(label: string, props: Inputs, dependentResources: Resource[]): Promise<Record<string, any>>
```


serializeProperties walks the props object passed in, awaiting all interior promises, creating a reasonable
POJO object that can be remoted over to registerResource.

<h2 class="pdoc-module-header" id="serializeProperty">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L222">function serializeProperty</a>
</h2>

```typescript
serializeProperty(ctx: string, prop: Input<any>, dependentResources: Resource[]): Promise<any>
```


serializeProperty serializes properties deeply.  This understands how to wait on any unresolved promises, as
appropriate, in addition to translating certain "special" values so that they are ready to go on the wire.

<h2 class="pdoc-module-header" id="serializeResourceProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L98">function serializeResourceProperties</a>
</h2>

```typescript
serializeResourceProperties(label: string, props: Inputs, dependentResources: Resource[]): Promise<Record<string, any>>
```


serializeResourceProperties walks the props object passed in, awaiting all interior promises besides those for `id`
and `urn`, creating a reasonable POJO object that can be remoted over to registerResource.

<h2 class="pdoc-module-header" id="setConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L32">function setConfig</a>
</h2>

```typescript
setConfig(k: string, v: string): void
```


setConfig sets a configuration variable.

<h2 class="pdoc-module-header" id="setIsDryRun">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L48">function setIsDryRun</a>
</h2>

```typescript
setIsDryRun(val: boolean): void
```

<h2 class="pdoc-module-header" id="setRootResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L261">function setRootResource</a>
</h2>

```typescript
setRootResource(res: ComponentResource): Promise<void>
```


setRootResource registers a resource that will become the default parent for all resources without explicit parents.

<h2 class="pdoc-module-header" id="transferProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L38">function transferProperties</a>
</h2>

```typescript
transferProperties(onto: Resource, label: string, props: Inputs): OutputResolvers
```


transferProperties mutates the 'onto' resource so that it has Promise-valued properties for all
the 'props' input/output props.  *Importantly* all these promises are completely unresolved. This
is because we don't want anyone to observe the values of these properties until the rpc call to
registerResource actually returns.  This is because the registerResource call may actually
override input values, and we only want people to see the final value.

The result of this call (beyond the stateful changes to 'onto') is the set of Promise resolvers
that will be called post-RPC call.  When the registerResource RPC call comes back, the values
that the engine actualy produced will be used to resolve all the unresolved promised placed on
'onto'.

<h2 class="pdoc-module-header" id="CapturedPropertyChain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L57">interface CapturedPropertyChain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L58">property infos</a>
</h3>

```typescript
infos: CapturedPropertyInfo[];
```

<h2 class="pdoc-module-header" id="CapturedPropertyInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L49">interface CapturedPropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L51">property invoked</a>
</h3>

```typescript
invoked: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L50">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="CapturedVariables">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L75">interface CapturedVariables</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L77">property optional</a>
</h3>

```typescript
optional: CapturedVariableMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L76">property required</a>
</h3>

```typescript
required: CapturedVariableMap;
```

<h2 class="pdoc-module-header" id="Entry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L85">interface Entry</a>
</h2>

Entry is the environment slot for a named lexically captured variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L100">property array</a>
</h3>

```typescript
array?: Entry[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L114">property expr</a>
</h3>

```typescript
expr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L93">property function</a>
</h3>

```typescript
function?: FunctionInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L87">property json</a>
</h3>

```typescript
json?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L103">property module</a>
</h3>

```typescript
module?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L97">property object</a>
</h3>

```typescript
object?: ObjectInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L111">property output</a>
</h3>

```typescript
output?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L107">property promise</a>
</h3>

```typescript
promise?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L90">property regexp</a>
</h3>

```typescript
regexp?: undefined | { ... };
```

<h2 class="pdoc-module-header" id="FunctionInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L38">interface FunctionInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L43">property capturedValues</a>
</h3>

```typescript
capturedValues: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L40">property code</a>
</h3>

```typescript
code: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L33">property env</a>
</h3>

```typescript
env: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L50">property name</a>
</h3>

```typescript
name: string | undefined;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L29">property proto</a>
</h3>

```typescript
proto?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L46">property usesNonLexicalThis</a>
</h3>

```typescript
usesNonLexicalThis: boolean;
```

<h2 class="pdoc-module-header" id="ObjectInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L25">interface ObjectInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L33">property env</a>
</h3>

```typescript
env: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L29">property proto</a>
</h3>

```typescript
proto?: Entry;
```

<h2 class="pdoc-module-header" id="Options">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L32">interface Options</a>
</h2>

Options is a bag of settings that controls the behavior of previews and deployments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L39">property dryRun</a>
</h3>

```typescript
dryRun?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L36">property engineAddr</a>
</h3>

```typescript
engineAddr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L37">property monitorAddr</a>
</h3>

```typescript
monitorAddr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L35">property parallel</a>
</h3>

```typescript
parallel?: undefined | number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L33">property project</a>
</h3>

```typescript
project?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L34">property stack</a>
</h3>

```typescript
stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="ParsedFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L39">interface ParsedFunction</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L41">property capturedVariables</a>
</h3>

```typescript
capturedVariables: CapturedVariables;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L27">property funcExprWithName</a>
</h3>

```typescript
funcExprWithName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L23">property funcExprWithoutName</a>
</h3>

```typescript
funcExprWithoutName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L33">property functionDeclarationName</a>
</h3>

```typescript
functionDeclarationName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L36">property isArrowFunction</a>
</h3>

```typescript
isArrowFunction: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L44">property usesNonLexicalThis</a>
</h3>

```typescript
usesNonLexicalThis: boolean;
```

<h2 class="pdoc-module-header" id="ParsedFunctionCode">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L20">interface ParsedFunctionCode</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L27">property funcExprWithName</a>
</h3>

```typescript
funcExprWithName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L23">property funcExprWithoutName</a>
</h3>

```typescript
funcExprWithoutName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L33">property functionDeclarationName</a>
</h3>

```typescript
functionDeclarationName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L36">property isArrowFunction</a>
</h3>

```typescript
isArrowFunction: boolean;
```

<h2 class="pdoc-module-header" id="PropertyInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L55">interface PropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L60">property configurable</a>
</h3>

```typescript
configurable?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L61">property enumerable</a>
</h3>

```typescript
enumerable?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L66">property get</a>
</h3>

```typescript
get?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L57">property hasValue</a>
</h3>

```typescript
hasValue: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L67">property set</a>
</h3>

```typescript
set?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L62">property writable</a>
</h3>

```typescript
writable?: undefined | false | true;
```

<h2 class="pdoc-module-header" id="PropertyInfoAndValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L72">interface PropertyInfoAndValue</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L74">property entry</a>
</h3>

```typescript
entry: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L73">property info</a>
</h3>

```typescript
info?: PropertyInfo;
```

<h2 class="pdoc-module-header" id="PropertyMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L79">interface PropertyMap</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L113">method __@iterator</a>
</h3>

```typescript
__@iterator(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of entries in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L22">method clear</a>
</h3>

```typescript
clear(): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L23">method delete</a>
</h3>

```typescript
delete(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L118">method entries</a>
</h3>

```typescript
entries(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of key, value pairs for every entry in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L24">method forEach</a>
</h3>

```typescript
forEach(callbackfn: { ... }, thisArg?: any): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L25">method get</a>
</h3>

```typescript
get(key: Entry): PropertyInfoAndValue | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L26">method has</a>
</h3>

```typescript
has(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L123">method keys</a>
</h3>

```typescript
keys(): IterableIterator<Entry>
```


Returns an iterable of keys in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L27">method set</a>
</h3>

```typescript
set(key: Entry, value: PropertyInfoAndValue): this
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.iterable.d.ts#L128">method values</a>
</h3>

```typescript
values(): IterableIterator<PropertyInfoAndValue>
```


Returns an iterable of values in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L35">property Map</a>
</h3>

```typescript
Map: MapConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.symbol.wellknown.d.ts#L130">property __@toStringTag</a>
</h3>

```typescript
__@toStringTag: Map;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//home/matell/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es2015.collection.d.ts#L28">property size</a>
</h3>

```typescript
size: number;
```

<h2 class="pdoc-module-header" id="SerializeFunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L22">interface SerializeFunctionArgs</a>
</h2>

SerializeFunctionArgs are arguments used to serialize a JavaScript function

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L26">property exportName</a>
</h3>

```typescript
exportName?: undefined | string;
```


The name to export from the module defined by the generated module text.  Defaults to 'handler'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L43">property isFactoryFunction</a>
</h3>

```typescript
isFactoryFunction?: undefined | false | true;
```


If this is a function which, when invoked, will produce the actual entrypoint function.
Useful for when serializing a function that has high startup cost that only wants to be
run once. The signature of this function should be:  () => (provider_handler_args...) => provider_result

This will then be emitted as: `exports.[exportName] = serialized_func_name();`

In other words, the function will be invoked (once) and the resulting inner function will
be what is exported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L48">property logResource</a>
</h3>

```typescript
logResource?: Resource;
```


The resource to log any errors we encounter against.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L31">property serialize</a>
</h3>

```typescript
serialize?: undefined | { ... };
```


A function to prevent serialization of certain objects captured during the serialization.  Primarily used to
prevent potential cycles.

<h2 class="pdoc-module-header" id="SerializedFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L54">interface SerializedFunction</a>
</h2>

SerializeFunction is a representation of a serialized JavaScript function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L64">property exportName</a>
</h3>

```typescript
exportName: string;
```


The name of the exported module member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L60">property text</a>
</h3>

```typescript
text: string;
```


The text of a JavaScript module which exports a single name bound to an appropriate value.
In the case of a normal function, this value will just be serialized function.  In the case
of a factory function this value will be the result of invoking the factory function.

<h2 class="pdoc-module-header" id="excessiveDebugOutput">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L27">let excessiveDebugOutput</a>
</h2>

```typescript
let excessiveDebugOutput: boolean = false;
```


excessiveDebugOutput enables, well, pretty excessive debug output pertaining to resources and properties.

<h2 class="pdoc-module-header" id="CapturedVariableMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L69">type CapturedVariableMap</a>
</h2>

```typescript
type CapturedVariableMap = Map<string, CapturedPropertyChain[]>;
```

<h2 class="pdoc-module-header" id="OutputResolvers">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L24">type OutputResolvers</a>
</h2>

```typescript
type OutputResolvers = Record<string, { ... }>;
```

