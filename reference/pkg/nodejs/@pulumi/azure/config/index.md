---
title: Module config
---

<a href="../index.html">@pulumi/azure</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#__config">let __config</a>
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


<h2 class="pdoc-module-header" id="__config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L6">let __config</a>
</h2>

```typescript
let __config: Config =  new pulumi.Config("azure");
```

<h2 class="pdoc-module-header" id="clientId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L8">let clientId</a>
</h2>

```typescript
let clientId: string | undefined =  __config.get("clientId");
```

<h2 class="pdoc-module-header" id="clientSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L9">let clientSecret</a>
</h2>

```typescript
let clientSecret: string | undefined =  __config.get("clientSecret");
```

<h2 class="pdoc-module-header" id="environment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L10">let environment</a>
</h2>

```typescript
let environment: string =  __config.require("environment");
```

<h2 class="pdoc-module-header" id="msiEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L11">let msiEndpoint</a>
</h2>

```typescript
let msiEndpoint: string | undefined =  __config.get("msiEndpoint");
```

<h2 class="pdoc-module-header" id="skipCredentialsValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L12">let skipCredentialsValidation</a>
</h2>

```typescript
let skipCredentialsValidation: boolean | undefined =  __config.getObject<boolean>("skipCredentialsValidation");
```

<h2 class="pdoc-module-header" id="skipProviderRegistration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L13">let skipProviderRegistration</a>
</h2>

```typescript
let skipProviderRegistration: boolean | undefined =  __config.getObject<boolean>("skipProviderRegistration");
```

<h2 class="pdoc-module-header" id="subscriptionId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L14">let subscriptionId</a>
</h2>

```typescript
let subscriptionId: string | undefined =  __config.get("subscriptionId");
```

<h2 class="pdoc-module-header" id="tenantId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L15">let tenantId</a>
</h2>

```typescript
let tenantId: string | undefined =  __config.get("tenantId");
```

<h2 class="pdoc-module-header" id="useMsi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/config/vars.ts#L16">let useMsi</a>
</h2>

```typescript
let useMsi: boolean | undefined =  __config.getObject<boolean>("useMsi");
```

