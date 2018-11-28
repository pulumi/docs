---
title: Module policy/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">policy</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isEviction">function isEviction</a>
* <a href="#isPodDisruptionBudget">function isPodDisruptionBudget</a>
* <a href="#isPodDisruptionBudgetList">function isPodDisruptionBudgetList</a>
* <a href="#isPodSecurityPolicy">function isPodSecurityPolicy</a>
* <a href="#isPodSecurityPolicyList">function isPodSecurityPolicyList</a>
* <a href="#AllowedFlexVolume">interface AllowedFlexVolume</a>
* <a href="#AllowedHostPath">interface AllowedHostPath</a>
* <a href="#Eviction">interface Eviction</a>
* <a href="#FSGroupStrategyOptions">interface FSGroupStrategyOptions</a>
* <a href="#HostPortRange">interface HostPortRange</a>
* <a href="#IDRange">interface IDRange</a>
* <a href="#PodDisruptionBudget">interface PodDisruptionBudget</a>
* <a href="#PodDisruptionBudgetList">interface PodDisruptionBudgetList</a>
* <a href="#PodDisruptionBudgetSpec">interface PodDisruptionBudgetSpec</a>
* <a href="#PodDisruptionBudgetStatus">interface PodDisruptionBudgetStatus</a>
* <a href="#PodSecurityPolicy">interface PodSecurityPolicy</a>
* <a href="#PodSecurityPolicyList">interface PodSecurityPolicyList</a>
* <a href="#PodSecurityPolicySpec">interface PodSecurityPolicySpec</a>
* <a href="#RunAsUserStrategyOptions">interface RunAsUserStrategyOptions</a>
* <a href="#SELinuxStrategyOptions">interface SELinuxStrategyOptions</a>
* <a href="#SupplementalGroupsStrategyOptions">interface SupplementalGroupsStrategyOptions</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isEviction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17297">function isEviction</a>
</h2>

