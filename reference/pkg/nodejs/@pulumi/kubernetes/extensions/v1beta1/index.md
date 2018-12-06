---
title: Module extensions/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">extensions</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isDaemonSet">function isDaemonSet</a>
* <a href="#isDaemonSetList">function isDaemonSetList</a>
* <a href="#isDeployment">function isDeployment</a>
* <a href="#isDeploymentList">function isDeploymentList</a>
* <a href="#isDeploymentRollback">function isDeploymentRollback</a>
* <a href="#isIngress">function isIngress</a>
* <a href="#isIngressList">function isIngressList</a>
* <a href="#isNetworkPolicy">function isNetworkPolicy</a>
* <a href="#isNetworkPolicyList">function isNetworkPolicyList</a>
* <a href="#isPodSecurityPolicy">function isPodSecurityPolicy</a>
* <a href="#isPodSecurityPolicyList">function isPodSecurityPolicyList</a>
* <a href="#isReplicaSet">function isReplicaSet</a>
* <a href="#isReplicaSetList">function isReplicaSetList</a>
* <a href="#isScale">function isScale</a>
* <a href="#AllowedFlexVolume">interface AllowedFlexVolume</a>
* <a href="#AllowedHostPath">interface AllowedHostPath</a>
* <a href="#DaemonSet">interface DaemonSet</a>
* <a href="#DaemonSetCondition">interface DaemonSetCondition</a>
* <a href="#DaemonSetList">interface DaemonSetList</a>
* <a href="#DaemonSetSpec">interface DaemonSetSpec</a>
* <a href="#DaemonSetStatus">interface DaemonSetStatus</a>
* <a href="#DaemonSetUpdateStrategy">interface DaemonSetUpdateStrategy</a>
* <a href="#Deployment">interface Deployment</a>
* <a href="#DeploymentCondition">interface DeploymentCondition</a>
* <a href="#DeploymentList">interface DeploymentList</a>
* <a href="#DeploymentRollback">interface DeploymentRollback</a>
* <a href="#DeploymentSpec">interface DeploymentSpec</a>
* <a href="#DeploymentStatus">interface DeploymentStatus</a>
* <a href="#DeploymentStrategy">interface DeploymentStrategy</a>
* <a href="#FSGroupStrategyOptions">interface FSGroupStrategyOptions</a>
* <a href="#HTTPIngressPath">interface HTTPIngressPath</a>
* <a href="#HTTPIngressRuleValue">interface HTTPIngressRuleValue</a>
* <a href="#HostPortRange">interface HostPortRange</a>
* <a href="#IDRange">interface IDRange</a>
* <a href="#IPBlock">interface IPBlock</a>
* <a href="#Ingress">interface Ingress</a>
* <a href="#IngressBackend">interface IngressBackend</a>
* <a href="#IngressList">interface IngressList</a>
* <a href="#IngressRule">interface IngressRule</a>
* <a href="#IngressSpec">interface IngressSpec</a>
* <a href="#IngressStatus">interface IngressStatus</a>
* <a href="#IngressTLS">interface IngressTLS</a>
* <a href="#NetworkPolicy">interface NetworkPolicy</a>
* <a href="#NetworkPolicyEgressRule">interface NetworkPolicyEgressRule</a>
* <a href="#NetworkPolicyIngressRule">interface NetworkPolicyIngressRule</a>
* <a href="#NetworkPolicyList">interface NetworkPolicyList</a>
* <a href="#NetworkPolicyPeer">interface NetworkPolicyPeer</a>
* <a href="#NetworkPolicyPort">interface NetworkPolicyPort</a>
* <a href="#NetworkPolicySpec">interface NetworkPolicySpec</a>
* <a href="#PodSecurityPolicy">interface PodSecurityPolicy</a>
* <a href="#PodSecurityPolicyList">interface PodSecurityPolicyList</a>
* <a href="#PodSecurityPolicySpec">interface PodSecurityPolicySpec</a>
* <a href="#ReplicaSet">interface ReplicaSet</a>
* <a href="#ReplicaSetCondition">interface ReplicaSetCondition</a>
* <a href="#ReplicaSetList">interface ReplicaSetList</a>
* <a href="#ReplicaSetSpec">interface ReplicaSetSpec</a>
* <a href="#ReplicaSetStatus">interface ReplicaSetStatus</a>
* <a href="#RollbackConfig">interface RollbackConfig</a>
* <a href="#RollingUpdateDaemonSet">interface RollingUpdateDaemonSet</a>
* <a href="#RollingUpdateDeployment">interface RollingUpdateDeployment</a>
* <a href="#RunAsGroupStrategyOptions">interface RunAsGroupStrategyOptions</a>
* <a href="#RunAsUserStrategyOptions">interface RunAsUserStrategyOptions</a>
* <a href="#SELinuxStrategyOptions">interface SELinuxStrategyOptions</a>
* <a href="#Scale">interface Scale</a>
* <a href="#ScaleSpec">interface ScaleSpec</a>
* <a href="#ScaleStatus">interface ScaleStatus</a>
* <a href="#SupplementalGroupsStrategyOptions">interface SupplementalGroupsStrategyOptions</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isDaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L14824">function isDaemonSet</a>
</h2>

