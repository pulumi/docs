---
title: Module auditregistration/v1alpha1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">auditregistration</a> &gt; v1alpha1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isAuditSink">function isAuditSink</a>
* <a href="#isAuditSinkList">function isAuditSinkList</a>
* <a href="#AuditSink">interface AuditSink</a>
* <a href="#AuditSinkList">interface AuditSinkList</a>
* <a href="#AuditSinkSpec">interface AuditSinkSpec</a>
* <a href="#Policy">interface Policy</a>
* <a href="#ServiceReference">interface ServiceReference</a>
* <a href="#Webhook">interface Webhook</a>
* <a href="#WebhookClientConfig">interface WebhookClientConfig</a>
* <a href="#WebhookThrottleConfig">interface WebhookThrottleConfig</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isAuditSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4592">function isAuditSink</a>
</h2>

```typescript
isAuditSink(o: any): boolean
```

<h2 class="pdoc-module-header" id="isAuditSinkList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4626">function isAuditSinkList</a>
</h2>

```typescript
isAuditSinkList(o: any): boolean
```

<h2 class="pdoc-module-header" id="AuditSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4320">interface AuditSink</a>
</h2>

AuditSink represents a cluster level audit sink

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4327">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4335">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4338">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4343">property spec</a>
</h3>

```typescript
spec: AuditSinkSpec;
```


Spec defines the audit configuration spec

<h2 class="pdoc-module-header" id="AuditSinkList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4350">interface AuditSinkList</a>
</h2>

AuditSinkList is a list of AuditSink items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4357">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4362">property items</a>
</h3>

```typescript
items: AuditSink[];
```


List of audit configurations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4370">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4373">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="AuditSinkSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4380">interface AuditSinkSpec</a>
</h2>

AuditSinkSpec holds the spec for the audit sink

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4384">property policy</a>
</h3>

```typescript
policy: Policy;
```


Policy defines the policy for selecting which events should be sent to the webhook required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4389">property webhook</a>
</h3>

```typescript
webhook: Webhook;
```


Webhook to send events required

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4396">interface Policy</a>
</h2>

Policy defines the configuration of how audit events are logged

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4401">property level</a>
</h3>

```typescript
level: string;
```


The Level that all requests are recorded at. available options: None, Metadata, Request,
RequestResponse required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4406">property stages</a>
</h3>

```typescript
stages: string[];
```


Stages is a list of stages for which events are created.

<h2 class="pdoc-module-header" id="ServiceReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4413">interface ServiceReference</a>
</h2>

ServiceReference holds a reference to Service.legacy.k8s.io

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4417">property name</a>
</h3>

```typescript
name: string;
```


`name` is the name of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4422">property namespace</a>
</h3>

```typescript
namespace: string;
```


`namespace` is the namespace of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4427">property path</a>
</h3>

```typescript
path: string;
```


`path` is an optional URL path which will be sent in any request to this service.

<h2 class="pdoc-module-header" id="Webhook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4434">interface Webhook</a>
</h2>

Webhook holds the configuration of the webhook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4438">property clientConfig</a>
</h3>

```typescript
clientConfig: WebhookClientConfig;
```


ClientConfig holds the connection parameters for the webhook required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4443">property throttle</a>
</h3>

```typescript
throttle: WebhookThrottleConfig;
```


Throttle holds the options for throttling the webhook

<h2 class="pdoc-module-header" id="WebhookClientConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4450">interface WebhookClientConfig</a>
</h2>

WebhookClientConfig contains the information to make a connection with the webhook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4455">property caBundle</a>
</h3>

```typescript
caBundle: string;
```


`caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server
certificate. If unspecified, system trust roots on the apiserver are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4465">property service</a>
</h3>

```typescript
service: ServiceReference;
```


`service` is a reference to the service for this webhook. Either `service` or `url` must be
specified.

If the webhook is running within the cluster, then you should use `service`.

Port 443 will be used if it is open, otherwise it is an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4489">property url</a>
</h3>

```typescript
url: string;
```


`url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`).
Exactly one of `url` or `service` must be specified.

The `host` should not refer to a service running in the cluster; use the `service` field
instead. The host might be resolved via external DNS in some apiservers (e.g.,
`kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation).
`host` may also be an IP address.

Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take
great care to run this webhook on all hosts which run an apiserver which might need to make
calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn
up in a new cluster.

The scheme must be "https"; the URL must begin with "https://".

A path is optional, and if present may be any string permissible in a URL. You may use the
path to pass an arbitrary string to the webhook, for example, a cluster identifier.

Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments
("#...") and query parameters ("?...") are not allowed, either.

<h2 class="pdoc-module-header" id="WebhookThrottleConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4496">interface WebhookThrottleConfig</a>
</h2>

WebhookThrottleConfig holds the configuration for throttling events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4500">property burst</a>
</h3>

```typescript
burst: number;
```


ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4505">property qps</a>
</h3>

```typescript
qps: number;
```


ThrottleQPS maximum number of batches per second default 10 QPS