```typescript
isEviction(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodDisruptionBudget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17390">function isPodDisruptionBudget</a>
</h2>

```typescript
isPodDisruptionBudget(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodDisruptionBudgetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17422">function isPodDisruptionBudgetList</a>
</h2>

```typescript
isPodDisruptionBudgetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodSecurityPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17536">function isPodSecurityPolicy</a>
</h2>

```typescript
isPodSecurityPolicy(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodSecurityPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17573">function isPodSecurityPolicyList</a>
</h2>

```typescript
isPodSecurityPolicyList(o: any): boolean
```

<h2 class="pdoc-module-header" id="AllowedFlexVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16357">interface AllowedFlexVolume</a>
</h2>

AllowedFlexVolume represents a single Flexvolume that is allowed to be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16361">property driver</a>
</h3>

```typescript
driver: string;
```


driver is the name of the Flexvolume driver.

<h2 class="pdoc-module-header" id="AllowedHostPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16369">interface AllowedHostPath</a>
</h2>

AllowedHostPath defines the host volume conditions that will be enabled by a policy for pods
to use. It requires the path prefix to be defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16377">property pathPrefix</a>
</h3>

```typescript
pathPrefix: string;
```


pathPrefix is the path prefix that the host volume must match. It does not support `*`.
Trailing slashes are trimmed when validating the path prefix with a host path.

Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food`
or `/etc/foo`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16383">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


when set to true, will allow host volumes matching the pathPrefix only if all volume mounts
are readOnly.

<h2 class="pdoc-module-header" id="Eviction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16392">interface Eviction</a>
</h2>

Eviction evicts a pod from its node subject to certain policies and safety constraints. This
is a subresource of Pod.  A request to cause such an eviction is created by POSTing to
.../pods/<pod name>/evictions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16399">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16404">property deleteOptions</a>
</h3>

```typescript
deleteOptions: DeleteOptions;
```


DeleteOptions may be provided

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16412">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16417">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


ObjectMeta describes the pod that is being evicted.

<h2 class="pdoc-module-header" id="FSGroupStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16424">interface FSGroupStrategyOptions</a>
</h2>

FSGroupStrategyOptions defines the strategy type and options used to create the strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16429">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of fs groups.  If you would like to force a single fs group
then supply a single range with the same start and end. Required for MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16434">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

<h2 class="pdoc-module-header" id="HostPortRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16442">interface HostPortRange</a>
</h2>

HostPortRange defines a range of host ports that will be enabled by a policy for pods to use.
It requires both the start and end to be defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16446">property max</a>
</h3>

```typescript
max: number;
```


max is the end of the range, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16451">property min</a>
</h3>

```typescript
min: number;
```


min is the start of the range, inclusive.

<h2 class="pdoc-module-header" id="IDRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16458">interface IDRange</a>
</h2>

IDRange provides a min/max of an allowed range of IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16462">property max</a>
</h3>

```typescript
max: number;
```


max is the end of the range, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16467">property min</a>
</h3>

```typescript
min: number;
```


min is the start of the range, inclusive.

<h2 class="pdoc-module-header" id="PodDisruptionBudget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16475">interface PodDisruptionBudget</a>
</h2>

PodDisruptionBudget is an object to define the max disruption that can be caused to a
collection of pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16482">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16490">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16493">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16498">property spec</a>
</h3>

```typescript
spec: PodDisruptionBudgetSpec;
```


Specification of the desired behavior of the PodDisruptionBudget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16503">property status</a>
</h3>

```typescript
status: PodDisruptionBudgetStatus;
```


Most recently observed status of the PodDisruptionBudget.

<h2 class="pdoc-module-header" id="PodDisruptionBudgetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16510">interface PodDisruptionBudgetList</a>
</h2>

PodDisruptionBudgetList is a collection of PodDisruptionBudgets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16517">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16520">property items</a>
</h3>

```typescript
items: PodDisruptionBudget[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16528">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16531">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="PodDisruptionBudgetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16538">interface PodDisruptionBudgetSpec</a>
</h2>

PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16545">property maxUnavailable</a>
</h3>

```typescript
maxUnavailable: number | string;
```


An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are
unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one
can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting
with "minAvailable".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16552">property minAvailable</a>
</h3>

```typescript
minAvailable: number | string;
```


An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be
available after the eviction, i.e. even in the absence of the evicted pod.  So for example
you can prevent all voluntary evictions by specifying "100%".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16557">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Label query over pods whose evictions are managed by the disruption budget.

<h2 class="pdoc-module-header" id="PodDisruptionBudgetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16565">interface PodDisruptionBudgetStatus</a>
</h2>

PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget.
Status may trail the actual state of a system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16569">property currentHealthy</a>
</h3>

```typescript
currentHealthy: number;
```


current number of healthy pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16574">property desiredHealthy</a>
</h3>

```typescript
desiredHealthy: number;
```


minimum desired number of healthy pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16588">property disruptedPods</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16593">property disruptionsAllowed</a>
</h3>

```typescript
disruptionsAllowed: number;
```


Number of pod disruptions that are currently allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16598">property expectedPods</a>
</h3>

```typescript
expectedPods: number;
```


total number of pods counted by this disruption budget

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16605">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


Most recent generation observed when updating this PDB status. PodDisruptionsAllowed and
other status informatio is valid only if observedGeneration equals to PDB's object
generation.

<h2 class="pdoc-module-header" id="PodSecurityPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16613">interface PodSecurityPolicy</a>
</h2>

PodSecurityPolicy governs the ability to make requests that affect the Security Context that
will be applied to a pod and container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16620">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16628">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16634">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16639">property spec</a>
</h3>

```typescript
spec: PodSecurityPolicySpec;
```


spec defines the policy enforced.

<h2 class="pdoc-module-header" id="PodSecurityPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16646">interface PodSecurityPolicyList</a>
</h2>

PodSecurityPolicyList is a list of PodSecurityPolicy objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16653">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16658">property items</a>
</h3>

```typescript
items: PodSecurityPolicy[];
```


items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16666">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16672">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="PodSecurityPolicySpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16679">interface PodSecurityPolicySpec</a>
</h2>

PodSecurityPolicySpec defines the policy enforced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16684">property allowPrivilegeEscalation</a>
</h3>

```typescript
allowPrivilegeEscalation: boolean;
```


allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If
unspecified, defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16691">property allowedCapabilities</a>
</h3>

```typescript
allowedCapabilities: string[];
```


allowedCapabilities is a list of capabilities that can be requested to add to the
container. Capabilities in this field may be added at the pod author's discretion. You must
not list a capability in both allowedCapabilities and requiredDropCapabilities.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16698">property allowedFlexVolumes</a>
</h3>

```typescript
allowedFlexVolumes: AllowedFlexVolume[];
```


allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all
Flexvolumes may be used.  This parameter is effective only when the usage of the
Flexvolumes is allowed in the "volumes" field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16704">property allowedHostPaths</a>
</h3>

```typescript
allowedHostPaths: AllowedHostPath[];
```


allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths
may be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16711">property allowedProcMountTypes</a>
</h3>

```typescript
allowedProcMountTypes: string[];
```


AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that
only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to
be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16722">property allowedUnsafeSysctls</a>
</h3>

```typescript
allowedUnsafeSysctls: string[];
```


allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each
entry is either a plain sysctl name or ends in "*" in which case it is considered as a
prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to
whitelist all allowed unsafe sysctls explicitly to avoid rejection.

Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar",
"foo.baz", etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16730">property defaultAddCapabilities</a>
</h3>

```typescript
defaultAddCapabilities: string[];
```


defaultAddCapabilities is the default set of capabilities that will be added to the
container unless the pod spec specifically drops the capability.  You may not list a
capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added
here are implicitly allowed, and need not be included in the allowedCapabilities list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16736">property defaultAllowPrivilegeEscalation</a>
</h3>

```typescript
defaultAllowPrivilegeEscalation: boolean;
```


defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain
more privileges than its parent process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16746">property forbiddenSysctls</a>
</h3>

```typescript
forbiddenSysctls: string[];
```


forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is
either a plain sysctl name or ends in "*" in which case it is considered as a prefix of
forbidden sysctls. Single * means all sysctls are forbidden.

Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar",
"foo.baz", etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16751">property fsGroup</a>
</h3>

```typescript
fsGroup: FSGroupStrategyOptions;
```


fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16756">property hostIPC</a>
</h3>

```typescript
hostIPC: boolean;
```


hostIPC determines if the policy allows the use of HostIPC in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16761">property hostNetwork</a>
</h3>

```typescript
hostNetwork: boolean;
```


hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16766">property hostPID</a>
</h3>

```typescript
hostPID: boolean;
```


hostPID determines if the policy allows the use of HostPID in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16771">property hostPorts</a>
</h3>

```typescript
hostPorts: HostPortRange[];
```


hostPorts determines which host port ranges are allowed to be exposed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16776">property privileged</a>
</h3>

```typescript
privileged: boolean;
```


privileged determines if a pod can request to be run as privileged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16784">property readOnlyRootFilesystem</a>
</h3>

```typescript
readOnlyRootFilesystem: boolean;
```


readOnlyRootFilesystem when set to true will force containers to run with a read only root
file system.  If the container specifically requests to run with a non-read only root file
system the PSP should deny the pod. If set to false the container may run with a read only
root file system if it wishes but it will not be forced to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16790">property requiredDropCapabilities</a>
</h3>

```typescript
requiredDropCapabilities: string[];
```


requiredDropCapabilities are the capabilities that will be dropped from the container.
These are required to be dropped and cannot be added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16795">property runAsUser</a>
</h3>

```typescript
runAsUser: RunAsUserStrategyOptions;
```


runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16800">property seLinux</a>
</h3>

```typescript
seLinux: SELinuxStrategyOptions;
```


seLinux is the strategy that will dictate the allowable labels that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16806">property supplementalGroups</a>
</h3>

```typescript
supplementalGroups: SupplementalGroupsStrategyOptions;
```


supplementalGroups is the strategy that will dictate what supplemental groups are used by
the SecurityContext.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16812">property volumes</a>
</h3>

```typescript
volumes: string[];
```


volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be
used. To allow all volumes you may use '*'.

<h2 class="pdoc-module-header" id="RunAsUserStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16820">interface RunAsUserStrategyOptions</a>
</h2>

RunAsUserStrategyOptions defines the strategy type and any options used to create the
strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16825">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of uids that may be used. If you would like to force a single
uid then supply a single range with the same start and end. Required for MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16830">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate the allowable RunAsUser values that may be set.

<h2 class="pdoc-module-header" id="SELinuxStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16837">interface SELinuxStrategyOptions</a>
</h2>

SELinuxStrategyOptions defines the strategy type and any options used to create the strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16841">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate the allowable labels that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16847">property seLinuxOptions</a>
</h3>

```typescript
seLinuxOptions: SELinuxOptions;
```


seLinuxOptions required to run as; required for MustRunAs More info:
https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

<h2 class="pdoc-module-header" id="SupplementalGroupsStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16855">interface SupplementalGroupsStrategyOptions</a>
</h2>

SupplementalGroupsStrategyOptions defines the strategy type and options used to create the
strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16861">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of supplemental groups.  If you would like to force a single
supplemental group then supply a single range with the same start and end. Required for
MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16867">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate what supplemental groups is used in the
SecurityContext.

