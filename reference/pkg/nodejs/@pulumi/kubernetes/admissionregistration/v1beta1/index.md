---
title: Module admissionregistration/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">admissionregistration</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isMutatingWebhookConfiguration">function isMutatingWebhookConfiguration</a>
* <a href="#isMutatingWebhookConfigurationList">function isMutatingWebhookConfigurationList</a>
* <a href="#isValidatingWebhookConfiguration">function isValidatingWebhookConfiguration</a>
* <a href="#isValidatingWebhookConfigurationList">function isValidatingWebhookConfigurationList</a>
* <a href="#MutatingWebhookConfiguration">interface MutatingWebhookConfiguration</a>
* <a href="#MutatingWebhookConfigurationList">interface MutatingWebhookConfigurationList</a>
* <a href="#RuleWithOperations">interface RuleWithOperations</a>
* <a href="#ServiceReference">interface ServiceReference</a>
* <a href="#ValidatingWebhookConfiguration">interface ValidatingWebhookConfiguration</a>
* <a href="#ValidatingWebhookConfigurationList">interface ValidatingWebhookConfigurationList</a>
* <a href="#Webhook">interface Webhook</a>
* <a href="#WebhookClientConfig">interface WebhookClientConfig</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isMutatingWebhookConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L179">function isMutatingWebhookConfiguration</a>
</h2>

```typescript
isMutatingWebhookConfiguration(o: any): boolean
```

<h2 class="pdoc-module-header" id="isMutatingWebhookConfigurationList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L216">function isMutatingWebhookConfigurationList</a>
</h2>

