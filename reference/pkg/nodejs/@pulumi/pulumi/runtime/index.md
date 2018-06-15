---
title: Module runtime
---

<a href="../index.html">@pulumi/pulumi</a> &gt; runtime

<h2 class="pdoc-module-header">Index</h2>

* <a href="#SerializedOutput">class SerializedOutput</a>
* <a href="#Stack">class Stack</a>
* <a href="#builtInModuleNames">const builtInModuleNames</a>
* <a href="#builtInModules">const builtInModules</a>
* <a href="#config">const config</a>
* <a href="#configEnvKey">const configEnvKey</a>
* <a href="#debugPromiseLeaks">const debugPromiseLeaks</a>
* <a href="#engrpc">const engrpc</a>
* <a href="#getFunctionScopeCount">const getFunctionScopeCount</a>
* <a href="#getFunctionScopeDetails">const getFunctionScopeDetails</a>
* <a href="#getScript">const getScript</a>
* <a href="#getSourcePosition">const getSourcePosition</a>
* <a href="#grpc">const grpc</a>
* <a href="#gstruct">const gstruct</a>
* <a href="#leakCandidates">const leakCandidates</a>
* <a href="#legalNameRegex">const legalNameRegex</a>
* <a href="#makeLegalRegex">const makeLegalRegex</a>
* <a href="#nodeModuleGlobals">const nodeModuleGlobals</a>
* <a href="#resproto">const resproto</a>
* <a href="#resrpc">const resrpc</a>
* <a href="#rootPulumiStackTypeName">const rootPulumiStackTypeName</a>
* <a href="#specialArchiveSig">const specialArchiveSig</a>
* <a href="#specialAssetSig">const specialAssetSig</a>
* <a href="#specialSigKey">const specialSigKey</a>
* <a href="#unknownValue">const unknownValue</a>
* <a href="#V8ScopeDetailsFields">enum V8ScopeDetailsFields</a>
* <a href="#allConfig">function allConfig</a>
* <a href="#cleanKey">function cleanKey</a>
* <a href="#computeCapturedVariableNames">function computeCapturedVariableNames</a>
* <a href="#computeUsesNonLexicalThis">function computeUsesNonLexicalThis</a>
* <a href="#createFunctionInfo">function createFunctionInfo</a>
* <a href="#createFunctionInfoAsync">function createFunctionInfoAsync</a>
* <a href="#createSourceFile">function createSourceFile</a>
* <a href="#debuggablePromise">function debuggablePromise</a>
* <a href="#deepContainsObjOrArray">function deepContainsObjOrArray</a>
* <a href="#deserializeProperties">function deserializeProperties</a>
* <a href="#deserializeProperty">function deserializeProperty</a>
* <a href="#disconnect">function disconnect</a>
* <a href="#disconnectSync">function disconnectSync</a>
* <a href="#ensureConfig">function ensureConfig</a>
* <a href="#envObjToString">function envObjToString</a>
* <a href="#errorString">function errorString</a>
* <a href="#findModuleName">function findModuleName</a>
* <a href="#getConfig">function getConfig</a>
* <a href="#getEngine">function getEngine</a>
* <a href="#getFunctionColumn">function getFunctionColumn</a>
* <a href="#getFunctionFile">function getFunctionFile</a>
* <a href="#getFunctionLine">function getFunctionLine</a>
* <a href="#getFunctionLocation">function getFunctionLocation</a>
* <a href="#getFunctionName">function getFunctionName</a>
* <a href="#getMonitor">function getMonitor</a>
* <a href="#getOrCreateEntry">function getOrCreateEntry</a>
* <a href="#getOwnPropertyNamesAndSymbols">function getOwnPropertyNamesAndSymbols</a>
* <a href="#getProject">function getProject</a>
* <a href="#getRootResource">function getRootResource</a>
* <a href="#getScopeForFunction">function getScopeForFunction</a>
* <a href="#getStack">function getStack</a>
* <a href="#hasMonitor">function hasMonitor</a>
* <a href="#hasNonNumericIndices">function hasNonNumericIndices</a>
* <a href="#invoke">function invoke</a>
* <a href="#isAwaiterCall">function isAwaiterCall</a>
* <a href="#isDefaultFunctionPrototype">function isDefaultFunctionPrototype</a>
* <a href="#isDerivedNoCaptureConstructor">function isDerivedNoCaptureConstructor</a>
* <a href="#isDryRun">function isDryRun</a>
* <a href="#isLegalFunctionName">function isLegalFunctionName</a>
* <a href="#isLegalMemberName">function isLegalMemberName</a>
* <a href="#isNumeric">function isNumeric</a>
* <a href="#isObjOrArray">function isObjOrArray</a>
* <a href="#isSparse">function isSparse</a>
* <a href="#loadOptions">function loadOptions</a>
* <a href="#lookupCapturedVariableValue">function lookupCapturedVariableValue</a>
* <a href="#makeLegalJSName">function makeLegalJSName</a>
* <a href="#options">function options</a>
* <a href="#parseFunction">function parseFunction</a>
* <a href="#parseFunctionCode">function parseFunctionCode</a>
* <a href="#prepareResource">function prepareResource</a>
* <a href="#promiseDebugString">function promiseDebugString</a>
* <a href="#readResource">function readResource</a>
* <a href="#registerResource">function registerResource</a>
* <a href="#registerResourceOutputs">function registerResourceOutputs</a>
* <a href="#resolveOutputs">function resolveOutputs</a>
* <a href="#resolveProperties">function resolveProperties</a>
* <a href="#rewriteSuperReferences">function rewriteSuperReferences</a>
* <a href="#rpcKeepAlive">function rpcKeepAlive</a>
* <a href="#runAsyncResourceOp">function runAsyncResourceOp</a>
* <a href="#runInPulumiStack">function runInPulumiStack</a>
* <a href="#serialize">function serialize</a>
* <a href="#serializeFilteredProperties">function serializeFilteredProperties</a>
* <a href="#serializeFunction">function serializeFunction</a>
* <a href="#serializeFunctionAsync">function serializeFunctionAsync</a>
* <a href="#serializeJavaScriptText">function serializeJavaScriptText</a>
* <a href="#serializeProperties">function serializeProperties</a>
* <a href="#serializeProperty">function serializeProperty</a>
* <a href="#serializeResourceProperties">function serializeResourceProperties</a>
* <a href="#setConfig">function setConfig</a>
* <a href="#setOptions">function setOptions</a>
* <a href="#setRootResource">function setRootResource</a>
* <a href="#throwSerializationError">function throwSerializationError</a>
* <a href="#transferProperties">function transferProperties</a>
* <a href="#waitForDeath">function waitForDeath</a>
* <a href="#CapturedPropertyInfo">interface CapturedPropertyInfo</a>
* <a href="#CapturedVariables">interface CapturedVariables</a>
* <a href="#Context">interface Context</a>
* <a href="#ContextFrame">interface ContextFrame</a>
* <a href="#Entry">interface Entry</a>
* <a href="#FunctionInfo">interface FunctionInfo</a>
* <a href="#FunctionLocation">interface FunctionLocation</a>
* <a href="#ObjectInfo">interface ObjectInfo</a>
* <a href="#Options">interface Options</a>
* <a href="#ParsedFunction">interface ParsedFunction</a>
* <a href="#ParsedFunctionCode">interface ParsedFunctionCode</a>
* <a href="#PropertyInfo">interface PropertyInfo</a>
* <a href="#PropertyInfoAndValue">interface PropertyInfoAndValue</a>
* <a href="#PropertyMap">interface PropertyMap</a>
* <a href="#ResourceResolverOperation">interface ResourceResolverOperation</a>
* <a href="#SerializeFunctionArgs">interface SerializeFunctionArgs</a>
* <a href="#SerializedFunction">interface SerializedFunction</a>
* <a href="#V8ScopeDetails">interface V8ScopeDetails</a>
* <a href="#V8Script">interface V8Script</a>
* <a href="#V8SourceLocation">interface V8SourceLocation</a>
* <a href="#V8SourcePosition">interface V8SourcePosition</a>
* <a href="#_options">let _options</a>
* <a href="#engine">let engine</a>
* <a href="#excessiveDebugOutput">let excessiveDebugOutput</a>
* <a href="#leakDetectorScheduled">let leakDetectorScheduled</a>
* <a href="#loaded">let loaded</a>
* <a href="#monitor">let monitor</a>
* <a href="#resourceChain">let resourceChain</a>
* <a href="#resourceChainLabel">let resourceChainLabel</a>
* <a href="#rootResource">let rootResource</a>
* <a href="#rpcDone">let rpcDone</a>
* <a href="#CapturedVariableMap">type CapturedVariableMap</a>
* <a href="#OutputResolvers">type OutputResolvers</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts">runtime/closure/createClosure.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts">runtime/closure/parseFunction.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/rewriteSuper.ts">runtime/closure/rewriteSuper.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts">runtime/closure/serializeClosure.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts">runtime/closure/v8.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts">runtime/config.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts">runtime/debuggable.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts">runtime/invoke.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts">runtime/resource.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts">runtime/rpc.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts">runtime/settings.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts">runtime/stack.ts</a> 


