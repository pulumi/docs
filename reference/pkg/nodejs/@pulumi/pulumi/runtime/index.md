---
title: Module runtime
---

<a href="..">@pulumi/pulumi</a>

<h2 class="pdoc-module-header">Index</h2>

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
* <a href="#ensureConfig">function ensureConfig</a>
* <a href="#errorString">function errorString</a>
* <a href="#getConfig">function getConfig</a>
* <a href="#getEngine">function getEngine</a>
* <a href="#getFunctionColumn">function getFunctionColumn</a>
* <a href="#getFunctionFile">function getFunctionFile</a>
* <a href="#getFunctionLine">function getFunctionLine</a>
* <a href="#getMonitor">function getMonitor</a>
* <a href="#getProject">function getProject</a>
* <a href="#getRootResource">function getRootResource</a>
* <a href="#getStack">function getStack</a>
* <a href="#hasMonitor">function hasMonitor</a>
* <a href="#invoke">function invoke</a>
* <a href="#isDryRun">function isDryRun</a>
* <a href="#isLegalFunctionName">function isLegalFunctionName</a>
* <a href="#isLegalMemberName">function isLegalMemberName</a>
* <a href="#lookupCapturedVariableValue">function lookupCapturedVariableValue</a>
* <a href="#parseFunction">function parseFunction</a>
* <a href="#readResource">function readResource</a>
* <a href="#registerResource">function registerResource</a>
* <a href="#registerResourceOutputs">function registerResourceOutputs</a>
* <a href="#resolveProperties">function resolveProperties</a>
* <a href="#rewriteSuperReferences">function rewriteSuperReferences</a>
* <a href="#rpcKeepAlive">function rpcKeepAlive</a>
* <a href="#runInPulumiStack">function runInPulumiStack</a>
* <a href="#serialize">function serialize</a>
* <a href="#serializeFunctionAsync">function serializeFunctionAsync</a>
* <a href="#serializeProperties">function serializeProperties</a>
* <a href="#serializeProperty">function serializeProperty</a>
* <a href="#serializeResourceProperties">function serializeResourceProperties</a>
* <a href="#setConfig">function setConfig</a>
* <a href="#setOptions">function setOptions</a>
* <a href="#setRootResource">function setRootResource</a>
* <a href="#transferProperties">function transferProperties</a>
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
* <a href="#excessiveDebugOutput">let excessiveDebugOutput</a>
* <a href="#CapturedVariableMap">type CapturedVariableMap</a>
* <a href="#OutputResolvers">type OutputResolvers</a>

<a href="/runtime/closure/createClosure.ts">runtime/closure/createClosure.ts</a> <a href="/runtime/closure/parseFunction.ts">runtime/closure/parseFunction.ts</a> <a href="/runtime/closure/rewriteSuper.ts">runtime/closure/rewriteSuper.ts</a> <a href="/runtime/closure/serializeClosure.ts">runtime/closure/serializeClosure.ts</a> <a href="/runtime/closure/v8.ts">runtime/closure/v8.ts</a> <a href="/runtime/config.ts">runtime/config.ts</a> <a href="/runtime/debuggable.ts">runtime/debuggable.ts</a> <a href="/runtime/invoke.ts">runtime/invoke.ts</a> <a href="/runtime/resource.ts">runtime/resource.ts</a> <a href="/runtime/rpc.ts">runtime/rpc.ts</a> <a href="/runtime/settings.ts">runtime/settings.ts</a> <a href="/runtime/stack.ts">runtime/stack.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="rootPulumiStackTypeName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L25">const rootPulumiStackTypeName</a>
</h2>

```typescript
const rootPulumiStackTypeName: pulumi:pulumi:Stack = "pulumi:pulumi:Stack";
```


rootPulumiStackTypeName is the type name that should be used to construct the root component in the tree of Pulumi
resources allocated by a deployment.  This must be kept up to date with
`github.com/pulumi/pulumi/pkg/resource/stack.RootPulumiStackTypeName`.