```typescript
isMutatingWebhookConfigurationList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isValidatingWebhookConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L316">function isValidatingWebhookConfiguration</a>
</h2>

```typescript
isValidatingWebhookConfiguration(o: any): boolean
```

<h2 class="pdoc-module-header" id="isValidatingWebhookConfigurationList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L353">function isValidatingWebhookConfigurationList</a>
</h2>

```typescript
isValidatingWebhookConfigurationList(o: any): boolean
```

<h2 class="pdoc-module-header" id="MutatingWebhookConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L137">interface MutatingWebhookConfiguration</a>
</h2>

MutatingWebhookConfiguration describes the configuration of and admission webhook that accept
or reject and may change the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L144">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L152">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L158">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L163">property webhooks</a>
</h3>

```typescript
webhooks: Webhook[];
```


Webhooks is a list of webhooks and the affected resources and operations.

<h2 class="pdoc-module-header" id="MutatingWebhookConfigurationList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L170">interface MutatingWebhookConfigurationList</a>
</h2>

MutatingWebhookConfigurationList is a list of MutatingWebhookConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L177">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L182">property items</a>
</h3>

```typescript
items: MutatingWebhookConfiguration[];
```


List of MutatingWebhookConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L190">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L196">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="RuleWithOperations">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L204">interface RuleWithOperations</a>
</h2>

RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure
that all the tuple expansions are valid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L209">property apiGroups</a>
</h3>

```typescript
apiGroups: string[];
```


APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present,
the length of the slice must be one. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L215">property apiVersions</a>
</h3>

```typescript
apiVersions: string[];
```


APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is
present, the length of the slice must be one. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L221">property operations</a>
</h3>

```typescript
operations: string[];
```


Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all
operations. If '*' is present, the length of the slice must be one. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L235">property resources</a>
</h3>

```typescript
resources: string[];
```


Resources is a list of resources this rule applies to.

For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all
resources, but not subresources. 'pods/*' means all subresources of pods. '*&#8205;/scale'
means all scale subresources. '*&#8205;/*' means all resources and their subresources.

If wildcard is present, the validation rule will ensure resources do not overlap with each
other.

Depending on the enclosing object, subresources might not be allowed. Required.

<h2 class="pdoc-module-header" id="ServiceReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L242">interface ServiceReference</a>
</h2>

ServiceReference holds a reference to Service.legacy.k8s.io

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L246">property name</a>
</h3>

```typescript
name: string;
```


`name` is the name of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L251">property namespace</a>
</h3>

```typescript
namespace: string;
```


`namespace` is the namespace of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L256">property path</a>
</h3>

```typescript
path: string;
```


`path` is an optional URL path which will be sent in any request to this service.

<h2 class="pdoc-module-header" id="ValidatingWebhookConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L264">interface ValidatingWebhookConfiguration</a>
</h2>

ValidatingWebhookConfiguration describes the configuration of and admission webhook that
accept or reject and object without changing it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L271">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L279">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L285">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L290">property webhooks</a>
</h3>

```typescript
webhooks: Webhook[];
```


Webhooks is a list of webhooks and the affected resources and operations.

<h2 class="pdoc-module-header" id="ValidatingWebhookConfigurationList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L297">interface ValidatingWebhookConfigurationList</a>
</h2>

ValidatingWebhookConfigurationList is a list of ValidatingWebhookConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L304">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L309">property items</a>
</h3>

```typescript
items: ValidatingWebhookConfiguration[];
```


List of ValidatingWebhookConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L317">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L323">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="Webhook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L330">interface Webhook</a>
</h2>

Webhook describes an admission webhook and the resources and operations it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L334">property clientConfig</a>
</h3>

```typescript
clientConfig: WebhookClientConfig;
```


ClientConfig defines how to communicate with the hook. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L340">property failurePolicy</a>
</h3>

```typescript
failurePolicy: string;
```


FailurePolicy defines how unrecognized errors from the admission endpoint are handled -
allowed values are Ignore or Fail. Defaults to Ignore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L347">property name</a>
</h3>

```typescript
name: string;
```


The name of the admission webhook. Name should be fully qualified, e.g.,
imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and
kubernetes.io is the name of the organization. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L389">property namespaceSelector</a>
</h3>

```typescript
namespaceSelector: LabelSelector;
```


NamespaceSelector decides whether to run the webhook on an object based on whether the
namespace for that object matches the selector. If the object itself is a namespace, the
matching is performed on object.metadata.labels. If the object is another cluster scoped
resource, it never skips the webhook.

For example, to run the webhook on any objects whose namespace is not associated with
"runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {
  "matchExpressions": [
    {
      "key": "runlevel",
      "operator": "NotIn",
      "values": [
        "0",
        "1"
      ]
    }
  ]
}

If instead you want to only run the webhook on any objects whose namespace is associated
with the "environment" of "prod" or "staging"; you will set the selector as follows:
"namespaceSelector": {
  "matchExpressions": [
    {
      "key": "environment",
      "operator": "In",
      "values": [
        "prod",
        "staging"
      ]
    }
  ]
}

See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more
examples of label selectors.

Default to the empty LabelSelector, which matches everything.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L395">property rules</a>
</h3>

```typescript
rules: RuleWithOperations[];
```


Rules describes what operations on what resources/subresources the webhook cares about. The
webhook cares about an operation if it matches _any_ Rule.

<h2 class="pdoc-module-header" id="WebhookClientConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L402">interface WebhookClientConfig</a>
</h2>

WebhookClientConfig contains the information to make a TLS connection with the webhook

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L407">property caBundle</a>
</h3>

```typescript
caBundle: string;
```


`caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server
certificate. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L418">property service</a>
</h3>

```typescript
service: ServiceReference;
```


`service` is a reference to the service for this webhook. Either `service` or `url` must be
specified.

If the webhook is running within the cluster, then you should use `service`.

If there is only one port open for the service, that port will be used. If there are
multiple ports open, port 443 will be used if it is open, otherwise it is an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L442">property url</a>
</h3>

```typescript
url: string;
```


`url` gives the location of the webhook, in standard URL form
(`[scheme://]host:port/path`). Exactly one of `url` or `service` must be specified.

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

