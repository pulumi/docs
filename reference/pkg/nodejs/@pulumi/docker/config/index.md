---
title: Module config
---

<a href="../index.html">@pulumi/docker</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#caMaterial">let caMaterial</a>
* <a href="#certMaterial">let certMaterial</a>
* <a href="#certPath">let certPath</a>
* <a href="#host">let host</a>
* <a href="#keyMaterial">let keyMaterial</a>
* <a href="#registryAuth">let registryAuth</a>

<a href="/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="caMaterial">
<a class="pdoc-member-name" href="/config/vars.ts#L12">let caMaterial</a>
</h2>

```typescript
let caMaterial: string | undefined =  __config.get("caMaterial") || utilities.getEnv("DOCKER_CA_MATERIAL");
```


PEM-encoded content of Docker host CA certificate

<h2 class="pdoc-module-header" id="certMaterial">
<a class="pdoc-member-name" href="/config/vars.ts#L16">let certMaterial</a>
</h2>

```typescript
let certMaterial: string | undefined =  __config.get("certMaterial") || utilities.getEnv("DOCKER_CERT_MATERIAL");
```


PEM-encoded content of Docker client certificate

<h2 class="pdoc-module-header" id="certPath">
<a class="pdoc-member-name" href="/config/vars.ts#L20">let certPath</a>
</h2>

```typescript
let certPath: string | undefined =  __config.get("certPath") || utilities.getEnv("DOCKER_CERT_PATH");
```


Path to directory with Docker TLS config

<h2 class="pdoc-module-header" id="host">
<a class="pdoc-member-name" href="/config/vars.ts#L24">let host</a>
</h2>

```typescript
let host: string =  utilities.requireWithDefault(() => __config.require("host"), (utilities.getEnv("DOCKER_HOST") || "unix:///var/run/docker.sock"));
```


The Docker daemon address

<h2 class="pdoc-module-header" id="keyMaterial">
<a class="pdoc-member-name" href="/config/vars.ts#L28">let keyMaterial</a>
</h2>

```typescript
let keyMaterial: string | undefined =  __config.get("keyMaterial") || utilities.getEnv("DOCKER_KEY_MATERIAL");
```


PEM-encoded content of Docker client private key

<h2 class="pdoc-module-header" id="registryAuth">
<a class="pdoc-member-name" href="/config/vars.ts#L29">let registryAuth</a>
</h2>

```typescript
let registryAuth: { ... }[] | undefined =  __config.getObject<{ address: string, configFile?: string, password?: string, username?: string }[]>("registryAuth");
```