<h2 class="pdoc-module-header" id="specialArchiveSig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L217">const specialArchiveSig</a>
</h2>

```typescript
const specialArchiveSig: 0def7320c3a5731c473e5ecbe6d01bc7 = "0def7320c3a5731c473e5ecbe6d01bc7";
```


specialArchiveSig is a randomly assigned hash used to identify archives in maps.  See pkg/resource/asset.go.

<h2 class="pdoc-module-header" id="specialAssetSig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L213">const specialAssetSig</a>
</h2>

```typescript
const specialAssetSig: c44067f5952c0a294b673a41bacd8c17 = "c44067f5952c0a294b673a41bacd8c17";
```


specialAssetSig is a randomly assigned hash used to identify assets in maps.  See pkg/resource/asset.go.

<h2 class="pdoc-module-header" id="specialSigKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L209">const specialSigKey</a>
</h2>

```typescript
const specialSigKey: 4dabf18193072939515e22adb298388d = "4dabf18193072939515e22adb298388d";
```


specialSigKey is sometimes used to encode type identity inside of a map.  See pkg/resource/properties.go.

<h2 class="pdoc-module-header" id="unknownValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L205">const unknownValue</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L193">function createFunctionInfoAsync</a>
</h2>

```typescript
createFunctionInfoAsync(func: Function, serialize: { ... }): Promise<FunctionInfo>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L311">function deserializeProperty</a>
</h2>

```typescript
deserializeProperty(prop: any): any
```


deserializeProperty unpacks some special types, reversing the above process.

<h2 class="pdoc-module-header" id="disconnect">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L207">function disconnect</a>
</h2>

```typescript
disconnect(): void
```


disconnect permanently disconnects from the server, closing the connections.  It waits for the existing RPC
queue to drain.  If any RPCs come in afterwards, however, they will crash the process.

<h2 class="pdoc-module-header" id="disconnectSync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L225">function disconnectSync</a>
</h2>

```typescript
disconnectSync(): void
```


disconnectSync permanently disconnects from the server, closing the connections. Unlike `disconnect`. it does not
wait for the existing RPC queue to drain. Any RPCs that come in after this call will crash the process.

<h2 class="pdoc-module-header" id="ensureConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L54">function ensureConfig</a>
</h2>

```typescript
ensureConfig(): void
```


ensureConfig populates the runtime.config object based on configuration set in the environment.

<h2 class="pdoc-module-header" id="errorString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L99">function errorString</a>
</h2>

```typescript
errorString(err: Error): string
```


errorString produces a string from an error, conditionally including additional diagnostics.

<h2 class="pdoc-module-header" id="getConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L41">function getConfig</a>
</h2>

```typescript
getConfig(k: string): string | undefined
```


getConfig returns a configuration variable's value or undefined if it is unset.

<h2 class="pdoc-module-header" id="getEngine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L119">function getEngine</a>
</h2>

```typescript
getEngine(): Object | undefined
```


getEngine returns the current engine, if any, for RPC communications back to the resource engine.

<h2 class="pdoc-module-header" id="getFunctionColumn">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L151">function getFunctionColumn</a>
</h2>

```typescript
getFunctionColumn(func: Function): number
```


Given a function, returns the column in the file where this function was defined.
Returns 0 if the given function has no script.

<h2 class="pdoc-module-header" id="getFunctionFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L127">function getFunctionFile</a>
</h2>

```typescript
getFunctionFile(func: Function): string
```


Given a function, returns the name of the file where this function was defined.
Returns the empty string if the given function has no Script. (e.g. a native function)

<h2 class="pdoc-module-header" id="getFunctionLine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L136">function getFunctionLine</a>
</h2>

```typescript
getFunctionLine(func: Function): number
```


Given a function, returns the line number in the file where this function was defined.
Returns 0 if the given function has no Script.

<h2 class="pdoc-module-header" id="getMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L96">function getMonitor</a>
</h2>

```typescript
getMonitor(): Object
```


getMonitor returns the current resource monitoring service client for RPC communications.

<h2 class="pdoc-module-header" id="getProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L70">function getProject</a>
</h2>

```typescript
getProject(): string | undefined
```


Get the project being run by the current update.

<h2 class="pdoc-module-header" id="getRootResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L269">function getRootResource</a>
</h2>

```typescript
getRootResource(): Resource | undefined
```


getRootResource returns a root resource that will automatically become the default parent of all resources.  This
can be used to ensure that all resources without explicit parents are parented to a common parent resource.

<h2 class="pdoc-module-header" id="getStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L77">function getStack</a>
</h2>

```typescript
getStack(): string | undefined
```


Get the stack being targeted by the current update.

<h2 class="pdoc-module-header" id="hasMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L89">function hasMonitor</a>
</h2>

```typescript
hasMonitor(): boolean
```


hasMonitor returns true if we are currently connected to a resource monitoring service.

<h2 class="pdoc-module-header" id="invoke">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L30">function invoke</a>
</h2>

```typescript
invoke(tok: string, props: Inputs): Promise<any>
```


invoke dynamically invokes the function, tok, which is offered by a provider plugin.  The inputs
can be a bag of computed values (Ts or Promise<T>s), and the result is a Promise<any> that
resolves when the invoke finishes.

<h2 class="pdoc-module-header" id="isDryRun">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L63">function isDryRun</a>
</h2>

```typescript
isDryRun(): boolean
```


Returns true if we're currently performing a dry-run, or false if this is a true update.

<h2 class="pdoc-module-header" id="isLegalFunctionName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L1019">function isLegalFunctionName</a>
</h2>

```typescript
isLegalFunctionName(n: string): boolean
```

<h2 class="pdoc-module-header" id="isLegalMemberName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L1015">function isLegalMemberName</a>
</h2>

```typescript
isLegalMemberName(n: string): boolean
```

<h2 class="pdoc-module-header" id="lookupCapturedVariableValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L105">function lookupCapturedVariableValue</a>
</h2>

```typescript
lookupCapturedVariableValue(func: Function, freeVariable: string, throwOnFailure: boolean): any
```


Given a function and a free variable name, lookupCapturedVariableValue looks up the value of that free variable
in the scope chain of the provided function. If the free variable is not found, `throwOnFailure` indicates
whether or not this function should throw or return `undefined.