```typescript
isDaemonSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDaemonSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L14893">function isDaemonSetList</a>
</h2>

```typescript
isDaemonSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15063">function isDeployment</a>
</h2>

```typescript
isDeployment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15136">function isDeploymentList</a>
</h2>

```typescript
isDeploymentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeploymentRollback">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15177">function isDeploymentRollback</a>
</h2>

```typescript
isDeploymentRollback(o: any): boolean
```

<h2 class="pdoc-module-header" id="isIngress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15472">function isIngress</a>
</h2>

```typescript
isIngress(o: any): boolean
```

<h2 class="pdoc-module-header" id="isIngressList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15526">function isIngressList</a>
</h2>

```typescript
isIngressList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNetworkPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15653">function isNetworkPolicy</a>
</h2>

```typescript
isNetworkPolicy(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNetworkPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15745">function isNetworkPolicyList</a>
</h2>

```typescript
isNetworkPolicyList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodSecurityPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15889">function isPodSecurityPolicy</a>
</h2>

```typescript
isPodSecurityPolicy(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodSecurityPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15927">function isPodSecurityPolicyList</a>
</h2>

```typescript
isPodSecurityPolicyList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicaSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L16124">function isReplicaSet</a>
</h2>

```typescript
isReplicaSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicaSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L16194">function isReplicaSetList</a>
</h2>

```typescript
isReplicaSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L16435">function isScale</a>
</h2>

```typescript
isScale(o: any): boolean
```

<h2 class="pdoc-module-header" id="AllowedFlexVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14008">interface AllowedFlexVolume</a>
</h2>

AllowedFlexVolume represents a single Flexvolume that is allowed to be used. Deprecated: use
AllowedFlexVolume from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14012">property driver</a>
</h3>

```typescript
driver: string;
```


driver is the name of the Flexvolume driver.

<h2 class="pdoc-module-header" id="AllowedHostPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14021">interface AllowedHostPath</a>
</h2>

AllowedHostPath defines the host volume conditions that will be enabled by a policy for pods
to use. It requires the path prefix to be defined. Deprecated: use AllowedHostPath from
policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14029">property pathPrefix</a>
</h3>

```typescript
pathPrefix: string;
```


pathPrefix is the path prefix that the host volume must match. It does not support `*`.
Trailing slashes are trimmed when validating the path prefix with a host path.

Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food`
or `/etc/foo`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14035">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


when set to true, will allow host volumes matching the pathPrefix only if all volume mounts
are readOnly.

<h2 class="pdoc-module-header" id="DaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14043">interface DaemonSet</a>
</h2>

DEPRECATED - This group version of DaemonSet is deprecated by apps/v1beta2/DaemonSet. See the
release notes for more information. DaemonSet represents the configuration of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14050">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14058">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14064">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14070">property spec</a>
</h3>

```typescript
spec: DaemonSetSpec;
```


The desired behavior of this daemon set. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14077">property status</a>
</h3>

```typescript
status: DaemonSetStatus;
```


The current status of this daemon set. This data may be out of date by some window of time.
Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="DaemonSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14084">interface DaemonSetCondition</a>
</h2>

DaemonSetCondition describes the state of a DaemonSet at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14088">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14093">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14098">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14103">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14108">property type</a>
</h3>

```typescript
type: string;
```


Type of DaemonSet condition.

<h2 class="pdoc-module-header" id="DaemonSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14115">interface DaemonSetList</a>
</h2>

DaemonSetList is a collection of daemon sets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14122">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14127">property items</a>
</h3>

```typescript
items: DaemonSet[];
```


A list of daemon sets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14135">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14141">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="DaemonSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14148">interface DaemonSetSpec</a>
</h2>

DaemonSetSpec is the specification of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14154">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


The minimum number of seconds for which a newly created DaemonSet pod should be ready
without any of its container crashing, for it to be considered available. Defaults to 0
(pod will be considered available as soon as it is ready).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14160">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


The number of old history to retain to allow rollback. This is a pointer to distinguish
between explicit zero and not specified. Defaults to 10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14167">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


A label query over pods that are managed by the daemon set. Must match in order to be
controlled. If empty, defaulted to labels on Pod template. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14175">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


An object that describes the pod that will be created. The DaemonSet will create exactly
one copy of this pod on every node that matches the template's node selector (or on every
node if no node selector is specified). More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14181">property templateGeneration</a>
</h3>

```typescript
templateGeneration: number;
```


DEPRECATED. A sequence number representing a specific generation of the template. Populated
by the system. It can be set only during the creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14186">property updateStrategy</a>
</h3>

```typescript
updateStrategy: DaemonSetUpdateStrategy;
```


An update strategy to replace existing DaemonSet pods with new pods.

<h2 class="pdoc-module-header" id="DaemonSetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14193">interface DaemonSetStatus</a>
</h2>

DaemonSetStatus represents the current status of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14199">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a
collision avoidance mechanism when it needs to create the name for the newest
ControllerRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14204">property conditions</a>
</h3>

```typescript
conditions: DaemonSetCondition[];
```


Represents the latest available observations of a DaemonSet's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14210">property currentNumberScheduled</a>
</h3>

```typescript
currentNumberScheduled: number;
```


The number of nodes that are running at least 1 daemon pod and are supposed to run the
daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14217">property desiredNumberScheduled</a>
</h3>

```typescript
desiredNumberScheduled: number;
```


The total number of nodes that should be running the daemon pod (including nodes correctly
running the daemon pod). More info:
https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14223">property numberAvailable</a>
</h3>

```typescript
numberAvailable: number;
```


The number of nodes that should be running the daemon pod and have one or more of the
daemon pod running and available (ready for at least spec.minReadySeconds)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14229">property numberMisscheduled</a>
</h3>

```typescript
numberMisscheduled: number;
```


The number of nodes that are running the daemon pod, but are not supposed to run the daemon
pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14235">property numberReady</a>
</h3>

```typescript
numberReady: number;
```


The number of nodes that should be running the daemon pod and have one or more of the
daemon pod running and ready.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14241">property numberUnavailable</a>
</h3>

```typescript
numberUnavailable: number;
```


The number of nodes that should be running the daemon pod and have none of the daemon pod
running and available (ready for at least spec.minReadySeconds)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14246">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


The most recent generation observed by the daemon set controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14251">property updatedNumberScheduled</a>
</h3>

```typescript
updatedNumberScheduled: number;
```


The total number of nodes that are running updated daemon pod

<h2 class="pdoc-module-header" id="DaemonSetUpdateStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14256">interface DaemonSetUpdateStrategy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14260">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateDaemonSet;
```


Rolling update config params. Present only if type = "RollingUpdate".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14265">property type</a>
</h3>

```typescript
type: string;
```


Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is OnDelete.

<h2 class="pdoc-module-header" id="Deployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14274">interface Deployment</a>
</h2>

DEPRECATED - This group version of Deployment is deprecated by apps/v1beta2/Deployment. See
the release notes for more information. Deployment enables declarative updates for Pods and
ReplicaSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14281">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14289">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14294">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14299">property spec</a>
</h3>

```typescript
spec: DeploymentSpec;
```


Specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14304">property status</a>
</h3>

```typescript
status: DeploymentStatus;
```


Most recently observed status of the Deployment.

<h2 class="pdoc-module-header" id="DeploymentCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14311">interface DeploymentCondition</a>
</h2>

DeploymentCondition describes the state of a deployment at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14315">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14320">property lastUpdateTime</a>
</h3>

```typescript
lastUpdateTime: string;
```


The last time this condition was updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14325">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14330">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14335">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14340">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment condition.

<h2 class="pdoc-module-header" id="DeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14347">interface DeploymentList</a>
</h2>

DeploymentList is a list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14354">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14359">property items</a>
</h3>

```typescript
items: Deployment[];
```


Items is the list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14367">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14372">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata.

<h2 class="pdoc-module-header" id="DeploymentRollback">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14379">interface DeploymentRollback</a>
</h2>

DEPRECATED. DeploymentRollback stores the information required to rollback a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14386">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14394">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14399">property name</a>
</h3>

```typescript
name: string;
```


Required: This must match the Name of a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14404">property rollbackTo</a>
</h3>

```typescript
rollbackTo: RollbackConfig;
```


The config of this deployment rollback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14409">property updatedAnnotations</a>
</h3>

```typescript
updatedAnnotations: { ... };
```


The annotations to be updated to a deployment

<h2 class="pdoc-module-header" id="DeploymentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14416">interface DeploymentSpec</a>
</h2>

DeploymentSpec is the specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14422">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14428">property paused</a>
</h3>

```typescript
paused: boolean;
```


Indicates that the deployment is paused and will not be processed by the deployment
controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14437">property progressDeadlineSeconds</a>
</h3>

```typescript
progressDeadlineSeconds: number;
```


The maximum time in seconds for a deployment to make progress before it is considered to be
failed. The deployment controller will continue to process failed deployments and a
condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status.
Note that progress will not be estimated during the time a deployment is paused. This is
set to the max value of int32 (i.e. 2147483647) by default, which means "no deadline".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14443">property replicas</a>
</h3>

```typescript
replicas: number;
```


Number of desired pods. This is a pointer to distinguish between explicit zero and not
specified. Defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14450">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish
between explicit zero and not specified. This is set to the max value of int32 (i.e.
2147483647) by default, which means "retaining all old RelicaSets".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14456">property rollbackTo</a>
</h3>

```typescript
rollbackTo: RollbackConfig;
```


DEPRECATED. The config this deployment is rolling back to. Will be cleared after rollback
is done.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14462">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the
ones affected by this deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14467">property strategy</a>
</h3>

```typescript
strategy: DeploymentStrategy;
```


The deployment strategy to use to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14472">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template describes the pods that will be created.

<h2 class="pdoc-module-header" id="DeploymentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14479">interface DeploymentStatus</a>
</h2>

DeploymentStatus is the most recently observed status of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14484">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


Total number of available pods (ready for at least minReadySeconds) targeted by this
deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14490">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


Count of hash collisions for the Deployment. The Deployment controller uses this field as a
collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14495">property conditions</a>
</h3>

```typescript
conditions: DeploymentCondition[];
```


Represents the latest available observations of a deployment's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14500">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


The generation observed by the deployment controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14505">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


Total number of ready pods targeted by this deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14511">property replicas</a>
</h3>

```typescript
replicas: number;
```


Total number of non-terminated pods targeted by this deployment (their labels match the
selector).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14519">property unavailableReplicas</a>
</h3>

```typescript
unavailableReplicas: number;
```


Total number of unavailable pods targeted by this deployment. This is the total number of
pods that are still required for the deployment to have 100% available capacity. They may
either be pods that are running but not yet available or pods that still have not been
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14525">property updatedReplicas</a>
</h3>

```typescript
updatedReplicas: number;
```


Total number of non-terminated pods targeted by this deployment that have the desired
template spec.

<h2 class="pdoc-module-header" id="DeploymentStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14532">interface DeploymentStrategy</a>
</h2>

DeploymentStrategy describes how to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14536">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateDeployment;
```


Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14541">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.

<h2 class="pdoc-module-header" id="FSGroupStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14549">interface FSGroupStrategyOptions</a>
</h2>

FSGroupStrategyOptions defines the strategy type and options used to create the strategy.
Deprecated: use FSGroupStrategyOptions from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14554">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of fs groups.  If you would like to force a single fs group
then supply a single range with the same start and end. Required for MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14559">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

<h2 class="pdoc-module-header" id="HTTPIngressPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14567">interface HTTPIngressPath</a>
</h2>

HTTPIngressPath associates a path regex with a backend. Incoming urls matching the path are
forwarded to the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14571">property backend</a>
</h3>

```typescript
backend: IngressBackend;
```


Backend defines the referenced service endpoint to which the traffic will be forwarded to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14580">property path</a>
</h3>

```typescript
path: string;
```


Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the
egrep/unix syntax, not the perl syntax) matched against the path of an incoming request.
Currently it can contain characters disallowed from the conventional "path" part of a URL
as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a
catch all sending traffic to the backend.

