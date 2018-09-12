---
title: Module config
---

<a href="../index.html">@pulumi/azure</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#clientId">let clientId</a>
* <a href="#clientSecret">let clientSecret</a>
* <a href="#environment">let environment</a>
* <a href="#msiEndpoint">let msiEndpoint</a>
* <a href="#skipCredentialsValidation">let skipCredentialsValidation</a>
* <a href="#skipProviderRegistration">let skipProviderRegistration</a>
* <a href="#subscriptionId">let subscriptionId</a>
* <a href="#tenantId">let tenantId</a>
* <a href="#useMsi">let useMsi</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="clientId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L9">let clientId</a>
</h2>

```typescript
let clientId: string | undefined =  __config.get("clientId") || (utilities.getEnv("ARM_CLIENT_ID") || "");
```

<h2 class="pdoc-module-header" id="clientSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L10">let clientSecret</a>
</h2>

```typescript
let clientSecret: string | undefined =  __config.get("clientSecret") || (utilities.getEnv("ARM_CLIENT_SECRET") || "");
```

<h2 class="pdoc-module-header" id="environment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L11">let environment</a>
</h2>

```typescript
let environment: string =  utilities.requireWithDefault(() => __config.require("environment"), (utilities.getEnv("ARM_ENVIRONMENT") || "public"));
```

<h2 class="pdoc-module-header" id="msiEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L12">let msiEndpoint</a>
</h2>

```typescript
let msiEndpoint: string | undefined =  __config.get("msiEndpoint") || (utilities.getEnv("ARM_MSI_ENDPOINT") || "");
```

<h2 class="pdoc-module-header" id="skipCredentialsValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L13">let skipCredentialsValidation</a>
</h2>

```typescript
let skipCredentialsValidation: boolean | undefined =  __config.getObject<boolean>("skipCredentialsValidation") || (utilities.getEnvBoolean("ARM_SKIP_CREDENTIALS_VALIDATION") || false);
```

<h2 class="pdoc-module-header" id="skipProviderRegistration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L14">let skipProviderRegistration</a>
</h2>

```typescript
let skipProviderRegistration: boolean | undefined =  __config.getObject<boolean>("skipProviderRegistration") || (utilities.getEnvBoolean("ARM_SKIP_PROVIDER_REGISTRATION") || false);
```

<h2 class="pdoc-module-header" id="subscriptionId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L15">let subscriptionId</a>
</h2>

```typescript
let subscriptionId: string | undefined =  __config.get("subscriptionId") || (utilities.getEnv("ARM_SUBSCRIPTION_ID") || "");
```

<h2 class="pdoc-module-header" id="tenantId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L16">let tenantId</a>
</h2>

```typescript
let tenantId: string | undefined =  __config.get("tenantId") || (utilities.getEnv("ARM_TENANT_ID") || "");
```

<h2 class="pdoc-module-header" id="useMsi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L17">let useMsi</a>
</h2>

```typescript
let useMsi: boolean | undefined =  __config.getObject<boolean>("useMsi") || (utilities.getEnvBoolean("ARM_USE_MSI") || false);
```