<h2 class="pdoc-module-header" id="parseFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L81">function parseFunction</a>
</h2>

```typescript
parseFunction(funcString: string): [, string, ParsedFunction]
```

<h2 class="pdoc-module-header" id="readResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L53">function readResource</a>
</h2>

```typescript
readResource(res: Resource, t: string, name: string, props: Inputs, opts: ResourceOptions): void
```


Reads an existing custom resource's state from the resource monitor.  Note that resources read in this way
will not be part of the resulting stack's state, as they are presumed to belong to another.

<h2 class="pdoc-module-header" id="registerResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L105">function registerResource</a>
</h2>

```typescript
registerResource(res: Resource, t: string, name: string, custom: boolean, props: Inputs, opts: ResourceOptions): void
```


registerResource registers a new resource object with a given type t and name.  It returns the auto-generated
URN and the ID that will resolve after the deployment has completed.  All properties will be initialized to property
objects that the registration operation will resolve at the right time (or remain unresolved for deployments).

<h2 class="pdoc-module-header" id="registerResourceOutputs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L265">function registerResourceOutputs</a>
</h2>

```typescript
registerResourceOutputs(res: Resource, outputs: Inputs): void
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/rewriteSuper.ts#L18">function rewriteSuperReferences</a>
</h2>

```typescript
rewriteSuperReferences(code: string, isStatic: boolean): string
```

<h2 class="pdoc-module-header" id="rpcKeepAlive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L256">function rpcKeepAlive</a>
</h2>

```typescript
rpcKeepAlive(): { ... }
```


rpcKeepAlive registers a pending call to ensure that we don't prematurely disconnect from the server.  It returns
a function that, when invoked, signals that the RPC has completed.

<h2 class="pdoc-module-header" id="runInPulumiStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L31">function runInPulumiStack</a>
</h2>

```typescript
runInPulumiStack(init: { ... }): void
```


runInPulumiStack creates a new Pulumi stack resource and executes the callback inside of it.  Any outputs
returned by the callback will be stored as output properties on this resulting Stack object.

<h2 class="pdoc-module-header" id="serialize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L133">function serialize</a>
</h2>

```typescript
serialize(): boolean
```


serialize returns true if resource operations should be serialized.

<h2 class="pdoc-module-header" id="serializeFunctionAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L17">function serializeFunctionAsync</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L223">function serializeProperty</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L33">function setConfig</a>
</h2>

```typescript
setConfig(k: string, v: string): void
```


setConfig sets a configuration variable.

<h2 class="pdoc-module-header" id="setOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L142">function setOptions</a>
</h2>

```typescript
setOptions(opts: Options): void
```


setOptions initializes the current runtime with information about whether we are performing a "dry
run" (preview), versus a real deployment, RPC addresses, and so on.   It may only be called once.

<h2 class="pdoc-module-header" id="setRootResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L276">function setRootResource</a>
</h2>

```typescript
setRootResource(res: Resource | undefined): void
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

