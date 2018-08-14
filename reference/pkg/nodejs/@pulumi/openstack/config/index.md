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
<a class="pdoc-member-name" href="/config/vars.ts#L11">let authUrl</a>
</h2>

```typescript
let authUrl: string | undefined =  __config.get("authUrl");
```


The Identity authentication URL.

<h2 class="pdoc-module-header" id="cacertFile">
<a class="pdoc-member-name" href="/config/vars.ts#L15">let cacertFile</a>
</h2>

```typescript
let cacertFile: string | undefined =  __config.get("cacertFile");
```


A Custom CA certificate.

<h2 class="pdoc-module-header" id="cert">
<a class="pdoc-member-name" href="/config/vars.ts#L19">let cert</a>
</h2>

```typescript
let cert: string | undefined =  __config.get("cert");
```


A client certificate to authenticate with.

<h2 class="pdoc-module-header" id="cloud">
<a class="pdoc-member-name" href="/config/vars.ts#L23">let cloud</a>
</h2>

```typescript
let cloud: string | undefined =  __config.get("cloud");
```


An entry in a `clouds.yaml` file to use.

<h2 class="pdoc-module-header" id="defaultDomain">
<a class="pdoc-member-name" href="/config/vars.ts#L27">let defaultDomain</a>
</h2>

```typescript
let defaultDomain: string | undefined =  __config.get("defaultDomain");
```


The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).

<h2 class="pdoc-module-header" id="domainId">
<a class="pdoc-member-name" href="/config/vars.ts#L31">let domainId</a>
</h2>

```typescript
let domainId: string | undefined =  __config.get("domainId");
```


The ID of the Domain to scope to (Identity v3).

<h2 class="pdoc-module-header" id="domainName">
<a class="pdoc-member-name" href="/config/vars.ts#L35">let domainName</a>
</h2>

```typescript
let domainName: string | undefined =  __config.get("domainName");
```


The name of the Domain to scope to (Identity v3).

<h2 class="pdoc-module-header" id="endpointType">
<a class="pdoc-member-name" href="/config/vars.ts#L36">let endpointType</a>
</h2>

```typescript
let endpointType: string | undefined =  __config.get("endpointType");
```

<h2 class="pdoc-module-header" id="insecure">
<a class="pdoc-member-name" href="/config/vars.ts#L40">let insecure</a>
</h2>

```typescript
let insecure: boolean | undefined =  __config.getObject<boolean>("insecure");
```


Trust self-signed certificates.

<h2 class="pdoc-module-header" id="key">
<a class="pdoc-member-name" href="/config/vars.ts#L44">let key</a>
</h2>

```typescript
let key: string | undefined =  __config.get("key");
```


A client private key to authenticate with.

<h2 class="pdoc-module-header" id="password">
<a class="pdoc-member-name" href="/config/vars.ts#L48">let password</a>
</h2>

```typescript
let password: string | undefined =  __config.get("password");
```


Password to login with.

<h2 class="pdoc-module-header" id="projectDomainId">
<a class="pdoc-member-name" href="/config/vars.ts#L52">let projectDomainId</a>
</h2>

```typescript
let projectDomainId: string | undefined =  __config.get("projectDomainId");
```


The ID of the domain where the proejct resides (Identity v3).

<h2 class="pdoc-module-header" id="projectDomainName">
<a class="pdoc-member-name" href="/config/vars.ts#L56">let projectDomainName</a>
</h2>

```typescript
let projectDomainName: string | undefined =  __config.get("projectDomainName");
```


The name of the domain where the project resides (Identity v3).

<h2 class="pdoc-module-header" id="region">
<a class="pdoc-member-name" href="/config/vars.ts#L60">let region</a>
</h2>

```typescript
let region: string | undefined =  __config.get("region");
```


The OpenStack region to connect to.

<h2 class="pdoc-module-header" id="swauth">
<a class="pdoc-member-name" href="/config/vars.ts#L64">let swauth</a>
</h2>

```typescript
let swauth: boolean | undefined =  __config.getObject<boolean>("swauth");
```


Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.

<h2 class="pdoc-module-header" id="tenantId">
<a class="pdoc-member-name" href="/config/vars.ts#L68">let tenantId</a>
</h2>

```typescript
let tenantId: string | undefined =  __config.get("tenantId");
```


The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h2 class="pdoc-module-header" id="tenantName">
<a class="pdoc-member-name" href="/config/vars.ts#L72">let tenantName</a>
</h2>

```typescript
let tenantName: string | undefined =  __config.get("tenantName");
```


The name of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h2 class="pdoc-module-header" id="token">
<a class="pdoc-member-name" href="/config/vars.ts#L76">let token</a>
</h2>

```typescript
let token: string | undefined =  __config.get("token");
```


Authentication token to use as an alternative to username/password.

<h2 class="pdoc-module-header" id="useOctavia">
<a class="pdoc-member-name" href="/config/vars.ts#L80">let useOctavia</a>
</h2>

```typescript
let useOctavia: boolean | undefined =  __config.getObject<boolean>("useOctavia");
```


If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).

<h2 class="pdoc-module-header" id="userDomainId">
<a class="pdoc-member-name" href="/config/vars.ts#L84">let userDomainId</a>
</h2>

```typescript
let userDomainId: string | undefined =  __config.get("userDomainId");
```


The ID of the domain where the user resides (Identity v3).

<h2 class="pdoc-module-header" id="userDomainName">
<a class="pdoc-member-name" href="/config/vars.ts#L88">let userDomainName</a>
</h2>

```typescript
let userDomainName: string | undefined =  __config.get("userDomainName");
```


The name of the domain where the user resides (Identity v3).

<h2 class="pdoc-module-header" id="userId">
<a class="pdoc-member-name" href="/config/vars.ts#L92">let userId</a>
</h2>

```typescript
let userId: string | undefined =  __config.get("userId");
```


Username to login with.

<h2 class="pdoc-module-header" id="userName">
<a class="pdoc-member-name" href="/config/vars.ts#L96">let userName</a>
</h2>

```typescript
let userName: string | undefined =  __config.get("userName");
```


Username to login with.