<h2 class="pdoc-module-header" id="SerializedOutput">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L172">class SerializedOutput</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L176">constructor</a>
</h3>

```typescript
public new SerializedOutput(value: T)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L182">method apply</a>
</h3>

```typescript
public apply<U>(func: { ... }): resource.Output<U>
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L187">method get</a>
</h3>

```typescript
public get(): T
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L173">property isKnown</a>
</h3>

```typescript
public isKnown: Promise<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L174">property promise</a>
</h3>

```typescript
public promise: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L175">property resources</a>
</h3>

```typescript
public resources: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L176">property value</a>
</h3>

```typescript
private value: T;
```

<h2 class="pdoc-module-header" id="Stack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L35">class Stack</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/stack.ts#L35">constructor</a>
</h3>

```typescript
new Stack(init: { ... })
```

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

<h2 class="pdoc-module-header" id="builtInModuleNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L983">const builtInModuleNames</a>
</h2>

```typescript
const builtInModuleNames: string[] =  [
    "assert", "buffer", "child_process", "cluster", "console", "constants", "crypto",
    "dgram", "dns", "domain", "events", "fs", "http", "https", "module", "net", "os",
    "path", "process", "punycode", "querystring", "readline", "repl", "stream", "string_decoder",
    /* "sys" deprecated ,*/ "timers", "tls", "tty", "url", "util", "v8", "vm", "zlib",
];
```