<h2 class="pdoc-module-header" id="HTTPIngressRuleValue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14590">interface HTTPIngressRuleValue</a>
</h2>

HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example:
http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC
3986, this resource will be used to match against everything after the last '/' and before
the first '?' or '#'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14594">property paths</a>
</h3>

```typescript
paths: HTTPIngressPath[];
```


A collection of paths that map requests to backends.

<h2 class="pdoc-module-header" id="HostPortRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14603">interface HostPortRange</a>
</h2>

HostPortRange defines a range of host ports that will be enabled by a policy for pods to use.
It requires both the start and end to be defined. Deprecated: use HostPortRange from policy
API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14607">property max</a>
</h3>

```typescript
max: number;
```


max is the end of the range, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14612">property min</a>
</h3>

```typescript
min: number;
```


min is the start of the range, inclusive.

<h2 class="pdoc-module-header" id="IDRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14620">interface IDRange</a>
</h2>

IDRange provides a min/max of an allowed range of IDs. Deprecated: use IDRange from policy
API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14624">property max</a>
</h3>

```typescript
max: number;
```


max is the end of the range, inclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14629">property min</a>
</h3>

```typescript
min: number;
```


min is the start of the range, inclusive.

<h2 class="pdoc-module-header" id="IPBlock">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14639">interface IPBlock</a>
</h2>