<h2 class="pdoc-module-header" id="CapturedPropertyInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L48">interface CapturedPropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L50">property invoked</a>
</h3>

```typescript
invoked: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L49">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="CapturedVariables">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L59">interface CapturedVariables</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L61">property optional</a>
</h3>

```typescript
optional: CapturedVariableMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L60">property required</a>
</h3>

```typescript
required: CapturedVariableMap;
```

<h2 class="pdoc-module-header" id="Entry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L84">interface Entry</a>
</h2>

Entry is the environment slot for a named lexically captured variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L96">property array</a>
</h3>

```typescript
array?: Entry[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L107">property expr</a>
</h3>

```typescript
expr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L89">property function</a>
</h3>

```typescript
function?: FunctionInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L86">property json</a>
</h3>

```typescript
json?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L93">property object</a>
</h3>

```typescript
object?: ObjectInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L104">property output</a>
</h3>

```typescript
output?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L100">property promise</a>
</h3>

```typescript
promise?: Entry;
```

<h2 class="pdoc-module-header" id="FunctionInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L37">interface FunctionInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L42">property capturedValues</a>
</h3>

```typescript
capturedValues: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L39">property code</a>
</h3>

```typescript
code: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L32">property env</a>
</h3>

```typescript
env: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L49">property name</a>
</h3>

```typescript
name: string | undefined;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L28">property proto</a>
</h3>

```typescript
proto?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L45">property usesNonLexicalThis</a>
</h3>

```typescript
usesNonLexicalThis: boolean;
```

<h2 class="pdoc-module-header" id="ObjectInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L24">interface ObjectInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L32">property env</a>
</h3>

```typescript
env: PropertyMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L28">property proto</a>
</h3>

```typescript
proto?: Entry;
```

<h2 class="pdoc-module-header" id="Options">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L33">interface Options</a>
</h2>

Options is a bag of settings that controls the behavior of previews and deployments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L36">property dryRun</a>
</h3>

```typescript
dryRun?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L38">property engineAddr</a>
</h3>

```typescript
engineAddr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L39">property monitorAddr</a>
</h3>

```typescript
monitorAddr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L37">property parallel</a>
</h3>

```typescript
parallel?: undefined | number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L34">property project</a>
</h3>

