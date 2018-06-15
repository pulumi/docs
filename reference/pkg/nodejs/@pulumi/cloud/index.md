---
title: Package @pulumi/cloud
---


Node.js:

```javascript
var cloud = require("@pulumi/cloud");
```

ES6 modules:

```typescript
import * as cloud from "@pulumi/cloud";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#config">const config</a>
* <a href="#provider">const provider</a>
* <a href="#loadFrameworkModule">function loadFrameworkModule</a>
* <a href="#require">function require</a>
* <a href="#module">let module</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts">index.ts</a> 


<h2 class="pdoc-module-header" id="config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts#L25">const config</a>
</h2>

```typescript
const config: Config =  new pulumi.Config("cloud");
```

<h2 class="pdoc-module-header" id="provider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts#L27">const provider</a>
</h2>

```typescript
const provider: string =  config.require("provider");
```

<h2 class="pdoc-module-header" id="loadFrameworkModule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts#L30">function loadFrameworkModule</a>
</h2>

```typescript
loadFrameworkModule(): any
```

<h2 class="pdoc-module-header" id="require">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts#L23">function require</a>
</h2>

```typescript
require(name: string): any
```

<h2 class="pdoc-module-header" id="module">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/index.ts#L22">let module</a>
</h2>

```typescript
let module: any;
```