<h2 class="pdoc-module-header" id="builtInModules">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L989">const builtInModules</a>
</h2>

```typescript
const builtInModules: Map<any, string> =  new Map<any, string>();
```

<h2 class="pdoc-module-header" id="config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L20">const config</a>
</h2>

```typescript
const config: { ... };
```

<h2 class="pdoc-module-header" id="configEnvKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L18">const configEnvKey</a>
</h2>

```typescript
const configEnvKey: PULUMI_CONFIG = "PULUMI_CONFIG";
```


configEnvKey is the environment variable key that the language plugin uses to set configuration values.

<h2 class="pdoc-module-header" id="debugPromiseLeaks">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L20">const debugPromiseLeaks</a>
</h2>

```typescript
const debugPromiseLeaks: boolean =  !!process.env.PULUMI_DEBUG_PROMISE_LEAKS;
```


debugPromiseLeaks can be set to enable promises leaks debugging.

<h2 class="pdoc-module-header" id="engrpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L22">const engrpc</a>
</h2>

```typescript
const engrpc: any =  require("../proto/engine_grpc_pb.js");
```

<h2 class="pdoc-module-header" id="getFunctionScopeCount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L65">const getFunctionScopeCount</a>
</h2>

```typescript
const getFunctionScopeCount: { ... } = 
    new Function("func", "return %GetFunctionScopeCount(func);") as any;
```

<h2 class="pdoc-module-header" id="getFunctionScopeDetails">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L63">const getFunctionScopeDetails</a>
</h2>

```typescript
const getFunctionScopeDetails: { ... } = 
    new Function("func", "index", "return %GetFunctionScopeDetails(func, index);") as any;
```

<h2 class="pdoc-module-header" id="getScript">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L28">const getScript</a>
</h2>

```typescript
const getScript: { ... } = 
    // The use of the Function constructor here and elsewhere in this file is because
    // because V8 intrinsics are not valid JavaScript identifiers; they all begin with '%',
    // which means that the TypeScript compiler issues errors for them.
    new Function("func", "return %FunctionGetScript(func);") as any;
```

<h2 class="pdoc-module-header" id="getSourcePosition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L45">const getSourcePosition</a>
</h2>

```typescript
const getSourcePosition: { ... } = 
    new Function("func", "return %FunctionGetScriptSourcePosition(func);") as any;
```

<h2 class="pdoc-module-header" id="grpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L21">const grpc</a>
</h2>

```typescript
const grpc: any =  require("grpc");
```

<h2 class="pdoc-module-header" id="gstruct">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L22">const gstruct</a>
</h2>

```typescript
const gstruct: any =  require("google-protobuf/google/protobuf/struct_pb.js");
```

<h2 class="pdoc-module-header" id="leakCandidates">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L29">const leakCandidates</a>
</h2>

```typescript
const leakCandidates: Set<Promise<any>> =  new Set<Promise<any>>();
```


leakCandidates tracks the list of potential leak candidates.

<h2 class="pdoc-module-header" id="legalNameRegex">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L1020">const legalNameRegex</a>
</h2>

```typescript
const legalNameRegex: RegExp =  /^[a-zA-Z_][0-9a-zA-Z_]*$/;
```

<h2 class="pdoc-module-header" id="makeLegalRegex">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L442">const makeLegalRegex</a>
</h2>

```typescript
const makeLegalRegex: RegExp =  /[^0-9a-zA-Z_]/g;
```

<h2 class="pdoc-module-header" id="nodeModuleGlobals">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L72">const nodeModuleGlobals</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L73">let __dirname</a>
</h3>

```typescript
let __dirname: true = true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L74">let __filename</a>
</h3>

```typescript
let __filename: true = true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L78">let require</a>
</h3>

```typescript
let require: true = true;
```

