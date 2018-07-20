---
title: Module tests
---

<a href="../index.html">@pulumi/pulumi</a> &gt; tests

<h2 class="pdoc-module-header">Index</h2>

* <a href="#exportedValue">const exportedValue</a>
* <a href="#gempty">const gempty</a>
* <a href="#grpc">const grpc</a>
* <a href="#gstruct">const gstruct</a>
* <a href="#langproto">const langproto</a>
* <a href="#langrpc">const langrpc</a>
* <a href="#resproto">const resproto</a>
* <a href="#resrpc">const resrpc</a>
* <a href="#assertAsyncThrows">function assertAsyncThrows</a>
* <a href="#asyncTest">function asyncTest</a>
* <a href="#compareErrorText">function compareErrorText</a>
* <a href="#createMockResourceMonitor">function createMockResourceMonitor</a>
* <a href="#makeUrn">function makeUrn</a>
* <a href="#mockRun">function mockRun</a>
* <a href="#serveLanguageHostProcess">function serveLanguageHostProcess</a>
* <a href="#stripEOL">function stripEOL</a>
* <a href="#ClosureCase">interface ClosureCase</a>
* <a href="#RunCase">interface RunCase</a>
* <a href="#MochaFunc">type MochaFunc</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts">tests/runtime/closure.spec.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts">tests/runtime/langhost/run.spec.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/util.ts">tests/util.ts</a> 


<h2 class="pdoc-module-header" id="exportedValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L34">const exportedValue</a>
</h2>

```typescript
const exportedValue: 42 = 42;
```

<h2 class="pdoc-module-header" id="gempty">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L22">const gempty</a>
</h2>

```typescript
const gempty: any =  require("google-protobuf/google/protobuf/empty_pb.js");
```

<h2 class="pdoc-module-header" id="grpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L24">const grpc</a>
</h2>

```typescript
const grpc: any =  require("grpc");
```

<h2 class="pdoc-module-header" id="gstruct">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L23">const gstruct</a>
</h2>

```typescript
const gstruct: any =  require("google-protobuf/google/protobuf/struct_pb.js");
```

<h2 class="pdoc-module-header" id="langproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L26">const langproto</a>
</h2>

```typescript
const langproto: any =  require("../../../proto/language_pb.js");
```

<h2 class="pdoc-module-header" id="langrpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L25">const langrpc</a>
</h2>

```typescript
const langrpc: any =  require("../../../proto/language_grpc_pb.js");
```

<h2 class="pdoc-module-header" id="resproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L28">const resproto</a>
</h2>

```typescript
const resproto: any =  require("../../../proto/resource_pb.js");
```

<h2 class="pdoc-module-header" id="resrpc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L27">const resrpc</a>
</h2>

```typescript
const resrpc: any =  require("../../../proto/resource_grpc_pb.js");
```

<h2 class="pdoc-module-header" id="assertAsyncThrows">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/util.ts#L40">function assertAsyncThrows</a>
</h2>

```typescript
assertAsyncThrows(test: { ... }): Promise<string>
```

<h2 class="pdoc-module-header" id="asyncTest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/util.ts#L21">function asyncTest</a>
</h2>

```typescript
asyncTest(test: { ... }): { ... }
```

<h2 class="pdoc-module-header" id="compareErrorText">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L4780">function compareErrorText</a>
</h2>

```typescript
compareErrorText(expected: string, actual: string): void
```


compareErrorText compares an "expected" error string and an "actual" error string
and issues an error if they do not match.

This function accepts two repetition operators to make writing tests easier against
error messages that are dependent on the environment:

 * (...) alone on a single line causes the matcher to accept zero or more lines
   between the repetition and the next line.
 * (...) within in the context of a line causes the matcher to accept zero or more characters
   between the repetition and the next character.

This is useful when testing error messages that you get when capturing bulit-in modules,
because the specific error message differs between Node versions.
<h2 class="pdoc-module-header" id="createMockResourceMonitor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L543">function createMockResourceMonitor</a>
</h2>

```typescript
createMockResourceMonitor(invokeCallback: { ... }, readResourceCallback: { ... }, registerResourceCallback: { ... }, registerResourceOutputsCallback: { ... }): { ... }
```

<h2 class="pdoc-module-header" id="makeUrn">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L48">function makeUrn</a>
</h2>

```typescript
makeUrn(t: string, name: string): URN
```

<h2 class="pdoc-module-header" id="mockRun">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L509">function mockRun</a>
</h2>

```typescript
mockRun(langHostClient: any, monitor: string, opts: RunCase, dryrun: boolean): Promise<string | undefined>
```

<h2 class="pdoc-module-header" id="serveLanguageHostProcess">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L561">function serveLanguageHostProcess</a>
</h2>

```typescript
serveLanguageHostProcess(): { ... }
```

<h2 class="pdoc-module-header" id="stripEOL">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L594">function stripEOL</a>
</h2>

```typescript
stripEOL(data: string | Buffer): string
```

<h2 class="pdoc-module-header" id="ClosureCase">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L24">interface ClosureCase</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L31">property afters</a>
</h3>

```typescript
afters?: ClosureCase[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L30">property error</a>
</h3>

```typescript
error?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L29">property expectPackages</a>
</h3>

```typescript
expectPackages?: Set<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L28">property expectText</a>
</h3>

```typescript
expectText?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L27">property func</a>
</h3>

```typescript
func: Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L25">property pre</a>
</h3>

```typescript
pre?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/closure.spec.ts#L26">property title</a>
</h3>

```typescript
title: string;
```

<h2 class="pdoc-module-header" id="RunCase">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L30">interface RunCase</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L35">property args</a>
</h3>

```typescript
args?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L36">property config</a>
</h3>

```typescript
config?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L37">property expectError</a>
</h3>

```typescript
expectError?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L38">property expectResourceCount</a>
</h3>

```typescript
expectResourceCount?: undefined | number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L39">property invoke</a>
</h3>

```typescript
invoke?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L34">property program</a>
</h3>

```typescript
program?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L31">property project</a>
</h3>

```typescript
project?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L33">property pwd</a>
</h3>

```typescript
pwd?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L40">property readResource</a>
</h3>

```typescript
readResource?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L42">property registerResource</a>
</h3>

```typescript
registerResource?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L44">property registerResourceOutputs</a>
</h3>

```typescript
registerResourceOutputs?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/runtime/langhost/run.spec.ts#L32">property stack</a>
</h3>

```typescript
stack?: undefined | string;
```

<h2 class="pdoc-module-header" id="MochaFunc">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/util.ts#L17">type MochaFunc</a>
</h2>

```typescript
type MochaFunc = { ... };
```

