---
title: Module config
---

<a href="../index.html">@pulumi/vsphere</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#allowUnverifiedSsl">let allowUnverifiedSsl</a>
* <a href="#clientDebug">let clientDebug</a>
* <a href="#clientDebugPath">let clientDebugPath</a>
* <a href="#clientDebugPathRun">let clientDebugPathRun</a>
* <a href="#password">let password</a>
* <a href="#persistSession">let persistSession</a>
* <a href="#restSessionPath">let restSessionPath</a>
* <a href="#user">let user</a>
* <a href="#vcenterServer">let vcenterServer</a>
* <a href="#vimSessionPath">let vimSessionPath</a>
* <a href="#vsphereServer">let vsphereServer</a>

<a href="/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="allowUnverifiedSsl">
<a class="pdoc-member-name" href="/config/vars.ts#L11">let allowUnverifiedSsl</a>
</h2>

```typescript
let allowUnverifiedSsl: boolean | undefined =  __config.getObject<boolean>("allowUnverifiedSsl");
```


If set, VMware vSphere client will permit unverifiable SSL certificates.

<h2 class="pdoc-module-header" id="clientDebug">
<a class="pdoc-member-name" href="/config/vars.ts#L15">let clientDebug</a>
</h2>

```typescript
let clientDebug: boolean | undefined =  __config.getObject<boolean>("clientDebug");
```


govmomi debug

<h2 class="pdoc-module-header" id="clientDebugPath">
<a class="pdoc-member-name" href="/config/vars.ts#L19">let clientDebugPath</a>
</h2>

```typescript
let clientDebugPath: string | undefined =  __config.get("clientDebugPath");
```


govmomi debug path for debug

<h2 class="pdoc-module-header" id="clientDebugPathRun">
<a class="pdoc-member-name" href="/config/vars.ts#L23">let clientDebugPathRun</a>
</h2>

```typescript
let clientDebugPathRun: string | undefined =  __config.get("clientDebugPathRun");
```


govmomi debug path for a single run

<h2 class="pdoc-module-header" id="password">
<a class="pdoc-member-name" href="/config/vars.ts#L27">let password</a>
</h2>

```typescript
let password: string =  __config.require("password");
```


The user password for vSphere API operations.

<h2 class="pdoc-module-header" id="persistSession">
<a class="pdoc-member-name" href="/config/vars.ts#L31">let persistSession</a>
</h2>

```typescript
let persistSession: boolean | undefined =  __config.getObject<boolean>("persistSession");
```


Persist vSphere client sessions to disk

<h2 class="pdoc-module-header" id="restSessionPath">
<a class="pdoc-member-name" href="/config/vars.ts#L35">let restSessionPath</a>
</h2>

```typescript
let restSessionPath: string | undefined =  __config.get("restSessionPath");
```


The directory to save vSphere REST API sessions to

<h2 class="pdoc-module-header" id="user">
<a class="pdoc-member-name" href="/config/vars.ts#L39">let user</a>
</h2>

```typescript
let user: string =  __config.require("user");
```


The user name for vSphere API operations.

<h2 class="pdoc-module-header" id="vcenterServer">
<a class="pdoc-member-name" href="/config/vars.ts#L40">let vcenterServer</a>
</h2>

```typescript
let vcenterServer: string | undefined =  __config.get("vcenterServer");
```

<h2 class="pdoc-module-header" id="vimSessionPath">
<a class="pdoc-member-name" href="/config/vars.ts#L44">let vimSessionPath</a>
</h2>

```typescript
let vimSessionPath: string | undefined =  __config.get("vimSessionPath");
```


The directory to save vSphere SOAP API sessions to

<h2 class="pdoc-module-header" id="vsphereServer">
<a class="pdoc-member-name" href="/config/vars.ts#L48">let vsphereServer</a>
</h2>

```typescript
let vsphereServer: string | undefined =  __config.get("vsphereServer");
```


The vSphere Server name for vSphere API operations.

