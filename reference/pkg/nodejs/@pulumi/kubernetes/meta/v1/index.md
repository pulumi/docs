---
title: Module meta/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">meta</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#APIGroup">interface APIGroup</a>
* <a href="#APIGroupList">interface APIGroupList</a>
* <a href="#APIResource">interface APIResource</a>
* <a href="#APIResourceList">interface APIResourceList</a>
* <a href="#APIVersions">interface APIVersions</a>
* <a href="#DeleteOptions">interface DeleteOptions</a>
* <a href="#GroupVersionForDiscovery">interface GroupVersionForDiscovery</a>
* <a href="#Initializer">interface Initializer</a>
* <a href="#Initializers">interface Initializers</a>
* <a href="#LabelSelector">interface LabelSelector</a>
* <a href="#LabelSelectorRequirement">interface LabelSelectorRequirement</a>
* <a href="#ListMeta">interface ListMeta</a>
* <a href="#ObjectMeta">interface ObjectMeta</a>
* <a href="#OwnerReference">interface OwnerReference</a>
* <a href="#Preconditions">interface Preconditions</a>
* <a href="#ServerAddressByClientCIDR">interface ServerAddressByClientCIDR</a>
* <a href="#Status">interface Status</a>
* <a href="#StatusCause">interface StatusCause</a>
* <a href="#StatusDetails">interface StatusDetails</a>
* <a href="#WatchEvent">interface WatchEvent</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="APIGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13648">interface APIGroup</a>
</h2>

APIGroup contains the name, the supported versions, and the preferred version of a group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13655">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13663">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13668">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13674">property preferredVersion</a>
</h3>

```typescript
preferredVersion: GroupVersionForDiscovery;
```


preferredVersion is the version preferred by the API server, which probably is the storage
version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13685">property serverAddressByClientCIDRs</a>
</h3>

```typescript
serverAddressByClientCIDRs: ServerAddressByClientCIDR[];
```


a map of client CIDR to server address that is serving this group. This is to help clients
reach servers in the most network-efficient way possible. Clients can use the appropriate
server address as per the CIDR that they match. In case of multiple matches, clients should
use the longest matching CIDR. The server returns only those CIDRs that it thinks that the
client can match. For example: the master will return an internal IP CIDR only, if the
client reaches the server using an internal IP. Server looks at X-Forwarded-For header or
X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13690">property versions</a>
</h3>

```typescript
versions: GroupVersionForDiscovery[];
```


versions are the versions supported in this group.

<h2 class="pdoc-module-header" id="APIGroupList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13697">interface APIGroupList</a>
</h2>

APIGroupList is a list of APIGroup, to allow clients to discover the API at /apis.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13704">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13709">property groups</a>
</h3>

```typescript
groups: APIGroup[];
```


groups is a list of APIGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13717">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="APIResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13724">interface APIResource</a>
</h2>

APIResource specifies the name of a resource and whether it is namespaced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13728">property categories</a>
</h3>

```typescript
categories: string[];
```


categories is a list of the grouped resources this resource belongs to (e.g. 'all')

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13734">property group</a>
</h3>

```typescript
group: string;
```


group is the preferred group of the resource.  Empty implies the group of the containing
resource list. For subresources, this may have a different value, for example: Scale".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13739">property kind</a>
</h3>

```typescript
kind: string;
```


kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13744">property name</a>
</h3>

```typescript
name: string;
```


name is the plural name of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13749">property namespaced</a>
</h3>

```typescript
namespaced: boolean;
```


namespaced indicates if a resource is namespaced or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13754">property shortNames</a>
</h3>

```typescript
shortNames: string[];
```


shortNames is a list of suggested short names of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13761">property singularName</a>
</h3>

```typescript
singularName: string;
```


singularName is the singular name of the resource.  This allows clients to handle plural
and singular opaquely. The singularName is more correct for reporting status on a single
item and both singular and plural are allowed from the kubectl CLI interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13767">property verbs</a>
</h3>

```typescript
verbs: string[];
```


verbs is a list of supported kube verbs (this includes get, list, watch, create, update,
patch, delete, deletecollection, and proxy)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13774">property version</a>
</h3>

```typescript
version: string;
```