DEPRECATED 1.9 - This group version of IPBlock is deprecated by networking/v1/IPBlock.
IPBlock describes a particular CIDR (Ex. "192.168.1.1/24") that is allowed to the pods
matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should
not be included within this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14643">property cidr</a>
</h3>

```typescript
cidr: string;
```


CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14649">property except</a>
</h3>

```typescript
except: string[];
```


Except is a slice of CIDRs that should not be included within an IP Block Valid examples
are "192.168.1.1/24" Except values will be rejected if they are outside the CIDR range

<h2 class="pdoc-module-header" id="Ingress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14658">interface Ingress</a>
</h2>

Ingress is a collection of rules that allow inbound connections to reach the endpoints
defined by a backend. An Ingress can be configured to give services externally-reachable
urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14665">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14673">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14679">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14685">property spec</a>
</h3>

```typescript
spec: IngressSpec;
```


Spec is the desired state of the Ingress. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14691">property status</a>
</h3>

```typescript
status: IngressStatus;
```


Status is the current state of the Ingress. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="IngressBackend">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14698">interface IngressBackend</a>
</h2>

IngressBackend describes all endpoints for a given service and port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14702">property serviceName</a>
</h3>

```typescript
serviceName: string;
```


Specifies the name of the referenced service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14707">property servicePort</a>
</h3>

```typescript
servicePort: number | string;
```


Specifies the port of the referenced service.

<h2 class="pdoc-module-header" id="IngressList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14714">interface IngressList</a>
</h2>

IngressList is a collection of Ingress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14721">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14726">property items</a>
</h3>

```typescript
items: Ingress[];
```


Items is the list of Ingress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14734">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14740">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="IngressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14749">interface IngressRule</a>
</h2>

IngressRule represents the rules mapping the paths under a specified host to the related
backend services. Incoming requests are first evaluated for a host match, then routed to the
backend associated with the matching IngressRuleValue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14762">property host</a>
</h3>

```typescript
host: string;
```


Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the
following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not
allowed. Currently an IngressRuleValue can only apply to the
	  IP in the Spec of the parent Ingress.
2. The `:` delimiter is not respected because ports are not allowed.
	  Currently the port of an Ingress is implicitly :80 for http and
	  :443 for https.