<h2 class="pdoc-module-header" id="resproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L23">const resproto</a>
</h2>

```typescript
const resproto: any =  require("../proto/resource_pb.js");
```

<h2 class="pdoc-module-header" id="resrpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L23">const resrpc</a>
</h2>

```typescript
const resrpc: any =  require("../proto/resource_grpc_pb.js");
```

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

<h2 class="pdoc-module-header" id="V8ScopeDetailsFields">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L70">enum V8ScopeDetailsFields</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L75">enum member kScopeDetailsEndPositionIndex</a>
</h3>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L76">enum member kScopeDetailsFunctionIndex</a>
</h3>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L73">enum member kScopeDetailsNameIndex</a>
</h3>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L72">enum member kScopeDetailsObjectIndex</a>
</h3>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L74">enum member kScopeDetailsStartPositionIndex</a>
</h3>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L71">enum member kScopeDetailsTypeIndex</a>
</h3>
<h2 class="pdoc-module-header" id="allConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L25">function allConfig</a>
</h2>

```typescript
allConfig(): { ... }
```


allConfig returns a copy of the full config map.

<h2 class="pdoc-module-header" id="cleanKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L74">function cleanKey</a>
</h2>

```typescript
cleanKey(key: string): string
```


cleanKey takes a configuration key, and if it is of the form "<string>:config:<string>" removes the ":config:"
portion. Previously, our keys always had the string ":config:" in them, and we'd like to remove it. However, the
language host needs to continue to set it so we can be compatable with older versions of our packages. Once we
stop supporting older packages, we can change the language host to not add this :config: thing and remove this
function.

<h2 class="pdoc-module-header" id="computeCapturedVariableNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L364">function computeCapturedVariableNames</a>
</h2>

```typescript
computeCapturedVariableNames(file: SourceFile): CapturedVariables
```


computeCapturedVariableNames computes the set of free variables in a given function string.  Note that this string is
expected to be the usual V8-serialized function expression text.

<h2 class="pdoc-module-header" id="computeUsesNonLexicalThis">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L281">function computeUsesNonLexicalThis</a>
</h2>

```typescript
computeUsesNonLexicalThis(file: SourceFile): boolean
```

<h2 class="pdoc-module-header" id="createFunctionInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L312">function createFunctionInfo</a>
</h2>

```typescript
createFunctionInfo(func: Function, context: Context, serialize: { ... }): FunctionInfo
```


createFunctionInfo does the work to create an asynchronous dataflow graph that resolves to a
final FunctionInfo.

<h2 class="pdoc-module-header" id="createFunctionInfoAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L198">function createFunctionInfoAsync</a>
</h2>

```typescript
createFunctionInfoAsync(func: Function, serialize: { ... }): Promise<FunctionInfo>
```


createFunctionInfo serializes a function and its closure environment into a form that is
amenable to persistence as simple JSON.  Like toString, it includes the full text of the
function's source code, suitable for execution. Unlike toString, it actually includes information
about the captured environment.

<h2 class="pdoc-module-header" id="createSourceFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L262">function createSourceFile</a>
</h2>

```typescript
createSourceFile(serializedFunction: ParsedFunctionCode): [, string, SourceFile | null]
```

<h2 class="pdoc-module-header" id="debuggablePromise">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L40">function debuggablePromise</a>
</h2>

```typescript
debuggablePromise<T>(p: Promise<T>, ctx?: any): Promise<T>
```


debuggablePromise optionally wraps a promise with some goo to make it easier to debug common problems.

<h2 class="pdoc-module-header" id="deepContainsObjOrArray">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L466">function deepContainsObjOrArray</a>
</h2>

```typescript
deepContainsObjOrArray(env: closure.Entry): boolean
```

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

<h2 class="pdoc-module-header" id="envObjToString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L480">function envObjToString</a>
</h2>

```typescript
envObjToString(envObj: Record<string, string>): string
```


Converts an environment object into a string which can be embedded into a serialized function
body.  Note that this is not JSON serialization, as we may have property values which are
variable references to other global functions. In other words, there can be free variables in the
resulting object literal.

<h2 class="pdoc-module-header" id="errorString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L99">function errorString</a>
</h2>

```typescript
errorString(err: Error): string
```


errorString produces a string from an error, conditionally including additional diagnostics.

<h2 class="pdoc-module-header" id="findModuleName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L996">function findModuleName</a>
</h2>

```typescript
findModuleName(obj: any): string | undefined
```

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

<h2 class="pdoc-module-header" id="getFunctionLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L641">function getFunctionLocation</a>
</h2>

```typescript
getFunctionLocation(loc: FunctionLocation): string
```

<h2 class="pdoc-module-header" id="getFunctionName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L651">function getFunctionName</a>
</h2>

```typescript
getFunctionName(loc: FunctionLocation): string
```

<h2 class="pdoc-module-header" id="getMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L96">function getMonitor</a>
</h2>

