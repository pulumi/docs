---
title: Module log
---

<a href="../index.html">@pulumi/pulumi</a> &gt; log

<h2 class="pdoc-module-header">Index</h2>

* <a href="#engproto">const engproto</a>
* <a href="#debug">function debug</a>
* <a href="#error">function error</a>
* <a href="#hasErrors">function hasErrors</a>
* <a href="#info">function info</a>
* <a href="#log">function log</a>
* <a href="#warn">function warn</a>
* <a href="#errcnt">let errcnt</a>
* <a href="#lastLog">let lastLog</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts">log/index.ts</a> 


<h2 class="pdoc-module-header" id="engproto">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L20">const engproto</a>
</h2>

```typescript
const engproto: any =  require("../proto/engine_pb.js");
```

<h2 class="pdoc-module-header" id="debug">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L35">function debug</a>
</h2>

```typescript
debug(msg: string, resource?: resourceTypes.Resource, streamId?: undefined | number): Promise<void>
```


debug logs a debug-level message that is generally hidden from end-users.

<h2 class="pdoc-module-header" id="error">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L76">function error</a>
</h2>

```typescript
error(msg: string, resource?: resourceTypes.Resource, streamId?: undefined | number): Promise<void>
```


error logs a fatal error to indicate that the tool should stop processing resource operations immediately.

<h2 class="pdoc-module-header" id="hasErrors">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L28">function hasErrors</a>
</h2>

```typescript
hasErrors(): boolean
```


hasErrors returns true if any errors have occurred in the program.

<h2 class="pdoc-module-header" id="info">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L48">function info</a>
</h2>

```typescript
info(msg: string, resource?: resourceTypes.Resource, streamId?: undefined | number): Promise<void>
```


info logs an informational message that is generally printed to stdout during resource operations.

<h2 class="pdoc-module-header" id="log">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L89">function log</a>
</h2>

```typescript
log(engine: any, sev: any, msg: string, resource: resourceTypes.Resource | undefined, streamId: number | undefined): Promise<void>
```

<h2 class="pdoc-module-header" id="warn">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L62">function warn</a>
</h2>

```typescript
warn(msg: string, resource?: resourceTypes.Resource, streamId?: undefined | number): Promise<void>
```


warn logs a warning to indicate that something went wrong, but not catastrophically so.

<h2 class="pdoc-module-header" id="errcnt">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L22">let errcnt</a>
</h2>

```typescript
let errcnt: number = 0;
```

<h2 class="pdoc-module-header" id="lastLog">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/log/index.ts#L23">let lastLog</a>
</h2>

```typescript
let lastLog: Promise<any> =  Promise.resolve();
```

