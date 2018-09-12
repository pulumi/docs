---
title: Module config
---

<a href="../index.html">@pulumi/openstack</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#authUrl">let authUrl</a>
* <a href="#cacertFile">let cacertFile</a>
* <a href="#cert">let cert</a>
* <a href="#cloud">let cloud</a>
* <a href="#defaultDomain">let defaultDomain</a>
* <a href="#domainId">let domainId</a>
* <a href="#domainName">let domainName</a>
* <a href="#endpointType">let endpointType</a>
* <a href="#insecure">let insecure</a>
* <a href="#key">let key</a>
* <a href="#password">let password</a>
* <a href="#projectDomainId">let projectDomainId</a>
* <a href="#projectDomainName">let projectDomainName</a>
* <a href="#region">let region</a>
* <a href="#swauth">let swauth</a>
* <a href="#tenantId">let tenantId</a>
* <a href="#tenantName">let tenantName</a>
* <a href="#token">let token</a>
* <a href="#useOctavia">let useOctavia</a>
* <a href="#userDomainId">let userDomainId</a>
* <a href="#userDomainName">let userDomainName</a>
* <a href="#userId">let userId</a>
* <a href="#userName">let userName</a>

<a href="/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="authUrl">
<a class="pdoc-member-name" href="/config/vars.ts#L12">let authUrl</a>
</h2>

```typescript
let authUrl: string | undefined =  __config.get("authUrl") || utilities.getEnv("OS_AUTH_URL");
```


The Identity authentication URL.

<h2 class="pdoc-module-header" id="cacertFile">
<a class="pdoc-member-name" href="/config/vars.ts#L16">let cacertFile</a>
</h2>

```typescript
let cacertFile: string | undefined =  __config.get("cacertFile") || utilities.getEnv("OS_CACERT");
```


A Custom CA certificate.

<h2 class="pdoc-module-header" id="cert">
<a class="pdoc-member-name" href="/config/vars.ts#L20">let cert</a>
</h2>

```typescript
let cert: string | undefined =  __config.get("cert") || utilities.getEnv("OS_CERT");
```


A client certificate to authenticate with.

<h2 class="pdoc-module-header" id="cloud">
<a class="pdoc-member-name" href="/config/vars.ts#L24">let cloud</a>
</h2>

```typescript
let cloud: string | undefined =  __config.get("cloud") || utilities.getEnv("OS_CLOUD");
```


An entry in a `clouds.yaml` file to use.

<h2 class="pdoc-module-header" id="defaultDomain">
<a class="pdoc-member-name" href="/config/vars.ts#L28">let defaultDomain</a>
</h2>

```typescript
let defaultDomain: string | undefined =  __config.get("defaultDomain") || (utilities.getEnv("OS_DEFAULT_DOMAIN") || "default");
```


The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).

<h2 class="pdoc-module-header" id="domainId">
<a class="pdoc-member-name" href="/config/vars.ts#L32">let domainId</a>
</h2>

```typescript
let domainId: string | undefined =  __config.get("domainId") || utilities.getEnv("OS_DOMAIN_ID");
```


The ID of the Domain to scope to (Identity v3).

<h2 class="pdoc-module-header" id="domainName">
<a class="pdoc-member-name" href="/config/vars.ts#L36">let domainName</a>
</h2>

```typescript
let domainName: string | undefined =  __config.get("domainName") || utilities.getEnv("OS_DOMAIN_NAME");
```


The name of the Domain to scope to (Identity v3).

<h2 class="pdoc-module-header" id="endpointType">
<a class="pdoc-member-name" href="/config/vars.ts#L37">let endpointType</a>
</h2>

```typescript
let endpointType: string | undefined =  __config.get("endpointType") || utilities.getEnv("OS_ENDPOINT_TYPE");
```

<h2 class="pdoc-module-header" id="insecure">
<a class="pdoc-member-name" href="/config/vars.ts#L41">let insecure</a>
</h2>

```typescript
let insecure: boolean | undefined =  __config.getObject<boolean>("insecure") || utilities.getEnvBoolean("OS_INSECURE");
```


Trust self-signed certificates.

<h2 class="pdoc-module-header" id="key">
<a class="pdoc-member-name" href="/config/vars.ts#L45">let key</a>
</h2>

```typescript
let key: string | undefined =  __config.get("key") || utilities.getEnv("OS_KEY");
```