```typescript
getMonitor(): Object
```


getMonitor returns the current resource monitoring service client for RPC communications.

<h2 class="pdoc-module-header" id="getOrCreateEntry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L697">function getOrCreateEntry</a>
</h2>

```typescript
getOrCreateEntry(obj: any, capturedObjectProperties: CapturedPropertyInfo[] | undefined, context: Context, serialize: { ... }): Entry
```


serializeAsync serializes an object, deeply, into something appropriate for an environment
entry.  If propNames is provided, and is non-empty, then only attempt to serialize out those
specific properties.  If propNames is not provided, or is empty, serialize out all properties.

<h2 class="pdoc-module-header" id="getOwnPropertyNamesAndSymbols">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L558">function getOwnPropertyNamesAndSymbols</a>
</h2>

```typescript
getOwnPropertyNamesAndSymbols(obj: any): string | symbol[]
```

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

<h2 class="pdoc-module-header" id="getScopeForFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L88">function getScopeForFunction</a>
</h2>

```typescript
getScopeForFunction(func: Function, index: number): V8ScopeDetails
```

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

<h2 class="pdoc-module-header" id="hasNonNumericIndices">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L454">function hasNonNumericIndices</a>
</h2>

```typescript
hasNonNumericIndices<T>(arr: Array<T>): boolean
```

<h2 class="pdoc-module-header" id="invoke">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L30">function invoke</a>
</h2>

```typescript
invoke(tok: string, props: Inputs): Promise<any>
```


invoke dynamically invokes the function, tok, which is offered by a provider plugin.  The inputs
can be a bag of computed values (Ts or Promise<T>s), and the result is a Promise<any> that
resolves when the invoke finishes.

<h2 class="pdoc-module-header" id="isAwaiterCall">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L801">function isAwaiterCall</a>
</h2>

```typescript
isAwaiterCall(node: CallExpression): boolean
```

<h2 class="pdoc-module-header" id="isDefaultFunctionPrototype">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L681">function isDefaultFunctionPrototype</a>
</h2>

```typescript
isDefaultFunctionPrototype(func: Function, prototypeProp: any): boolean
```

<h2 class="pdoc-module-header" id="isDerivedNoCaptureConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L969">function isDerivedNoCaptureConstructor</a>
</h2>

```typescript
isDerivedNoCaptureConstructor(func: Function): boolean
```

<h2 class="pdoc-module-header" id="isDryRun">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L63">function isDryRun</a>
</h2>

```typescript
isDryRun(): boolean
```


Returns true if we're currently performing a dry-run, or false if this is a true update.

<h2 class="pdoc-module-header" id="isLegalFunctionName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L1025">function isLegalFunctionName</a>
</h2>

```typescript
isLegalFunctionName(n: string): boolean
```

<h2 class="pdoc-module-header" id="isLegalMemberName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L1021">function isLegalMemberName</a>
</h2>

```typescript
isLegalMemberName(n: string): boolean
```

<h2 class="pdoc-module-header" id="isNumeric">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L458">function isNumeric</a>
</h2>

```typescript
isNumeric(n: string): boolean
```

<h2 class="pdoc-module-header" id="isObjOrArray">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L462">function isObjOrArray</a>
</h2>

```typescript
isObjOrArray(env: closure.Entry): boolean
```

<h2 class="pdoc-module-header" id="isSparse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L447">function isSparse</a>
</h2>

```typescript
isSparse<T>(arr: Array<T>): boolean
```

<h2 class="pdoc-module-header" id="loadOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L175">function loadOptions</a>
</h2>

```typescript
loadOptions(): Options
```


loadOptions recovers previously configured options in the case that a copy of the runtime SDK library
is loaded without going through the entry point shim, as happens when multiple copies are loaded.

<h2 class="pdoc-module-header" id="lookupCapturedVariableValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L105">function lookupCapturedVariableValue</a>
</h2>

```typescript
lookupCapturedVariableValue(func: Function, freeVariable: string, throwOnFailure: boolean): any
```


Given a function and a free variable name, lookupCapturedVariableValue looks up the value of that free variable
in the scope chain of the provided function. If the free variable is not found, `throwOnFailure` indicates
whether or not this function should throw or return `undefined.

<h2 class="pdoc-module-header" id="makeLegalJSName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L443">function makeLegalJSName</a>
</h2>

```typescript
makeLegalJSName(n: string): string
```

<h2 class="pdoc-module-header" id="options">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L50">function options</a>
</h2>

```typescript
options(): Options
```


options fetches the current configured options and, if required, lazily initializes them.

<h2 class="pdoc-module-header" id="parseFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L85">function parseFunction</a>
</h2>

```typescript
parseFunction(funcString: string): [, string, ParsedFunction]
```

<h2 class="pdoc-module-header" id="parseFunctionCode">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L120">function parseFunctionCode</a>
</h2>

```typescript
parseFunctionCode(funcString: string): [, string, ParsedFunctionCode]
```

<h2 class="pdoc-module-header" id="prepareResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L165">function prepareResource</a>
</h2>

```typescript
prepareResource(label: string, res: Resource, custom: boolean, props: Inputs, opts: ResourceOptions): Promise<ResourceResolverOperation>
```


Prepares for an RPC that will manufacture a resource, and hence deals with input and output properties.

<h2 class="pdoc-module-header" id="promiseDebugString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L31">function promiseDebugString</a>
</h2>

```typescript
promiseDebugString(p: Promise<any>): string
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

