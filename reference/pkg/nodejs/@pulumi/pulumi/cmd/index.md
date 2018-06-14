---
title: Module cmd
---

<a href="../index.html">@pulumi/pulumi</a> &gt; cmd

<h2 class="pdoc-module-header">Index</h2>

* <a href="#emptyproto">const emptyproto</a>
* <a href="#grpc">const grpc</a>
* <a href="#plugproto">const plugproto</a>
* <a href="#providerKey">const providerKey</a>
* <a href="#provproto">const provproto</a>
* <a href="#provrpc">const provrpc</a>
* <a href="#requireFromString">const requireFromString</a>
* <a href="#structproto">const structproto</a>
* <a href="#checkRPC">function checkRPC</a>
* <a href="#configureRPC">function configureRPC</a>
* <a href="#createRPC">function createRPC</a>
* <a href="#deleteRPC">function deleteRPC</a>
* <a href="#diffRPC">function diffRPC</a>
* <a href="#getPluginInfoRPC">function getPluginInfoRPC</a>
* <a href="#getProvider">function getProvider</a>
* <a href="#invokeRPC">function invokeRPC</a>
* <a href="#main">function main</a>
* <a href="#printErrorUsageAndExit">function printErrorUsageAndExit</a>
* <a href="#readRPC">function readRPC</a>
* <a href="#reportModuleLoadFailure">function reportModuleLoadFailure</a>
* <a href="#resultIncludingProvider">function resultIncludingProvider</a>
* <a href="#updateRPC">function updateRPC</a>
* <a href="#usage">function usage</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts">cmd/dynamic-provider/index.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/run/index.ts">cmd/run/index.ts</a> 


<h2 class="pdoc-module-header" id="emptyproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L24">const emptyproto</a>
</h2>

```typescript
const emptyproto: any =  require("google-protobuf/google/protobuf/empty_pb.js");
```

<h2 class="pdoc-module-header" id="grpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L23">const grpc</a>
</h2>

```typescript
const grpc: any =  require("grpc");
```

<h2 class="pdoc-module-header" id="plugproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L28">const plugproto</a>
</h2>

```typescript
const plugproto: any =  require("../../proto/plugin_pb.js");
```

<h2 class="pdoc-module-header" id="providerKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L30">const providerKey</a>
</h2>

```typescript
const providerKey: string = "__provider";
```

<h2 class="pdoc-module-header" id="provproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L26">const provproto</a>
</h2>

```typescript
const provproto: any =  require("../../proto/provider_pb.js");
```

<h2 class="pdoc-module-header" id="provrpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L27">const provrpc</a>
</h2>

```typescript
const provrpc: any =  require("../../proto/provider_grpc_pb.js");
```

<h2 class="pdoc-module-header" id="requireFromString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L22">const requireFromString</a>
</h2>

```typescript
const requireFromString: any =  require("require-from-string");
```

<h2 class="pdoc-module-header" id="structproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L25">const structproto</a>
</h2>

```typescript
const structproto: any =  require("google-protobuf/google/protobuf/struct_pb.js");
```

<h2 class="pdoc-module-header" id="checkRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L59">function checkRPC</a>
</h2>

```typescript
checkRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="configureRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L48">function configureRPC</a>
</h2>

```typescript
configureRPC(call: any, callback: any): void
```

<h2 class="pdoc-module-header" id="createRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L142">function createRPC</a>
</h2>

```typescript
createRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="deleteRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L213">function deleteRPC</a>
</h2>

```typescript
deleteRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="diffRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L101">function diffRPC</a>
</h2>

```typescript
diffRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="getPluginInfoRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L228">function getPluginInfoRPC</a>
</h2>

```typescript
getPluginInfoRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="getProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L32">function getProvider</a>
</h2>

```typescript
getProvider(props: any): dynamic.ResourceProvider
```

<h2 class="pdoc-module-header" id="invokeRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L52">function invokeRPC</a>
</h2>

```typescript
invokeRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="main">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L240">function main</a>
</h2>

```typescript
main(args: string[]): void
```

<h2 class="pdoc-module-header" id="printErrorUsageAndExit">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/run/index.ts#L43">function printErrorUsageAndExit</a>
</h2>

```typescript
printErrorUsageAndExit(message: string): never
```

<h2 class="pdoc-module-header" id="readRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L161">function readRPC</a>
</h2>

```typescript
readRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="reportModuleLoadFailure">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/run/index.ts#L55">function reportModuleLoadFailure</a>
</h2>

```typescript
reportModuleLoadFailure(program: string, error: Error): never
```


Attempts to provide a detailed error message for module load failure if the
module that failed to load is the top-level module.

<h2 class="pdoc-module-header" id="resultIncludingProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L234">function resultIncludingProvider</a>
</h2>

```typescript
resultIncludingProvider(result: any, props: any): any
```

<h2 class="pdoc-module-header" id="updateRPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/dynamic-provider/index.ts#L186">function updateRPC</a>
</h2>

```typescript
updateRPC(call: any, callback: any): Promise<void>
```

<h2 class="pdoc-module-header" id="usage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/cmd/run/index.ts#L26">function usage</a>
</h2>

```typescript
usage(): void
```