```typescript
project?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L35">property stack</a>
</h3>

```typescript
stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="ParsedFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L38">interface ParsedFunction</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L40">property capturedVariables</a>
</h3>

```typescript
capturedVariables: CapturedVariables;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L26">property funcExprWithName</a>
</h3>

```typescript
funcExprWithName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L22">property funcExprWithoutName</a>
</h3>

```typescript
funcExprWithoutName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L32">property functionDeclarationName</a>
</h3>

```typescript
functionDeclarationName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L35">property isArrowFunction</a>
</h3>

```typescript
isArrowFunction: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L43">property usesNonLexicalThis</a>
</h3>

```typescript
usesNonLexicalThis: boolean;
```

<h2 class="pdoc-module-header" id="ParsedFunctionCode">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L19">interface ParsedFunctionCode</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L26">property funcExprWithName</a>
</h3>

```typescript
funcExprWithName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L22">property funcExprWithoutName</a>
</h3>

```typescript
funcExprWithoutName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L32">property functionDeclarationName</a>
</h3>

```typescript
functionDeclarationName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L35">property isArrowFunction</a>
</h3>

```typescript
isArrowFunction: boolean;
```

<h2 class="pdoc-module-header" id="PropertyInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L54">interface PropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L59">property configurable</a>
</h3>

```typescript
configurable?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L60">property enumerable</a>
</h3>

```typescript
enumerable?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L65">property get</a>
</h3>

```typescript
get?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L56">property hasValue</a>
</h3>

```typescript
hasValue: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L66">property set</a>
</h3>

```typescript
set?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L61">property writable</a>
</h3>

```typescript
writable?: undefined | true | false;
```

<h2 class="pdoc-module-header" id="PropertyInfoAndValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L71">interface PropertyInfoAndValue</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L73">property entry</a>
</h3>

```typescript
entry: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L72">property info</a>
</h3>

```typescript
info?: PropertyInfo;
```

<h2 class="pdoc-module-header" id="PropertyMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L78">interface PropertyMap</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4874">method __@iterator</a>
</h3>

```typescript
__@iterator(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of entries in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4655">method clear</a>
</h3>

```typescript
clear(): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4656">method delete</a>
</h3>

```typescript
delete(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4879">method entries</a>
</h3>

```typescript
entries(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of key, value pairs for every entry in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4657">method forEach</a>
</h3>

```typescript
forEach(callbackfn: { ... }, thisArg?: any): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4658">method get</a>
</h3>

```typescript
get(key: Entry): PropertyInfoAndValue | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4659">method has</a>
</h3>

```typescript
has(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4884">method keys</a>
</h3>

```typescript
keys(): IterableIterator<Entry>
```


Returns an iterable of keys in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4660">method set</a>
</h3>

```typescript
set(key: Entry, value: PropertyInfoAndValue): this
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4889">method values</a>
</h3>

```typescript
values(): IterableIterator<PropertyInfoAndValue>
```


Returns an iterable of values in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4669">property Map</a>
</h3>

```typescript
Map: MapConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L5648">property __@toStringTag</a>
</h3>

```typescript
__@toStringTag: Map;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/node_modules/typedoc/node_modules/typescript/lib/lib.es6.d.ts#L4661">property size</a>
</h3>

```typescript
size: number;
```

<h2 class="pdoc-module-header" id="excessiveDebugOutput">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L28">let excessiveDebugOutput</a>
</h2>

```typescript
let excessiveDebugOutput: boolean = false;
```


excessiveDebugOutput enables, well, pretty excessive debug output pertaining to resources and properties.

<h2 class="pdoc-module-header" id="CapturedVariableMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L53">type CapturedVariableMap</a>
</h2>

```typescript
type CapturedVariableMap = Map<string, CapturedPropertyInfo[]>;
```

<h2 class="pdoc-module-header" id="OutputResolvers">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L24">type OutputResolvers</a>
</h2>

```typescript
type OutputResolvers = Record<string, { ... }>;
```

