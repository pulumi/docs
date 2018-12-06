---
title: Module certificates/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">certificates</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCertificateSigningRequest">function isCertificateSigningRequest</a>
* <a href="#isCertificateSigningRequestList">function isCertificateSigningRequestList</a>
* <a href="#CertificateSigningRequest">interface CertificateSigningRequest</a>
* <a href="#CertificateSigningRequestCondition">interface CertificateSigningRequestCondition</a>
* <a href="#CertificateSigningRequestList">interface CertificateSigningRequestList</a>
* <a href="#CertificateSigningRequestSpec">interface CertificateSigningRequestSpec</a>
* <a href="#CertificateSigningRequestStatus">interface CertificateSigningRequestStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCertificateSigningRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L7840">function isCertificateSigningRequest</a>
</h2>

```typescript
isCertificateSigningRequest(o: any): boolean
```

<h2 class="pdoc-module-header" id="isCertificateSigningRequestList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L7895">function isCertificateSigningRequestList</a>
</h2>

```typescript
isCertificateSigningRequestList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CertificateSigningRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7379">interface CertificateSigningRequest</a>
</h2>

Describes a certificate signing request

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7386">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7394">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7397">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7402">property spec</a>
</h3>

```typescript
spec: CertificateSigningRequestSpec;
```


The certificate request itself and any additional information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7407">property status</a>
</h3>

```typescript
status: CertificateSigningRequestStatus;
```


Derived information about the request.

<h2 class="pdoc-module-header" id="CertificateSigningRequestCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7412">interface CertificateSigningRequestCondition</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7416">property lastUpdateTime</a>
</h3>

```typescript
lastUpdateTime: string;
```


timestamp for the last update to this condition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7421">property message</a>
</h3>

```typescript
message: string;
```


human readable message with details about the request state

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7426">property reason</a>
</h3>

```typescript
reason: string;
```


brief reason for the request state

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7431">property type</a>
</h3>

```typescript
type: string;
```


request approval state, currently Approved or Denied.

<h2 class="pdoc-module-header" id="CertificateSigningRequestList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7436">interface CertificateSigningRequestList</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7443">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7446">property items</a>
</h3>

```typescript
items: CertificateSigningRequest[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7454">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7457">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="CertificateSigningRequestSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7466">interface CertificateSigningRequestSpec</a>
</h2>

This information is immutable after the request is created. Only the Request and Usages
fields can be set on creation, other fields are derived by Kubernetes and cannot be modified
by users.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7470">property extra</a>
</h3>

```typescript
extra: object;
```


Extra information about the requesting user. See user.Info interface for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7475">property groups</a>
</h3>

```typescript
groups: string[];
```


Group information about the requesting user. See user.Info interface for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7480">property request</a>
</h3>

```typescript
request: string;
```


Base64-encoded PKCS#10 CSR data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7485">property uid</a>
</h3>

```typescript
uid: string;
```


UID information about the requesting user. See user.Info interface for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7492">property usages</a>
</h3>

```typescript
usages: string[];
```


allowedUsages specifies a set of usage contexts the key will be valid for. See:
https://tools.ietf.org/html/rfc5280#section-4.2.1.3
     https://tools.ietf.org/html/rfc5280#section-4.2.1.12

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7497">property username</a>
</h3>

```typescript
username: string;
```


Information about the requesting user. See user.Info interface for details.

<h2 class="pdoc-module-header" id="CertificateSigningRequestStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7502">interface CertificateSigningRequestStatus</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7506">property certificate</a>
</h3>

```typescript
certificate: string;
```


If request was approved, the controller will place the issued certificate here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7511">property conditions</a>
</h3>

```typescript
conditions: CertificateSigningRequestCondition[];
```


Conditions applied to the request, such as approval or denial.