Both these may change in the future. Incoming requests are matched against the host before
the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on
the specified IngressRuleValue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14765">property http</a>
</h3>

```typescript
http: HTTPIngressRuleValue;
```

<h2 class="pdoc-module-header" id="IngressSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14772">interface IngressSpec</a>
</h2>

IngressSpec describes the Ingress the user wishes to exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14778">property backend</a>
</h3>

```typescript
backend: IngressBackend;
```


A default backend capable of servicing requests that don't match any rule. At least one of
'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer
controller or defaulting logic to specify a global default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14784">property rules</a>
</h3>

```typescript
rules: IngressRule[];
```


A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all
traffic is sent to the default backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14792">property tls</a>
</h3>

```typescript
tls: IngressTLS[];
```


TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple
members of this list specify different hosts, they will be multiplexed on the same port
according to the hostname specified through the SNI TLS extension, if the ingress
controller fulfilling the ingress supports SNI.

<h2 class="pdoc-module-header" id="IngressStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14799">interface IngressStatus</a>
</h2>

IngressStatus describe the current state of the Ingress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14803">property loadBalancer</a>
</h3>

```typescript
loadBalancer: LoadBalancerStatus;
```


LoadBalancer contains the current status of the load-balancer.

<h2 class="pdoc-module-header" id="IngressTLS">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14810">interface IngressTLS</a>
</h2>

IngressTLS describes the transport layer security associated with an Ingress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14816">property hosts</a>
</h3>

```typescript
hosts: string[];
```


Hosts are a list of hosts included in the TLS certificate. The values in this list must
match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the
loadbalancer controller fulfilling this Ingress, if left unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14824">property secretName</a>
</h3>

```typescript
secretName: string;
```


SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left
optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener
conflicts with the "Host" header field used by an IngressRule, the SNI host is used for
termination and value of the Host header is used for routing.

<h2 class="pdoc-module-header" id="NetworkPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14833">interface NetworkPolicy</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicy is deprecated by
networking/v1/NetworkPolicy. NetworkPolicy describes what network traffic is allowed for a
set of Pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14840">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14848">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14854">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14859">property spec</a>
</h3>

```typescript
spec: NetworkPolicySpec;
```


Specification of the desired behavior for this NetworkPolicy.

<h2 class="pdoc-module-header" id="NetworkPolicyEgressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14869">interface NetworkPolicyEgressRule</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicyEgressRule is deprecated by
networking/v1/NetworkPolicyEgressRule. NetworkPolicyEgressRule describes a particular set of
traffic that is allowed out of pods matched by a NetworkPolicySpec's podSelector. The traffic
must match both ports and to. This type is beta-level in 1.8

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14876">property ports</a>
</h3>

```typescript
ports: NetworkPolicyPort[];
```


List of destination ports for outgoing traffic. Each item in this list is combined using a
logical OR. If this field is empty or missing, this rule matches all ports (traffic not
restricted by port). If this field is present and contains at least one item, then this
rule allows traffic only if the traffic matches at least one port in the list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14885">property to</a>
</h3>

```typescript
to: NetworkPolicyPeer[];
```


List of destinations for outgoing traffic of pods selected for this rule. Items in this
list are combined using a logical OR operation. If this field is empty or missing, this
rule matches all destinations (traffic not restricted by destination). If this field is
present and contains at least one item, this rule allows traffic only if the traffic
matches at least one item in the to list.

<h2 class="pdoc-module-header" id="NetworkPolicyIngressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14894">interface NetworkPolicyIngressRule</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicyIngressRule is deprecated by
networking/v1/NetworkPolicyIngressRule. This NetworkPolicyIngressRule matches traffic if and
only if the traffic matches both ports AND from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14902">property from</a>
</h3>

```typescript
from: NetworkPolicyPeer[];
```


List of sources which should be able to access the pods selected for this rule. Items in
this list are combined using a logical OR operation. If this field is empty or missing,
this rule matches all sources (traffic not restricted by source). If this field is present
and contains at least on item, this rule allows traffic only if the traffic matches at
least one item in the from list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14911">property ports</a>
</h3>

```typescript
ports: NetworkPolicyPort[];
```


List of ports which should be made accessible on the pods selected for this rule. Each item
in this list is combined using a logical OR. If this field is empty or missing, this rule
matches all ports (traffic not restricted by port). If this field is present and contains
at least one item, then this rule allows traffic only if the traffic matches at least one
port in the list.

<h2 class="pdoc-module-header" id="NetworkPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14919">interface NetworkPolicyList</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicyList is deprecated by
networking/v1/NetworkPolicyList. Network Policy List is a list of NetworkPolicy objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14926">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14931">property items</a>
</h3>

```typescript
items: NetworkPolicy[];
```


Items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14939">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14945">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="NetworkPolicyPeer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14953">interface NetworkPolicyPeer</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicyPeer is deprecated by
networking/v1/NetworkPolicyPeer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14958">property ipBlock</a>
</h3>

```typescript
ipBlock: IPBlock;
```


IPBlock defines policy on a particular IPBlock. If this field is set then neither of the
other fields can be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14968">property namespaceSelector</a>
</h3>

```typescript
namespaceSelector: LabelSelector;
```