version is the preferred version of the resource.  Empty implies the version of the
containing resource list For subresources, this may have a different value, for example: v1
(while inside a v1beta1 version of the core resource's group)".

<h2 class="pdoc-module-header" id="APIResourceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13782">interface APIResourceList</a>
</h2>

APIResourceList is a list of APIResource, it is used to expose the name of the resources
supported in a specific group and version, and if the resource is namespaced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13789">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13794">property groupVersion</a>
</h3>

```typescript
groupVersion: string;
```


groupVersion is the group and version this APIResourceList is for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13802">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13807">property resources</a>
</h3>

```typescript
resources: APIResource[];
```


resources contains the name of the resources and if they are namespaced.

<h2 class="pdoc-module-header" id="APIVersions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13815">interface APIVersions</a>
</h2>

APIVersions lists the versions that are available, to allow clients to discover the API at
/api, which is the root path of the legacy v1 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13822">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13830">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13841">property serverAddressByClientCIDRs</a>
</h3>

```typescript
serverAddressByClientCIDRs: ServerAddressByClientCIDR[];
```


a map of client CIDR to server address that is serving this group. This is to help clients
reach servers in the most network-efficient way possible. Clients can use the appropriate
server address as per the CIDR that they match. In case of multiple matches, clients should
use the longest matching CIDR. The server returns only those CIDRs that it thinks that the
client can match. For example: the master will return an internal IP CIDR only, if the
client reaches the server using an internal IP. Server looks at X-Forwarded-For header or
X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13846">property versions</a>
</h3>

```typescript
versions: string[];
```


versions are the api versions that are available.

<h2 class="pdoc-module-header" id="DeleteOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13853">interface DeleteOptions</a>
</h2>

DeleteOptions may be provided when deleting an API object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13860">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13868">property gracePeriodSeconds</a>
</h3>

```typescript
gracePeriodSeconds: number;
```


The duration in seconds before the object should be deleted. Value must be non-negative
integer. The value zero indicates delete immediately. If this value is nil, the default
grace period for the specified type will be used. Defaults to a per object value if not
specified. zero means delete immediately.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13876">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13884">property orphanDependents</a>
</h3>

```typescript
orphanDependents: boolean;
```


Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should
the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added
to/removed from the object's finalizers list. Either this field or PropagationPolicy may be
set, but not both.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13890">property preconditions</a>
</h3>

```typescript
preconditions: Preconditions;
```


Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status
will be returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13900">property propagationPolicy</a>
</h3>

```typescript
propagationPolicy: string;
```


Whether and how garbage collection will be performed. Either this field or OrphanDependents
may be set, but not both. The default policy is decided by the existing finalizer set in
the metadata.finalizers and the resource-specific default policy. Acceptable values are:
'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the
dependents in the background; 'Foreground' - a cascading policy that deletes all dependents
in the foreground.

<h2 class="pdoc-module-header" id="GroupVersionForDiscovery">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13908">interface GroupVersionForDiscovery</a>
</h2>

GroupVersion contains the "group/version" and "version" string of a version. It is made a
struct to keep extensibility.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13912">property groupVersion</a>
</h3>

```typescript
groupVersion: string;
```


groupVersion specifies the API group and version in the form "group/version"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13918">property version</a>
</h3>

```typescript
version: string;
```


version specifies the version in the form of "version". This is to save the clients the
trouble of splitting the GroupVersion.

<h2 class="pdoc-module-header" id="Initializer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13925">interface Initializer</a>
</h2>

Initializer is information about an initializer that has not yet completed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13929">property name</a>
</h3>

```typescript
name: string;
```


name of the process that is responsible for initializing this object.

<h2 class="pdoc-module-header" id="Initializers">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13936">interface Initializers</a>
</h2>

Initializers tracks the progress of initialization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13943">property pending</a>
</h3>

```typescript
pending: Initializer[];
```


Pending is a list of initializers that must execute in order before this object is visible.
When the last pending initializer is removed, and no failing result is set, the
initializers struct will be set to nil and the object is considered as initialized and
visible to all clients.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13949">property result</a>
</h3>

```typescript
result: Status;
```


If result is set with the Failure field, the object will be persisted to storage and then
deleted, ensuring that other clients can observe the deletion.

<h2 class="pdoc-module-header" id="LabelSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13958">interface LabelSelector</a>
</h2>

A label selector is a label query over a set of resources. The result of matchLabels and
matchExpressions are ANDed. An empty label selector matches all objects. A null label
selector matches no objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13962">property matchExpressions</a>
</h3>

```typescript
matchExpressions: LabelSelectorRequirement[];
```


matchExpressions is a list of label selector requirements. The requirements are ANDed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13969">property matchLabels</a>
</h3>

```typescript
matchLabels: object;
```


matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is
equivalent to an element of matchExpressions, whose key field is "key", the operator is
"In", and the values array contains only "value". The requirements are ANDed.

<h2 class="pdoc-module-header" id="LabelSelectorRequirement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13977">interface LabelSelectorRequirement</a>
</h2>

A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13981">property key</a>
</h3>

```typescript
key: string;
```


key is the label key that the selector applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13987">property operator</a>
</h3>

```typescript
operator: string;
```


operator represents a key's relationship to a set of values. Valid operators are In, NotIn,
Exists and DoesNotExist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13994">property values</a>
</h3>

```typescript
values: string[];
```


values is an array of string values. If the operator is In or NotIn, the values array must
be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty.
This array is replaced during a strategic merge patch.

<h2 class="pdoc-module-header" id="ListMeta">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14002">interface ListMeta</a>
</h2>

ListMeta describes metadata that synthetic resources must have, including lists and various
status objects. A resource may have only one of {ObjectMeta, ListMeta}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14011">property continue</a>
</h3>

```typescript
continue: string;
```


continue may be set if the user set a limit on the number of items returned, and indicates
that the server has more data available. The value is opaque and may be used to issue
another request to the endpoint that served this list to retrieve the next set of available
objects. Continuing a list may not be possible if the server configuration has changed or
more than a few minutes have passed. The resourceVersion field returned when using this
continue value will be identical to the value in the first response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14019">property resourceVersion</a>
</h3>

```typescript
resourceVersion: string;
```


String that identifies the server's internal version of this object that can be used by
clients to determine when objects have changed. Value must be treated as opaque by clients
and passed unmodified back to the server. Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14024">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


selfLink is a URL representing this object. Populated by the system. Read-only.

<h2 class="pdoc-module-header" id="ObjectMeta">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14032">interface ObjectMeta</a>
</h2>

ObjectMeta is metadata that all persisted resources must have, which includes all objects
users must create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14039">property annotations</a>
</h3>

```typescript
annotations: object;
```


Annotations is an unstructured key value map stored with a resource that may be set by
external tools to store and retrieve arbitrary metadata. They are not queryable and should
be preserved when modifying objects. More info:
http://kubernetes.io/docs/user-guide/annotations

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14046">property clusterName</a>
</h3>

```typescript
clusterName: string;
```


The name of the cluster which the object belongs to. This is used to distinguish resources
with same name and namespace in different clusters. This field is not set anywhere right
now and apiserver is going to ignore it if set in create or update request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14056">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp: string;
```


CreationTimestamp is a timestamp representing the server time when this object was created.
It is not guaranteed to be set in happens-before order across separate operations. Clients
may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14063">property deletionGracePeriodSeconds</a>
</h3>

```typescript
deletionGracePeriodSeconds: number;
```


Number of seconds allowed for this object to gracefully terminate before it will be removed
from the system. Only set when deletionTimestamp is also set. May only be shortened.
Read-only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14084">property deletionTimestamp</a>
</h3>

```typescript
deletionTimestamp: string;
```


DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This
field is set by the server when a graceful deletion is requested by the user, and is not
directly settable by a client. The resource is expected to be deleted (no longer visible
from resource lists, and not reachable by name) after the time in this field, once the
finalizers list is empty. As long as the finalizers list contains items, deletion is
blocked. Once the deletionTimestamp is set, this value may not be unset or be set further
into the future, although it may be shortened or the resource may be deleted prior to this
time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will
react by sending a graceful termination signal to the containers in the pod. After that 30
seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and
after cleanup, remove the pod from the API. In the presence of network partitions, this
object may still exist after this timestamp, until an administrator or automated process
can determine the resource is fully terminated. If not set, graceful deletion of the object
has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14091">property finalizers</a>
</h3>

```typescript
finalizers: string[];
```


Must be empty before the object is deleted from the registry. Each entry is an identifier
for the responsible component that will remove the entry from the list. If the
deletionTimestamp of the object is non-nil, entries in this list can only be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14108">property generateName</a>
</h3>

```typescript
generateName: string;
```


GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF
the Name field has not been provided. If this field is used, the name returned to the
client will be different than the name passed. This value will also be combined with a
unique suffix. The provided value has the same validation rules as the Name field, and may
be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409
- instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a
unique name could not be found in the time allotted, and the client should retry
(optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#idempotency

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14114">property generation</a>
</h3>

```typescript
generation: number;
```


A sequence number representing a specific generation of the desired state. Populated by the
system. Read-only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14127">property initializers</a>
</h3>

```typescript
initializers: Initializers;
```


An initializer is a controller which enforces some system invariant at object creation
time. This field is a list of initializers that have not yet acted on this object. If nil
or empty, this object has been completely initialized. Otherwise, the object is considered
uninitialized and is hidden (in list/watch and get calls) from clients that haven't
explicitly asked to observe uninitialized objects.

When an object is created, the system will populate this list with the current set of
initializers. Only privileged users may set or modify this list. Once it is empty, it may
not be modified further by any user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14134">property labels</a>
</h3>

```typescript
labels: object;
```


Map of string keys and values that can be used to organize and categorize (scope and
select) objects. May match selectors of replication controllers and services. More info:
http://kubernetes.io/docs/user-guide/labels

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14143">property name</a>
</h3>

```typescript
name: string;
```


Name must be unique within a namespace. Is required when creating resources, although some
resources may allow a client to request the generation of an appropriate name
automatically. Name is primarily intended for creation idempotence and configuration
definition. Cannot be updated. More info:
http://kubernetes.io/docs/user-guide/identifiers#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14154">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace defines the space within each name must be unique. An empty namespace is
equivalent to the "default" namespace, but "default" is the canonical representation. Not
all objects are required to be scoped to a namespace - the value of this field for those
objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info:
http://kubernetes.io/docs/user-guide/namespaces

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14162">property ownerReferences</a>
</h3>

```typescript
ownerReferences: OwnerReference[];
```


List of objects depended by this object. If ALL objects in the list have been deleted, this
object will be garbage collected. If this object is managed by a controller, then an entry
in this list will point to this controller, with the controller field set to true. There
cannot be more than one managing controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14175">property resourceVersion</a>
</h3>

```typescript
resourceVersion: string;
```


An opaque value that represents the internal version of this object that can be used by
clients to determine when objects have changed. May be used for optimistic concurrency,
change detection, and the watch operation on a resource or set of resources. Clients must
treat these values as opaque and passed unmodified back to the server. They may only be
valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More
info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14180">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


SelfLink is a URL representing this object. Populated by the system. Read-only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14189">property uid</a>
</h3>

```typescript
uid: string;
```


UID is the unique in time and space value for this object. It is typically generated by the
server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info:
http://kubernetes.io/docs/user-guide/identifiers#uids

<h2 class="pdoc-module-header" id="OwnerReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14197">interface OwnerReference</a>
</h2>

OwnerReference contains enough information to let you identify an owning object. Currently,
an owning object must be in the same namespace, so there is no namespace field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14201">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14209">property blockOwnerDeletion</a>
</h3>

```typescript
blockOwnerDeletion: boolean;
```


If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be
deleted from the key-value store until this reference is removed. Defaults to false. To set
this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable
Entity) will be returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14214">property controller</a>
</h3>

```typescript
controller: boolean;
```


If true, this reference points to the managing controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14220">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14225">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14230">property uid</a>
</h3>

```typescript
uid: string;
```


UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

<h2 class="pdoc-module-header" id="Preconditions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14237">interface Preconditions</a>
</h2>

Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14241">property uid</a>
</h3>

```typescript
uid: string;
```


Specifies the target UID.

<h2 class="pdoc-module-header" id="ServerAddressByClientCIDR">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14249">interface ServerAddressByClientCIDR</a>
</h2>

ServerAddressByClientCIDR helps the client to determine the server address that they should
use, depending on the clientCIDR that they match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14254">property clientCIDR</a>
</h3>

```typescript
clientCIDR: string;
```


The CIDR with which clients can match their IP to figure out the server address that they
should use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14260">property serverAddress</a>
</h3>

```typescript
serverAddress: string;
```


Address of this server, suitable for a client that matches the above CIDR. This can be a
hostname, hostname:port, IP or IP:port.

<h2 class="pdoc-module-header" id="Status">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14267">interface Status</a>
</h2>

Status is a return value for calls that don't return other objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14274">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14279">property code</a>
</h3>

```typescript
code: number;
```


Suggested HTTP return code for this status, 0 if not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14286">property details</a>
</h3>

```typescript
details: StatusDetails;
```


Extended data associated with the reason.  Each reason may define its own extended details.
This field is optional and the data returned is not guaranteed to conform to any schema
except that defined by the reason type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14294">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14299">property message</a>
</h3>

```typescript
message: string;
```


A human-readable description of the status of this operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14305">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14312">property reason</a>
</h3>

```typescript
reason: string;
```


A machine-readable description of why this operation is in the "Failure" status. If this
value is empty there is no information available. A Reason clarifies an HTTP status code
but does not override it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14318">property status</a>
</h3>

```typescript
status: string;
```


Status of the operation. One of: "Success" or "Failure". More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="StatusCause">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14326">interface StatusCause</a>
</h2>

StatusCause provides more information about an api.Status failure, including cases when
multiple errors are encountered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14337">property field</a>
</h3>

```typescript
field: string;
```


The field of the resource that has caused this error, as named by its JSON serialization.
May include dot and postfix notation for nested attributes. Arrays are zero-indexed.
Fields may appear more than once in an array of causes due to fields having multiple
errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14343">property message</a>
</h3>

```typescript
message: string;
```


A human-readable description of the cause of the error.  This field may be presented as-is
to a reader.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14349">property reason</a>
</h3>

```typescript
reason: string;
```


A machine-readable description of the cause of the error. If this value is empty there is
no information available.

<h2 class="pdoc-module-header" id="StatusDetails">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14359">interface StatusDetails</a>
</h2>

StatusDetails is a set of additional properties that MAY be set by the server to provide
additional information about a response. The Reason field of a Status object defines what
attributes will be set. Clients must ignore fields that do not match the defined type of each
attribute, and should assume that any attribute may be empty, invalid, or under defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14364">property causes</a>
</h3>

```typescript
causes: StatusCause[];
```


The Causes array includes more details associated with the StatusReason failure. Not all
StatusReasons may provide detailed causes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14369">property group</a>
</h3>

```typescript
group: string;
```


The group attribute of the resource associated with the status StatusReason.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14376">property kind</a>
</h3>

```typescript
kind: string;
```


The kind attribute of the resource associated with the status StatusReason. On some
operations may differ from the requested resource Kind. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14382">property name</a>
</h3>

```typescript
name: string;
```


The name attribute of the resource associated with the status StatusReason (when there is a
single name which can be described).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14389">property retryAfterSeconds</a>
</h3>

```typescript
retryAfterSeconds: number;
```


If specified, the time in seconds before the operation should be retried. Some errors may
indicate the client must take an alternate action - for those errors this field may
indicate how long to wait before taking the alternate action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14395">property uid</a>
</h3>

```typescript
uid: string;
```


UID of the resource. (when there is a single resource which can be described). More info:
http://kubernetes.io/docs/user-guide/identifiers#uids

<h2 class="pdoc-module-header" id="WatchEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14402">interface WatchEvent</a>
</h2>

Event represents a single event to a watched resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14410">property object</a>
</h3>

```typescript
object: RawExtension;
```


Object is:
 * If Type is Added or Modified: the new state of the object.
 * If Type is Deleted: the state of the object immediately before deletion.
 * If Type is Error: *Status is recommended; other types may make sense
   depending on context.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14413">property type</a>
</h3>

```typescript
type: string;
```