<h2 class="pdoc-module-header" id="resolveOutputs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L236">function resolveOutputs</a>
</h2>

```typescript
resolveOutputs(res: Resource, t: string, name: string, props: Inputs, outputs: any, resolvers: OutputResolvers): Promise<void>
```


Finishes a resource creation RPC operation by resolving its outputs to the resulting RPC payload.

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

<h2 class="pdoc-module-header" id="runAsyncResourceOp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L320">function runAsyncResourceOp</a>
</h2>

```typescript
runAsyncResourceOp(label: string, callback: { ... }, serial?: undefined | true | false): void
```

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

<h2 class="pdoc-module-header" id="serializeFilteredProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/rpc.ts#L77">function serializeFilteredProperties</a>
</h2>

```typescript
serializeFilteredProperties(label: string, props: Inputs, acceptKey: { ... }, dependentResources: Resource[]): Promise<Record<string, any>>
```


serializeFilteredProperties walks the props object passed in, awaiting all interior promises for propertoes with
keys that match the provided filter, creating a reasonable POJO object that can be remoted over to
registerResource.

<h2 class="pdoc-module-header" id="serializeFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L70">function serializeFunction</a>
</h2>

```typescript
serializeFunction(func: Function, args?: SerializeFunctionArgs): Promise<SerializedFunction>
```


serializeFunction serializes a JavaScript function into a text form that can be loaded in another exuection context,
for example as part of a function callback associated with an AWS Lambda.  The function serialization captures any
variables captured by the function body and serializes those values into the generated text along with the function
body.  This process is recursive, so that functions referenced by the body of the serialized function will themselves
be serialized as well.  Thid process also deeply serializes captured object values, including prototype chains and
property descriptors, such that the semantics of the function when deserialized should match the original function.

There are several known limitations:
- If a native function is captured either directly or indirectly, closure serialization will return an error.
- Captured values will be serialized based on their values at the time that `serializeFunction` is called.  Mutations
  to these values after that (but before the deserialized funtion is used) will not be observed by the deserialized
  function.

<h2 class="pdoc-module-header" id="serializeFunctionAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L85">function serializeFunctionAsync</a>
</h2>

```typescript
serializeFunctionAsync(func: Function, serialize?: undefined | { ... }): Promise<string>
```

<h2 class="pdoc-module-header" id="serializeJavaScriptText">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L99">function serializeJavaScriptText</a>
</h2>

```typescript
serializeJavaScriptText(func: Function, outerFunction: closure.FunctionInfo, exportName: string): SerializedFunction
```


serializeJavaScriptText converts a FunctionInfo object into a string representation of a Node.js module body which
exposes a single function `exports.handler` representing the serialized function.

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

<h2 class="pdoc-module-header" id="throwSerializationError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L563">function throwSerializationError</a>
</h2>

```typescript
throwSerializationError(func: Function, context: Context, info: string): never
```

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

<h2 class="pdoc-module-header" id="waitForDeath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/invoke.ts#L85">function waitForDeath</a>
</h2>

```typescript
waitForDeath(): never
```


waitForDeath loops forever. See the comments in resource.ts on the function with
the same name for an explanation as to why this exists.

<h2 class="pdoc-module-header" id="CapturedPropertyInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L51">interface CapturedPropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L53">property invoked</a>
</h3>

```typescript
invoked: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L52">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="CapturedVariables">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L62">interface CapturedVariables</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L64">property optional</a>
</h3>

```typescript
optional: CapturedVariableMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L63">property required</a>
</h3>

```typescript
required: CapturedVariableMap;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L65">property requiredPackages</a>
</h3>

```typescript
requiredPackages: Set<string>;
```

<h2 class="pdoc-module-header" id="Context">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L113">interface Context</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L139">property asyncWorkQueue</a>
</h3>

```typescript
asyncWorkQueue: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L117">property cache</a>
</h3>

```typescript
cache: Map<Object, Entry>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L131">property classInstanceMemberToSuperEntry</a>
</h3>

```typescript
classInstanceMemberToSuperEntry: Map<Function, Entry>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L132">property classStaticMemberToSuperEntry</a>
</h3>