Selects Namespaces using cluster-scoped labels. This field follows standard label selector
semantics; if present but empty, it selects all namespaces.

If PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching
PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods
in the Namespaces selected by NamespaceSelector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14978">property podSelector</a>
</h3>

```typescript
podSelector: LabelSelector;
```


This is a label selector which selects Pods. This field follows standard label selector
semantics; if present but empty, it selects all pods.

If NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods
matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects
the Pods matching PodSelector in the policy's own Namespace.

<h2 class="pdoc-module-header" id="NetworkPolicyPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14986">interface NetworkPolicyPort</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicyPort is deprecated by
networking/v1/NetworkPolicyPort.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14992">property port</a>
</h3>

```typescript
port: number | string;
```


If specified, the port on the given protocol.  This can either be a numerical or named port
on a pod.  If this field is not provided, this matches all port names and numbers. If
present, only traffic on the specified protocol AND port will be matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14998">property protocol</a>
</h3>

```typescript
protocol: string;
```


Optional.  The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified,
this field defaults to TCP.

<h2 class="pdoc-module-header" id="NetworkPolicySpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15006">interface NetworkPolicySpec</a>
</h2>

DEPRECATED 1.9 - This group version of NetworkPolicySpec is deprecated by
networking/v1/NetworkPolicySpec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15015">property egress</a>
</h3>

```typescript
egress: NetworkPolicyEgressRule[];
```


List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if
there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the
traffic), OR if the traffic matches at least one egress rule across all of the
NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this
NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it
selects are isolated by default). This field is beta-level in 1.8

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15025">property ingress</a>
</h3>

```typescript
ingress: NetworkPolicyIngressRule[];
```


