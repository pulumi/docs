---
title: Module apiregistration/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apiregistration</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isAPIService">function isAPIService</a>
* <a href="#isAPIServiceList">function isAPIServiceList</a>
* <a href="#APIService">interface APIService</a>
* <a href="#APIServiceCondition">interface APIServiceCondition</a>
* <a href="#APIServiceList">interface APIServiceList</a>
* <a href="#APIServiceSpec">interface APIServiceSpec</a>
* <a href="#APIServiceStatus">interface APIServiceStatus</a>
* <a href="#ServiceReference">interface ServiceReference</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isAPIService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L1357">function isAPIService</a>
</h2>

```typescript
isAPIService(o: any): boolean
```

<h2 class="pdoc-module-header" id="isAPIServiceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L1419">function isAPIServiceList</a>
</h2>

```typescript
isAPIServiceList(o: any): boolean
```

<h2 class="pdoc-module-header" id="APIService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1259">interface APIService</a>
</h2>

APIService represents a server for a particular GroupVersion. Name must be "version.group".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1266">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1274">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1277">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1282">property spec</a>
</h3>

```typescript
spec: APIServiceSpec;
```


Spec contains information for locating and communicating with a server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1287">property status</a>
</h3>

```typescript
status: APIServiceStatus;
```


Status contains derived information about an API server

<h2 class="pdoc-module-header" id="APIServiceCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1292">interface APIServiceCondition</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1296">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1301">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1306">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, one-word, CamelCase reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1311">property status</a>
</h3>

```typescript
status: string;
```


Status is the status of the condition. Can be True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1316">property type</a>
</h3>

```typescript
type: string;
```


Type is the type of the condition.

<h2 class="pdoc-module-header" id="APIServiceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1323">interface APIServiceList</a>
</h2>

APIServiceList is a list of APIService objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1330">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1333">property items</a>
</h3>

```typescript
items: APIService[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1341">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1344">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="APIServiceSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1352">interface APIServiceSpec</a>
</h2>

APIServiceSpec contains information for locating and communicating with a server. Only https
is supported, though you are able to disable certificate verification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1357">property caBundle</a>
</h3>

```typescript
caBundle: string;
```


CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving
certificate. If unspecified, system trust roots on the apiserver are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1362">property group</a>
</h3>

```typescript
group: string;
```


Group is the API group name this server hosts

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1374">property groupPriorityMinimum</a>
</h3>

```typescript
groupPriorityMinimum: number;
```


GroupPriorityMininum is the priority this group should have at least. Higher priority means
that the group is preferred by clients over lower priority ones. Note that other versions
of this group might specify even higher GroupPriorityMininum values such that the whole
group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered
highest number to lowest (20 before 10). The secondary sort is based on the alphabetical
comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something
like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to
be in the 2000s

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1380">property insecureSkipTLSVerify</a>
</h3>

```typescript
insecureSkipTLSVerify: boolean;
```


InsecureSkipTLSVerify disables TLS certificate verification when communicating with this
server. This is strongly discouraged.  You should use the CABundle instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1387">property service</a>
</h3>

```typescript
service: ServiceReference;
```


Service is a reference to the service for this API server.  It must communicate on port 443
If the Service is nil, that means the handling for the API groupversion is handled locally
on this server. The call will simply delegate to the normal handler chain to be fulfilled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1392">property version</a>
</h3>

```typescript
version: string;
```


Version is the API version this server hosts.  For example, "v1"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1407">property versionPriority</a>
</h3>

```typescript
versionPriority: number;
```


VersionPriority controls the ordering of this API version inside of its group.  Must be
greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest
(20 before 10). Since it's inside of a group, the number can be small, probably in the 10s.
In case of equal version priorities, the version string will be used to compute the order
inside a group. If the version string is "kube-like", it will sort above non "kube-like"
version strings, which are ordered lexicographically. "Kube-like" versions start with a
"v", then are followed by a number (the major version), then optionally the string "alpha"
or "beta" and another number (the minor version). These are sorted first by GA > beta >
alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing
major version, then minor version. An example sorted list of versions: v10, v2, v1,
v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.

<h2 class="pdoc-module-header" id="APIServiceStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1414">interface APIServiceStatus</a>
</h2>

APIServiceStatus contains derived information about an API server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1418">property conditions</a>
</h3>

```typescript
conditions: APIServiceCondition[];
```


Current service state of apiService.

<h2 class="pdoc-module-header" id="ServiceReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1425">interface ServiceReference</a>
</h2>

ServiceReference holds a reference to Service.legacy.k8s.io

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1429">property name</a>
</h3>

```typescript
name: string;
```


Name is the name of the service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1434">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace is the namespace of the service