```typescript
classStaticMemberToSuperEntry: Map<Function, Entry>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L122">property frames</a>
</h3>

```typescript
frames: ContextFrame[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L147">property simpleFunctions</a>
</h3>

```typescript
simpleFunctions: FunctionInfo[];
```

<h2 class="pdoc-module-header" id="ContextFrame">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L159">interface ContextFrame</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L161">property capturedFunctionName</a>
</h3>

```typescript
capturedFunctionName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L163">property capturedModuleName</a>
</h3>

```typescript
capturedModuleName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L162">property capturedVariableName</a>
</h3>

```typescript
capturedVariableName?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L160">property functionLocation</a>
</h3>

```typescript
functionLocation?: FunctionLocation;
```

<h2 class="pdoc-module-header" id="Entry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L87">interface Entry</a>
</h2>

Entry is the environment slot for a named lexically captured variable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L99">property array</a>
</h3>

```typescript
array?: Entry[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L110">property expr</a>
</h3>

```typescript
expr?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L92">property function</a>
</h3>

```typescript
function?: FunctionInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L89">property json</a>
</h3>

```typescript
json?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L96">property object</a>
</h3>

```typescript
object?: ObjectInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L107">property output</a>
</h3>

```typescript
output?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L103">property promise</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L52">property requiredPackages</a>
</h3>

```typescript
requiredPackages: Set<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L45">property usesNonLexicalThis</a>
</h3>

```typescript
usesNonLexicalThis: boolean;
```

<h2 class="pdoc-module-header" id="FunctionLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L150">interface FunctionLocation</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L154">property column</a>
</h3>

```typescript
column: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L152">property file</a>
</h3>

```typescript
file: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L151">property func</a>
</h3>

```typescript
func: Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L155">property functionString</a>
</h3>

```typescript
functionString: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L156">property isArrowFunction</a>
</h3>

```typescript
isArrowFunction?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L153">property line</a>
</h3>

```typescript
line: number;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L46">property requiredPackages</a>
</h3>

```typescript
requiredPackages: Set<string>;
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L57">interface PropertyInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L62">property configurable</a>
</h3>

```typescript
configurable?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L63">property enumerable</a>
</h3>

```typescript
enumerable?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L68">property get</a>
</h3>

```typescript
get?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L59">property hasValue</a>
</h3>

```typescript
hasValue: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L69">property set</a>
</h3>

```typescript
set?: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L64">property writable</a>
</h3>

```typescript
writable?: undefined | true | false;
```

<h2 class="pdoc-module-header" id="PropertyInfoAndValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L74">interface PropertyInfoAndValue</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L76">property entry</a>
</h3>

```typescript
entry: Entry;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L75">property info</a>
</h3>

```typescript
info?: PropertyInfo;
```

<h2 class="pdoc-module-header" id="PropertyMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/createClosure.ts#L81">interface PropertyMap</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4874">method __@iterator</a>
</h3>

```typescript
__@iterator(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of entries in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4655">method clear</a>
</h3>

```typescript
clear(): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4656">method delete</a>
</h3>

```typescript
delete(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4879">method entries</a>
</h3>

```typescript
entries(): IterableIterator<[, Entry, PropertyInfoAndValue]>
```


Returns an iterable of key, value pairs for every entry in the map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4657">method forEach</a>
</h3>

```typescript
forEach(callbackfn: { ... }, thisArg?: any): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4658">method get</a>
</h3>

```typescript
get(key: Entry): PropertyInfoAndValue | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4659">method has</a>
</h3>

```typescript
has(key: Entry): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4884">method keys</a>
</h3>

```typescript
keys(): IterableIterator<Entry>
```


Returns an iterable of keys in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4660">method set</a>
</h3>

```typescript
set(key: Entry, value: PropertyInfoAndValue): this
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4889">method values</a>
</h3>

```typescript
values(): IterableIterator<PropertyInfoAndValue>
```


Returns an iterable of values in the map

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4669">property Map</a>
</h3>

```typescript
Map: MapConstructor;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L5648">property __@toStringTag</a>
</h3>

```typescript
__@toStringTag: Map;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs//Users/swgillespie/go/src/github.com/pulumi/docs/node_modules/typescript/lib/lib.es6.d.ts#L4661">property size</a>
</h3>

```typescript
size: number;
```

<h2 class="pdoc-module-header" id="ResourceResolverOperation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L34">interface ResourceResolverOperation</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L46">property dependencies</a>
</h3>

```typescript
dependencies: Set<URN>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L42">property parentURN</a>
</h3>

```typescript
parentURN: URN | undefined;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L38">property resolveID</a>
</h3>

```typescript
resolveID: { ... } | undefined;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L36">property resolveURN</a>
</h3>

```typescript
resolveURN: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L40">property resolvers</a>
</h3>

```typescript
resolvers: OutputResolvers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L44">property serializedProps</a>
</h3>

```typescript
serializedProps: Record<string, any>;
```

<h2 class="pdoc-module-header" id="SerializeFunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L20">interface SerializeFunctionArgs</a>
</h2>

SerializeFunctionArgs are arguments used to serialize a JavaScript function

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L24">property exportName</a>
</h3>

```typescript
exportName?: undefined | string;
```


The name to export from the module defined by the generated module text.  Defaults to 'handler'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L29">property serialize</a>
</h3>

```typescript
serialize?: undefined | { ... };
```


A function to prevent serialization of certain objects captured during the serialization.  Primarily used to
prevent potential cycles.

<h2 class="pdoc-module-header" id="SerializedFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L35">interface SerializedFunction</a>
</h2>

SerializeFunction is a representation of a serialized JavaScript function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L44">property exportName</a>
</h3>

```typescript
exportName: string;
```


The name of the exported module member.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L50">property requiredPackages</a>
</h3>

```typescript
requiredPackages: Set<string>;
```


The set of pacakges that were 'require'd by the transitive closure of functions serialized as part of the
JavaScript function serialization.  These pacakges must be able to resolve in the target execution environment
for the serialized function to be able to be loaded and evaluated correctly.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/serializeClosure.ts#L40">property text</a>
</h3>

```typescript
text: string;
```


The text of a JavaScript module which exports a single name bound to a function value matching the serialized
JavaScript function.

<h2 class="pdoc-module-header" id="V8ScopeDetails">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L82">interface V8ScopeDetails</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L83">property scopeObject</a>
</h3>

```typescript
scopeObject: Record<string, any>;
```

<h2 class="pdoc-module-header" id="V8Script">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L37">interface V8Script</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L39">method locationFromPosition</a>
</h3>

```typescript
locationFromPosition(pos: V8SourcePosition): V8SourceLocation
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L38">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="V8SourceLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L54">interface V8SourceLocation</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L56">property column</a>
</h3>

```typescript
column: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L55">property line</a>
</h3>

```typescript
line: number;
```

<h2 class="pdoc-module-header" id="V8SourcePosition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/v8.ts#L50">interface V8SourcePosition</a>
</h2>
<h2 class="pdoc-module-header" id="_options">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L45">let _options</a>
</h2>

```typescript
let _options: Options | undefined;
```


_options are the current deployment options being used for this entire session.

<h2 class="pdoc-module-header" id="engine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L114">let engine</a>
</h2>

```typescript
let engine: any | undefined;
```


engine is a live connection to the engine, used for logging, etc. (lazily initialized).

<h2 class="pdoc-module-header" id="excessiveDebugOutput">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L28">let excessiveDebugOutput</a>
</h2>

```typescript
let excessiveDebugOutput: boolean = false;
```


excessiveDebugOutput enables, well, pretty excessive debug output pertaining to resources and properties.

<h2 class="pdoc-module-header" id="leakDetectorScheduled">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/debuggable.ts#L25">let leakDetectorScheduled</a>
</h2>

```typescript
let leakDetectorScheduled: boolean = false;
```


leakDetectorScheduled is true when the promise leak detector is scheduled for process exit.

<h2 class="pdoc-module-header" id="loaded">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/config.ts#L49">let loaded</a>
</h2>

```typescript
let loaded: boolean = false;
```


loaded is set to true if and when we've attempted to load config from the environment.

<h2 class="pdoc-module-header" id="monitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L84">let monitor</a>
</h2>

```typescript
let monitor: any | undefined;
```


monitor is a live connection to the resource monitor that tracks deployments (lazily initialized).

<h2 class="pdoc-module-header" id="resourceChain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L316">let resourceChain</a>
</h2>

```typescript
let resourceChain: Promise<void> =  Promise.resolve();
```


resourceChain is used to serialize all resource requests.  If we don't do this, all resource operations will be
entirely asynchronous, meaning the dataflow graph that results will determine ordering of operations.  This
causes problems with some resource providers, so for now we will serialize all of them.  The issue
pulumi/pulumi#335 tracks coming up with a long-term solution here.

<h2 class="pdoc-module-header" id="resourceChainLabel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/resource.ts#L317">let resourceChainLabel</a>
</h2>

```typescript
let resourceChainLabel: string | undefined =  undefined;
```

<h2 class="pdoc-module-header" id="rootResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L263">let rootResource</a>
</h2>

```typescript
let rootResource: Resource | undefined;
```

<h2 class="pdoc-module-header" id="rpcDone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/settings.ts#L250">let rpcDone</a>
</h2>

```typescript
let rpcDone: Promise<any> =  Promise.resolve();
```


rpcDone resolves when the last known client-side RPC call finishes.

<h2 class="pdoc-module-header" id="CapturedVariableMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/runtime/closure/parseFunction.ts#L56">type CapturedVariableMap</a>
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