List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if
there are no NetworkPolicies selecting the pod OR if the traffic source is the pod's local
node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy
objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy
does not allow any traffic (and serves solely to ensure that the pods it selects are
isolated by default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15034">property podSelector</a>
</h3>

```typescript
podSelector: LabelSelector;
```


Selects the pods to which this NetworkPolicy object applies.  The array of ingress rules is
applied to any pods selected by this field. Multiple network policies can select the same
set of pods.  In this case, the ingress rules for each are combined additively. This field
is NOT optional and follows standard label selector semantics. An empty podSelector matches
all pods in this namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15047">property policyTypes</a>
</h3>

```typescript
policyTypes: string[];
```


List of rule types that the NetworkPolicy relates to. Valid options are Ingress, Egress, or
Ingress,Egress. If this field is not specified, it will default based on the existence of
Ingress or Egress rules; policies that contain an Egress section are assumed to affect
Egress, and all policies (whether or not they contain an Ingress section) are assumed to
affect Ingress. If you want to write an egress-only policy, you must explicitly specify
policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no
egress is allowed, you must specify a policyTypes value that include "Egress" (since such a
policy would not include an Egress section and would otherwise default to just [ "Ingress"
]). This field is beta-level in 1.8

<h2 class="pdoc-module-header" id="PodSecurityPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15056">interface PodSecurityPolicy</a>
</h2>

PodSecurityPolicy governs the ability to make requests that affect the Security Context that
will be applied to a pod and container. Deprecated: use PodSecurityPolicy from policy API
Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15063">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15071">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15077">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15082">property spec</a>
</h3>

```typescript
spec: PodSecurityPolicySpec;
```


spec defines the policy enforced.

<h2 class="pdoc-module-header" id="PodSecurityPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15090">interface PodSecurityPolicyList</a>
</h2>

PodSecurityPolicyList is a list of PodSecurityPolicy objects. Deprecated: use
PodSecurityPolicyList from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15097">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15102">property items</a>
</h3>

```typescript
items: PodSecurityPolicy[];
```


items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15110">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15116">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="PodSecurityPolicySpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15124">interface PodSecurityPolicySpec</a>
</h2>

PodSecurityPolicySpec defines the policy enforced. Deprecated: use PodSecurityPolicySpec from
policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15129">property allowPrivilegeEscalation</a>
</h3>

```typescript
allowPrivilegeEscalation: boolean;
```


allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If
unspecified, defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15136">property allowedCapabilities</a>
</h3>

```typescript
allowedCapabilities: string[];
```


allowedCapabilities is a list of capabilities that can be requested to add to the
container. Capabilities in this field may be added at the pod author's discretion. You must
not list a capability in both allowedCapabilities and requiredDropCapabilities.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15143">property allowedFlexVolumes</a>
</h3>

```typescript
allowedFlexVolumes: AllowedFlexVolume[];
```


allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all
Flexvolumes may be used.  This parameter is effective only when the usage of the
Flexvolumes is allowed in the "volumes" field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15149">property allowedHostPaths</a>
</h3>

```typescript
allowedHostPaths: AllowedHostPath[];
```


allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths
may be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15156">property allowedProcMountTypes</a>
</h3>

```typescript
allowedProcMountTypes: string[];
```


AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that
only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to
be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15167">property allowedUnsafeSysctls</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15175">property defaultAddCapabilities</a>
</h3>

```typescript
defaultAddCapabilities: string[];
```


defaultAddCapabilities is the default set of capabilities that will be added to the
container unless the pod spec specifically drops the capability.  You may not list a
capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added
here are implicitly allowed, and need not be included in the allowedCapabilities list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15181">property defaultAllowPrivilegeEscalation</a>
</h3>

```typescript
defaultAllowPrivilegeEscalation: boolean;
```


defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain
more privileges than its parent process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15191">property forbiddenSysctls</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15196">property fsGroup</a>
</h3>

```typescript
fsGroup: FSGroupStrategyOptions;
```


fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15201">property hostIPC</a>
</h3>

```typescript
hostIPC: boolean;
```


hostIPC determines if the policy allows the use of HostIPC in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15206">property hostNetwork</a>
</h3>

```typescript
hostNetwork: boolean;
```


hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15211">property hostPID</a>
</h3>

```typescript
hostPID: boolean;
```


hostPID determines if the policy allows the use of HostPID in the pod spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15216">property hostPorts</a>
</h3>

```typescript
hostPorts: HostPortRange[];
```


hostPorts determines which host port ranges are allowed to be exposed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15221">property privileged</a>
</h3>

```typescript
privileged: boolean;
```


privileged determines if a pod can request to be run as privileged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15229">property readOnlyRootFilesystem</a>
</h3>

```typescript
readOnlyRootFilesystem: boolean;
```


readOnlyRootFilesystem when set to true will force containers to run with a read only root
file system.  If the container specifically requests to run with a non-read only root file
system the PSP should deny the pod. If set to false the container may run with a read only
root file system if it wishes but it will not be forced to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15235">property requiredDropCapabilities</a>
</h3>

```typescript
requiredDropCapabilities: string[];
```


requiredDropCapabilities are the capabilities that will be dropped from the container.
These are required to be dropped and cannot be added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15242">property runAsGroup</a>
</h3>

```typescript
runAsGroup: RunAsGroupStrategyOptions;
```


RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be
set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires
the RunAsGroup feature gate to be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15247">property runAsUser</a>
</h3>

```typescript
runAsUser: RunAsUserStrategyOptions;
```


runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15252">property seLinux</a>
</h3>

```typescript
seLinux: SELinuxStrategyOptions;
```


seLinux is the strategy that will dictate the allowable labels that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15258">property supplementalGroups</a>
</h3>

```typescript
supplementalGroups: SupplementalGroupsStrategyOptions;
```


supplementalGroups is the strategy that will dictate what supplemental groups are used by
the SecurityContext.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15264">property volumes</a>
</h3>

```typescript
volumes: string[];
```


volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be
used. To allow all volumes you may use '*'.

<h2 class="pdoc-module-header" id="ReplicaSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15273">interface ReplicaSet</a>
</h2>

DEPRECATED - This group version of ReplicaSet is deprecated by apps/v1beta2/ReplicaSet. See
the release notes for more information. ReplicaSet ensures that a specified number of pod
replicas are running at any given time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15280">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15288">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15295">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s)
that the ReplicaSet manages. Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15301">property spec</a>
</h3>

```typescript
spec: ReplicaSetSpec;
```


Spec defines the specification of the desired behavior of the ReplicaSet. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15308">property status</a>
</h3>

```typescript
status: ReplicaSetStatus;
```


Status is the most recently observed status of the ReplicaSet. This data may be out of date
by some window of time. Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="ReplicaSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15315">interface ReplicaSetCondition</a>
</h2>

ReplicaSetCondition describes the state of a replica set at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15319">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


The last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15324">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15329">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15334">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15339">property type</a>
</h3>

```typescript
type: string;
```


Type of replica set condition.

<h2 class="pdoc-module-header" id="ReplicaSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15346">interface ReplicaSetList</a>
</h2>

ReplicaSetList is a collection of ReplicaSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15353">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15359">property items</a>
</h3>

```typescript
items: ReplicaSet[];
```


List of ReplicaSets. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15367">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15373">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ReplicaSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15380">interface ReplicaSetSpec</a>
</h2>

ReplicaSetSpec is the specification of a ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15386">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15393">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the number of desired replicas. This is a pointer to distinguish between
explicit zero and unspecified. Defaults to 1. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15401">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Selector is a label query over pods that should match the replica count. If the selector is
empty, it is defaulted to the labels present on the pod template. Label keys and values
that must match in order to be controlled by this replica set. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15408">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template is the object that describes the pod that will be created if insufficient replicas
are detected. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

<h2 class="pdoc-module-header" id="ReplicaSetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15415">interface ReplicaSetStatus</a>
</h2>

ReplicaSetStatus represents the current status of a ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15419">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


The number of available replicas (ready for at least minReadySeconds) for this replica set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15424">property conditions</a>
</h3>

```typescript
conditions: ReplicaSetCondition[];
```


Represents the latest available observations of a replica set's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15430">property fullyLabeledReplicas</a>
</h3>

```typescript
fullyLabeledReplicas: number;
```


The number of pods that have labels matching the labels of the pod template of the
replicaset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15435">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


ObservedGeneration reflects the generation of the most recently observed ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15440">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


The number of ready replicas for this replica set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15446">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the most recently oberved number of replicas. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller

<h2 class="pdoc-module-header" id="RollbackConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15453">interface RollbackConfig</a>
</h2>

DEPRECATED.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15457">property revision</a>
</h3>

```typescript
revision: number;
```


The revision to rollback to. If set to 0, rollback to the last revision.

<h2 class="pdoc-module-header" id="RollingUpdateDaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15464">interface RollingUpdateDaemonSet</a>
</h2>

Spec to control the desired behavior of daemon set rolling update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15477">property maxUnavailable</a>
</h3>

```typescript
maxUnavailable: number | string;
```


The maximum number of DaemonSet pods that can be unavailable during the update. Value can
be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the
start of the update (ex: 10%). Absolute number is calculated from percentage by rounding
up. This cannot be 0. Default value is 1. Example: when this is set to 30%, at most 30% of
the total number of nodes that should be running the daemon pod (i.e.
status.desiredNumberScheduled) can have their pods stopped for an update at any given time.
The update starts by stopping at most 30% of those DaemonSet pods and then brings up new
DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other
DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are
available at all times during the update.

<h2 class="pdoc-module-header" id="RollingUpdateDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15484">interface RollingUpdateDeployment</a>
</h2>

Spec to control the desired behavior of rolling update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15495">property maxSurge</a>
</h3>

```typescript
maxSurge: number | string;
```


The maximum number of pods that can be scheduled above the desired number of pods. Value
can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not
be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up.
By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be
scaled up immediately when the rolling update starts, such that the total number of old and
new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be
scaled up further, ensuring that total number of pods running at any time during the update
is atmost 130% of desired pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15507">property maxUnavailable</a>
</h3>

```typescript
maxUnavailable: number | string;
```


The maximum number of pods that can be unavailable during the update. Value can be an
absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is
calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. By
default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be
scaled down to 70% of desired pods immediately when the rolling update starts. Once new
pods are ready, old RC can be scaled down further, followed by scaling up the new RC,
ensuring that the total number of pods available at all times during the update is at least
70% of desired pods.

<h2 class="pdoc-module-header" id="RunAsGroupStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15515">interface RunAsGroupStrategyOptions</a>
</h2>

RunAsGroupStrategyOptions defines the strategy type and any options used to create the
strategy. Deprecated: use RunAsGroupStrategyOptions from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15520">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of gids that may be used. If you would like to force a single
gid then supply a single range with the same start and end. Required for MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15525">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate the allowable RunAsGroup values that may be set.

<h2 class="pdoc-module-header" id="RunAsUserStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15533">interface RunAsUserStrategyOptions</a>
</h2>

RunAsUserStrategyOptions defines the strategy type and any options used to create the
strategy. Deprecated: use RunAsUserStrategyOptions from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15538">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of uids that may be used. If you would like to force a single
uid then supply a single range with the same start and end. Required for MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15543">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate the allowable RunAsUser values that may be set.

<h2 class="pdoc-module-header" id="SELinuxStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15551">interface SELinuxStrategyOptions</a>
</h2>

SELinuxStrategyOptions defines the strategy type and any options used to create the strategy.
Deprecated: use SELinuxStrategyOptions from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15555">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate the allowable labels that may be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15561">property seLinuxOptions</a>
</h3>

```typescript
seLinuxOptions: SELinuxOptions;
```


seLinuxOptions required to run as; required for MustRunAs More info:
https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

<h2 class="pdoc-module-header" id="Scale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15568">interface Scale</a>
</h2>

represents a scaling request for a resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15575">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15583">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15589">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15595">property spec</a>
</h3>

```typescript
spec: ScaleSpec;
```


defines the behavior of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15602">property status</a>
</h3>

```typescript
status: ScaleStatus;
```


current status of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
Read-only.

<h2 class="pdoc-module-header" id="ScaleSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15609">interface ScaleSpec</a>
</h2>

describes the attributes of a scale subresource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15613">property replicas</a>
</h3>

```typescript
replicas: number;
```


desired number of instances for the scaled object.

<h2 class="pdoc-module-header" id="ScaleStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15620">interface ScaleStatus</a>
</h2>

represents the current status of a scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15624">property replicas</a>
</h3>

```typescript
replicas: number;
```


actual number of observed instances of the scaled object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15630">property selector</a>
</h3>

```typescript
selector: { ... };
```


label query over pods that should match the replicas count. More info:
http://kubernetes.io/docs/user-guide/labels#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15640">property targetSelector</a>
</h3>

```typescript
targetSelector: string;
```


label selector for pods that should match the replicas count. This is a serializated
version of both map-based and more expressive set-based selectors. This is done to avoid
introspection in the clients. The string will be in the same format as the query-param
syntax. If the target type only supports map-based selectors, both this field and map-based
selector field are populated. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h2 class="pdoc-module-header" id="SupplementalGroupsStrategyOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15648">interface SupplementalGroupsStrategyOptions</a>
</h2>

SupplementalGroupsStrategyOptions defines the strategy type and options used to create the
strategy. Deprecated: use SupplementalGroupsStrategyOptions from policy API Group instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15654">property ranges</a>
</h3>

```typescript
ranges: IDRange[];
```


ranges are the allowed ranges of supplemental groups.  If you would like to force a single
supplemental group then supply a single range with the same start and end. Required for
MustRunAs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L15660">property rule</a>
</h3>

```typescript
rule: string;
```


rule is the strategy that will dictate what supplemental groups is used in the
SecurityContext.

