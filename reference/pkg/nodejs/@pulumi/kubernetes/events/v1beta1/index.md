---
title: Module events/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">events</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isEvent">function isEvent</a>
* <a href="#isEventList">function isEventList</a>
* <a href="#Event">interface Event</a>
* <a href="#EventList">interface EventList</a>
* <a href="#EventSeries">interface EventSeries</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L14675">function isEvent</a>
</h2>

```typescript
isEvent(o: any): boolean
```

<h2 class="pdoc-module-header" id="isEventList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L14712">function isEventList</a>
</h2>

```typescript
isEventList(o: any): boolean
```

<h2 class="pdoc-module-header" id="Event">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13847">interface Event</a>
</h2>

Event is a report of an event somewhere in the cluster. It generally denotes some state
change in the system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13851">property action</a>
</h3>

```typescript
action: string;
```


What action was taken/failed regarding to the regarding object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13859">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13864">property deprecatedCount</a>
</h3>

```typescript
deprecatedCount: number;
```


Deprecated field assuring backward compatibility with core.v1 Event type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13869">property deprecatedFirstTimestamp</a>
</h3>

```typescript
deprecatedFirstTimestamp: string;
```


Deprecated field assuring backward compatibility with core.v1 Event type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13874">property deprecatedLastTimestamp</a>
</h3>

```typescript
deprecatedLastTimestamp: string;
```


Deprecated field assuring backward compatibility with core.v1 Event type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13879">property deprecatedSource</a>
</h3>

```typescript
deprecatedSource: EventSource;
```


Deprecated field assuring backward compatibility with core.v1 Event type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13884">property eventTime</a>
</h3>

```typescript
eventTime: string;
```


Required. Time when this Event was first observed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13892">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13895">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13901">property note</a>
</h3>

```typescript
note: string;
```


Optional. A human-readable description of the status of this operation. Maximal length of
the note is 1kB, but libraries should be prepared to handle values up to 64kB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13906">property reason</a>
</h3>

```typescript
reason: string;
```


Why the action was taken.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13913">property regarding</a>
</h3>

```typescript
regarding: ObjectReference;
```


The object this Event is about. In most cases it's an Object reporting controller
implements. E.g. ReplicaSetController implements ReplicaSets and this event is emitted
because it acts on some changes in a ReplicaSet object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13919">property related</a>
</h3>

```typescript
related: ObjectReference;
```


Optional secondary object for more complex actions. E.g. when regarding object triggers a
creation or deletion of related object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13924">property reportingController</a>
</h3>

```typescript
reportingController: string;
```


Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13929">property reportingInstance</a>
</h3>

```typescript
reportingInstance: string;
```


ID of the controller instance, e.g. `kubelet-xyzf`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13934">property series</a>
</h3>

```typescript
series: EventSeries;
```


Data about the Event series this event represents or nil if it's a singleton Event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13939">property type</a>
</h3>

```typescript
type: string;
```


Type of this event (Normal, Warning), new types could be added in the future.

<h2 class="pdoc-module-header" id="EventList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13946">interface EventList</a>
</h2>

EventList is a list of Event objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13953">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13958">property items</a>
</h3>

```typescript
items: Event[];
```


Items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13966">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13972">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="EventSeries">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13980">interface EventSeries</a>
</h2>

EventSeries contain information on series of events, i.e. thing that was/is happening
continuously for some time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13984">property count</a>
</h3>

```typescript
count: number;
```


Number of occurrences in this series up to the last heartbeat time

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13989">property lastObservedTime</a>
</h3>

```typescript
lastObservedTime: string;
```


Time when last Event from the series was seen before last heartbeat.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13994">property state</a>
</h3>

```typescript
state: string;
```


Information whether this series is ongoing or finished.

