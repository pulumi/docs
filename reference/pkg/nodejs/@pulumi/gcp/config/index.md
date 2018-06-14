---
title: Module config
---

<a href="../index.html">@pulumi/gcp</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#__config">let __config</a>
* <a href="#credentials">let credentials</a>
* <a href="#project">let project</a>
* <a href="#region">let region</a>
* <a href="#zone">let zone</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="__config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L6">let __config</a>
</h2>

```typescript
let __config: Config =  new pulumi.Config("gcp");
```

<h2 class="pdoc-module-header" id="credentials">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L8">let credentials</a>
</h2>

```typescript
let credentials: string | undefined =  __config.get("credentials");
```

<h2 class="pdoc-module-header" id="project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L9">let project</a>
</h2>

```typescript
let project: string | undefined =  __config.get("project");
```

<h2 class="pdoc-module-header" id="region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L10">let region</a>
</h2>

```typescript
let region: string | undefined =  __config.get("region");
```

<h2 class="pdoc-module-header" id="zone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L11">let zone</a>
</h2>

```typescript
let zone: string | undefined =  __config.get("zone");
```