A client private key to authenticate with.

<h2 class="pdoc-module-header" id="password">
<a class="pdoc-member-name" href="/config/vars.ts#L49">let password</a>
</h2>

```typescript
let password: string | undefined =  __config.get("password") || utilities.getEnv("OS_PASSWORD");
```


Password to login with.

<h2 class="pdoc-module-header" id="projectDomainId">
<a class="pdoc-member-name" href="/config/vars.ts#L53">let projectDomainId</a>
</h2>

```typescript
let projectDomainId: string | undefined =  __config.get("projectDomainId") || utilities.getEnv("OS_PROJECT_DOMAIN_ID");
```


The ID of the domain where the proejct resides (Identity v3).

<h2 class="pdoc-module-header" id="projectDomainName">
<a class="pdoc-member-name" href="/config/vars.ts#L57">let projectDomainName</a>
</h2>

```typescript
let projectDomainName: string | undefined =  __config.get("projectDomainName") || utilities.getEnv("OS_PROJECT_DOMAIN_NAME");
```


The name of the domain where the project resides (Identity v3).

<h2 class="pdoc-module-header" id="region">
<a class="pdoc-member-name" href="/config/vars.ts#L61">let region</a>
</h2>

```typescript
let region: string | undefined =  __config.get("region") || utilities.getEnv("OS_REGION_NAME");
```


The OpenStack region to connect to.

<h2 class="pdoc-module-header" id="swauth">
<a class="pdoc-member-name" href="/config/vars.ts#L65">let swauth</a>
</h2>

```typescript
let swauth: boolean | undefined =  __config.getObject<boolean>("swauth") || utilities.getEnvBoolean("OS_SWAUTH");
```


Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.

<h2 class="pdoc-module-header" id="tenantId">
<a class="pdoc-member-name" href="/config/vars.ts#L69">let tenantId</a>
</h2>

```typescript
let tenantId: string | undefined =  __config.get("tenantId") || utilities.getEnv("OS_TENANT_ID", "OS_PROJECT_ID");
```


The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h2 class="pdoc-module-header" id="tenantName">
<a class="pdoc-member-name" href="/config/vars.ts#L73">let tenantName</a>
</h2>

```typescript
let tenantName: string | undefined =  __config.get("tenantName") || utilities.getEnv("OS_TENANT_NAME", "OS_PROJECT_NAME");
```


The name of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h2 class="pdoc-module-header" id="token">
<a class="pdoc-member-name" href="/config/vars.ts#L77">let token</a>
</h2>

```typescript
let token: string | undefined =  __config.get("token") || utilities.getEnv("OS_TOKEN", "OS_AUTH_TOKEN");
```


Authentication token to use as an alternative to username/password.

<h2 class="pdoc-module-header" id="useOctavia">
<a class="pdoc-member-name" href="/config/vars.ts#L81">let useOctavia</a>
</h2>

```typescript
let useOctavia: boolean | undefined =  __config.getObject<boolean>("useOctavia") || utilities.getEnvBoolean("OS_USE_OCTAVIA");
```


If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).

<h2 class="pdoc-module-header" id="userDomainId">
<a class="pdoc-member-name" href="/config/vars.ts#L85">let userDomainId</a>
</h2>

```typescript
let userDomainId: string | undefined =  __config.get("userDomainId") || utilities.getEnv("OS_USER_DOMAIN_ID");
```


The ID of the domain where the user resides (Identity v3).

<h2 class="pdoc-module-header" id="userDomainName">
<a class="pdoc-member-name" href="/config/vars.ts#L89">let userDomainName</a>
</h2>

```typescript
let userDomainName: string | undefined =  __config.get("userDomainName") || utilities.getEnv("OS_USER_DOMAIN_NAME");
```


The name of the domain where the user resides (Identity v3).

<h2 class="pdoc-module-header" id="userId">
<a class="pdoc-member-name" href="/config/vars.ts#L93">let userId</a>
</h2>

```typescript
let userId: string | undefined =  __config.get("userId") || utilities.getEnv("OS_USER_ID");
```


Username to login with.

<h2 class="pdoc-module-header" id="userName">
<a class="pdoc-member-name" href="/config/vars.ts#L97">let userName</a>
</h2>

```typescript
let userName: string | undefined =  __config.get("userName") || utilities.getEnv("OS_USERNAME");
```


Username to login with.

