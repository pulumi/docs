---
title: Module autoscaling/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">autoscaling</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCrossVersionObjectReference">function isCrossVersionObjectReference</a>
* <a href="#isHorizontalPodAutoscaler">function isHorizontalPodAutoscaler</a>
* <a href="#isHorizontalPodAutoscalerList">function isHorizontalPodAutoscalerList</a>
* <a href="#isScale">function isScale</a>
* <a href="#CrossVersionObjectReference">interface CrossVersionObjectReference</a>
* <a href="#HorizontalPodAutoscaler">interface HorizontalPodAutoscaler</a>
* <a href="#HorizontalPodAutoscalerList">interface HorizontalPodAutoscalerList</a>
* <a href="#HorizontalPodAutoscalerSpec">interface HorizontalPodAutoscalerSpec</a>
* <a href="#HorizontalPodAutoscalerStatus">interface HorizontalPodAutoscalerStatus</a>
* <a href="#Scale">interface Scale</a>
* <a href="#ScaleSpec">interface ScaleSpec</a>
* <a href="#ScaleStatus">interface ScaleStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5905">function isCrossVersionObjectReference</a>
</h2>

```typescript
isCrossVersionObjectReference(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5948">function isHorizontalPodAutoscaler</a>
</h2>

```typescript
isHorizontalPodAutoscaler(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5984">function isHorizontalPodAutoscalerList</a>
</h2>

```typescript
isHorizontalPodAutoscalerList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6093">function isScale</a>
</h2>

```typescript
isScale(o: any): boolean
```

<h2 class="pdoc-module-header" id="CrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5563">interface CrossVersionObjectReference</a>
</h2>

CrossVersionObjectReference contains enough information to let you identify the referred
resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5567">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5573">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5578">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names

<h2 class="pdoc-module-header" id="HorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5585">interface HorizontalPodAutoscaler</a>
</h2>

configuration of a horizontal pod autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5592">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5600">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5606">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5612">property spec</a>
</h3>

```typescript
spec: HorizontalPodAutoscalerSpec;
```


behaviour of autoscaler. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5617">property status</a>
</h3>

```typescript
status: HorizontalPodAutoscalerStatus;
```


current information about the autoscaler.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5624">interface HorizontalPodAutoscalerList</a>
</h2>

list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5631">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5636">property items</a>
</h3>

```typescript
items: HorizontalPodAutoscaler[];
```


list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5644">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5649">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5656">interface HorizontalPodAutoscalerSpec</a>
</h2>

specification of a horizontal pod autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5661">property maxReplicas</a>
</h3>

```typescript
maxReplicas: number;
```


upper limit for the number of pods that can be set by the autoscaler; cannot be smaller
than MinReplicas.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5666">property minReplicas</a>
</h3>

```typescript
minReplicas: number;
```


lower limit for the number of pods that can be set by the autoscaler, default 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5672">property scaleTargetRef</a>
</h3>

```typescript
scaleTargetRef: CrossVersionObjectReference;
```


reference to scaled resource; horizontal pod autoscaler will learn the current resource
consumption and will set the desired number of pods by using its Scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5678">property targetCPUUtilizationPercentage</a>
</h3>

```typescript
targetCPUUtilizationPercentage: number;
```


target average CPU utilization (represented as a percentage of requested CPU) over all the
pods; if not specified the default autoscaling policy will be used.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5685">interface HorizontalPodAutoscalerStatus</a>
</h2>

current status of a horizontal pod autoscaler

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5690">property currentCPUUtilizationPercentage</a>
</h3>

```typescript
currentCPUUtilizationPercentage: number;
```


current average CPU utilization over all pods, represented as a percentage of requested
CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5695">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


current number of replicas of pods managed by this autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5700">property desiredReplicas</a>
</h3>

```typescript
desiredReplicas: number;
```


desired number of replicas of pods managed by this autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5706">property lastScaleTime</a>
</h3>

```typescript
lastScaleTime: string;
```


last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to
control how often the number of pods is changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5711">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


most recent generation observed by this autoscaler.

<h2 class="pdoc-module-header" id="Scale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5718">interface Scale</a>
</h2>

Scale represents a scaling request for a resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5725">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5733">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5739">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5745">property spec</a>
</h3>

```typescript
spec: ScaleSpec;
```


defines the behavior of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5752">property status</a>
</h3>

```typescript
status: ScaleStatus;
```


current status of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
Read-only.

<h2 class="pdoc-module-header" id="ScaleSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5759">interface ScaleSpec</a>
</h2>

ScaleSpec describes the attributes of a scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5763">property replicas</a>
</h3>

```typescript
replicas: number;
```


desired number of instances for the scaled object.

<h2 class="pdoc-module-header" id="ScaleStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5770">interface ScaleStatus</a>
</h2>

ScaleStatus represents the current status of a scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5774">property replicas</a>
</h3>

```typescript
replicas: number;
```


actual number of observed instances of the scaled object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5782">property selector</a>
</h3>

```typescript
selector: string;
```


label query over pods that should match the replicas count. This is same as the label
selector but in the string format to avoid introspection by clients. The string will be in
the same format as the query-param syntax. More info about label selectors:
http://kubernetes.io/docs/user-guide/labels#label-selectors

