---
title: Module policy/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">policy</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isEviction">function isEviction</a>
* <a href="#isPodDisruptionBudget">function isPodDisruptionBudget</a>
* <a href="#isPodDisruptionBudgetList">function isPodDisruptionBudgetList</a>
* <a href="#Eviction">interface Eviction</a>
* <a href="#PodDisruptionBudget">interface PodDisruptionBudget</a>
* <a href="#PodDisruptionBudgetList">interface PodDisruptionBudgetList</a>
* <a href="#PodDisruptionBudgetSpec">interface PodDisruptionBudgetSpec</a>
* <a href="#PodDisruptionBudgetStatus">interface PodDisruptionBudgetStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isEviction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15591">function isEviction</a>
</h2>

```typescript
isEviction(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodDisruptionBudget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15631">function isPodDisruptionBudget</a>
</h2>

```typescript
isPodDisruptionBudget(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodDisruptionBudgetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15663">function isPodDisruptionBudgetList</a>
</h2>

```typescript
isPodDisruptionBudgetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="Eviction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14749">interface Eviction</a>
</h2>

Eviction evicts a pod from its node subject to certain policies and safety constraints. This
is a subresource of Pod.  A request to cause such an eviction is created by POSTing to
.../pods/<pod name>/evictions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14756">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14761">property deleteOptions</a>
</h3>

```typescript
deleteOptions: DeleteOptions;
```


DeleteOptions may be provided

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14769">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14774">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


ObjectMeta describes the pod that is being evicted.

<h2 class="pdoc-module-header" id="PodDisruptionBudget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14782">interface PodDisruptionBudget</a>
</h2>

PodDisruptionBudget is an object to define the max disruption that can be caused to a
collection of pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14789">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14797">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14800">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14805">property spec</a>
</h3>

```typescript
spec: PodDisruptionBudgetSpec;
```


Specification of the desired behavior of the PodDisruptionBudget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14810">property status</a>
</h3>

```typescript
status: PodDisruptionBudgetStatus;
```


Most recently observed status of the PodDisruptionBudget.

<h2 class="pdoc-module-header" id="PodDisruptionBudgetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14817">interface PodDisruptionBudgetList</a>
</h2>

PodDisruptionBudgetList is a collection of PodDisruptionBudgets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14824">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14827">property items</a>
</h3>

```typescript
items: PodDisruptionBudget[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14835">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14838">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="PodDisruptionBudgetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14845">interface PodDisruptionBudgetSpec</a>
</h2>

PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14852">property maxUnavailable</a>
</h3>

```typescript
maxUnavailable: number | string;
```


An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are
unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one
can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting
with "minAvailable".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14859">property minAvailable</a>
</h3>

```typescript
minAvailable: number | string;
```


An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be
available after the eviction, i.e. even in the absence of the evicted pod.  So for example
you can prevent all voluntary evictions by specifying "100%".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14864">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Label query over pods whose evictions are managed by the disruption budget.

<h2 class="pdoc-module-header" id="PodDisruptionBudgetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14872">interface PodDisruptionBudgetStatus</a>
</h2>

PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget.
Status may trail the actual state of a system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14876">property currentHealthy</a>
</h3>

```typescript
currentHealthy: number;
```


current number of healthy pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14881">property desiredHealthy</a>
</h3>

```typescript
desiredHealthy: number;
```


minimum desired number of healthy pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14895">property disruptedPods</a>
</h3>

```typescript
disruptedPods: object;
```


DisruptedPods contains information about pods whose eviction was processed by the API
server eviction subresource handler but has not yet been observed by the
PodDisruptionBudget controller. A pod will be in this map from the time when the API server
processed the eviction request to the time when the pod is seen by PDB controller as having
been marked for deletion (or after a timeout). The key in the map is the name of the pod
and the value is the time when the API server processed the eviction request. If the
deletion didn't occur and a pod is still there it will be removed from the list
automatically by PodDisruptionBudget controller after some time. If everything goes smooth
this map should be empty for the most of the time. Large number of entries in the map may
indicate problems with pod deletions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14900">property disruptionsAllowed</a>
</h3>

```typescript
disruptionsAllowed: number;
```


Number of pod disruptions that are currently allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14905">property expectedPods</a>
</h3>

```typescript
expectedPods: number;
```


total number of pods counted by this disruption budget

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14912">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


Most recent generation observed when updating this PDB status. PodDisruptionsAllowed and
other status informatio is valid only if observedGeneration equals to PDB's object
generation.

