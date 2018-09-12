---
title: Module config
---

<a href="../index.html">@pulumi/gcp</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#credentials">let credentials</a>
* <a href="#project">let project</a>
* <a href="#region">let region</a>
* <a href="#zone">let zone</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="credentials">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L9">let credentials</a>
</h2>

```typescript
let credentials: string | undefined =  __config.get("credentials") || utilities.getEnv("GOOGLE_CREDENTIALS", "GOOGLE_CLOUD_KEYFILE_JSON", "GCLOUD_KEYFILE_JSON");
```

<h2 class="pdoc-module-header" id="project">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L10">let project</a>
</h2>

```typescript
let project: string | undefined =  __config.get("project") || utilities.getEnv("GOOGLE_PROJECT", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT", "CLOUDSDK_CORE_PROJECT");
```

<h2 class="pdoc-module-header" id="region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L11">let region</a>
</h2>

```typescript
let region: string | undefined =  __config.get("region") || utilities.getEnv("GOOGLE_REGION", "GCLOUD_REGION", "CLOUDSDK_COMPUTE_REGION");
```

<h2 class="pdoc-module-header" id="zone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/config/vars.ts#L12">let zone</a>
</h2>

```typescript
let zone: string | undefined =  __config.get("zone") || utilities.getEnv("GOOGLE_ZONE", "GCLOUD_ZONE", "CLOUDSDK_COMPUTE_ZONE");
```

