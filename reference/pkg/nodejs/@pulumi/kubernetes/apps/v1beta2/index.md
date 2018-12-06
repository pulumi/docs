---
title: Module apps/v1beta2
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apps</a> &gt; v1beta2

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isControllerRevision">function isControllerRevision</a>
* <a href="#isControllerRevisionList">function isControllerRevisionList</a>
* <a href="#isDaemonSet">function isDaemonSet</a>
* <a href="#isDaemonSetList">function isDaemonSetList</a>
* <a href="#isDeployment">function isDeployment</a>
* <a href="#isDeploymentList">function isDeploymentList</a>
* <a href="#isReplicaSet">function isReplicaSet</a>
* <a href="#isReplicaSetList">function isReplicaSetList</a>
* <a href="#isScale">function isScale</a>
* <a href="#isStatefulSet">function isStatefulSet</a>
* <a href="#isStatefulSetList">function isStatefulSetList</a>
* <a href="#ControllerRevision">interface ControllerRevision</a>
* <a href="#ControllerRevisionList">interface ControllerRevisionList</a>
* <a href="#DaemonSet">interface DaemonSet</a>
* <a href="#DaemonSetCondition">interface DaemonSetCondition</a>
* <a href="#DaemonSetList">interface DaemonSetList</a>
* <a href="#DaemonSetSpec">interface DaemonSetSpec</a>
* <a href="#DaemonSetStatus">interface DaemonSetStatus</a>
* <a href="#DaemonSetUpdateStrategy">interface DaemonSetUpdateStrategy</a>
* <a href="#Deployment">interface Deployment</a>
* <a href="#DeploymentCondition">interface DeploymentCondition</a>
* <a href="#DeploymentList">interface DeploymentList</a>
* <a href="#DeploymentSpec">interface DeploymentSpec</a>
* <a href="#DeploymentStatus">interface DeploymentStatus</a>
* <a href="#DeploymentStrategy">interface DeploymentStrategy</a>
* <a href="#ReplicaSet">interface ReplicaSet</a>
* <a href="#ReplicaSetCondition">interface ReplicaSetCondition</a>
* <a href="#ReplicaSetList">interface ReplicaSetList</a>
* <a href="#ReplicaSetSpec">interface ReplicaSetSpec</a>
* <a href="#ReplicaSetStatus">interface ReplicaSetStatus</a>
* <a href="#RollingUpdateDaemonSet">interface RollingUpdateDaemonSet</a>
* <a href="#RollingUpdateDeployment">interface RollingUpdateDeployment</a>
* <a href="#RollingUpdateStatefulSetStrategy">interface RollingUpdateStatefulSetStrategy</a>
* <a href="#Scale">interface Scale</a>
* <a href="#ScaleSpec">interface ScaleSpec</a>
* <a href="#ScaleStatus">interface ScaleStatus</a>
* <a href="#StatefulSet">interface StatefulSet</a>
* <a href="#StatefulSetCondition">interface StatefulSetCondition</a>
* <a href="#StatefulSetList">interface StatefulSetList</a>
* <a href="#StatefulSetSpec">interface StatefulSetSpec</a>
* <a href="#StatefulSetStatus">interface StatefulSetStatus</a>
* <a href="#StatefulSetUpdateStrategy">interface StatefulSetUpdateStrategy</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isControllerRevision">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3431">function isControllerRevision</a>
</h2>

```typescript
isControllerRevision(o: any): boolean
```

<h2 class="pdoc-module-header" id="isControllerRevisionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3467">function isControllerRevisionList</a>
</h2>

```typescript
isControllerRevisionList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3513">function isDaemonSet</a>
</h2>

```typescript
isDaemonSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDaemonSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3582">function isDaemonSetList</a>
</h2>

```typescript
isDaemonSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3748">function isDeployment</a>
</h2>

```typescript
isDeployment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3821">function isDeploymentList</a>
</h2>

```typescript
isDeploymentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicaSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3996">function isReplicaSet</a>
</h2>

```typescript
isReplicaSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicaSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4066">function isReplicaSetList</a>
</h2>

```typescript
isReplicaSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4252">function isScale</a>
</h2>

```typescript
isScale(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStatefulSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4338">function isStatefulSet</a>
</h2>

```typescript
isStatefulSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStatefulSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L4402">function isStatefulSetList</a>
</h2>

```typescript
isStatefulSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="ControllerRevision">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3215">interface ControllerRevision</a>
</h2>

DEPRECATED - This group version of ControllerRevision is deprecated by
apps/v1/ControllerRevision. See the release notes for more information. ControllerRevision
implements an immutable snapshot of state data. Clients are responsible for serializing and
deserializing the objects that contain their internal state. Once a ControllerRevision has
been successfully created, it can not be updated. The API Server will fail validation of all
requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted.
Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and
rollback, this object is beta. However, it may be subject to name and representation changes
in future releases, and clients should not depend on its stability. It is primarily for
internal use by controllers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3222">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3227">property data</a>
</h3>

```typescript
data: RawExtension;
```


Data is the serialized representation of the state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3235">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3241">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3246">property revision</a>
</h3>

```typescript
revision: number;
```


Revision indicates the revision of the state represented by Data.

<h2 class="pdoc-module-header" id="ControllerRevisionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3253">interface ControllerRevisionList</a>
</h2>

ControllerRevisionList is a resource containing a list of ControllerRevision objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3260">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3265">property items</a>
</h3>

```typescript
items: ControllerRevision[];
```


Items is the list of ControllerRevisions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3273">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3278">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="DaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3286">interface DaemonSet</a>
</h2>

DEPRECATED - This group version of DaemonSet is deprecated by apps/v1/DaemonSet. See the
release notes for more information. DaemonSet represents the configuration of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3293">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3301">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3307">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3313">property spec</a>
</h3>

```typescript
spec: DaemonSetSpec;
```


The desired behavior of this daemon set. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3320">property status</a>
</h3>

```typescript
status: DaemonSetStatus;
```


The current status of this daemon set. This data may be out of date by some window of time.
Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="DaemonSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3327">interface DaemonSetCondition</a>
</h2>

DaemonSetCondition describes the state of a DaemonSet at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3331">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3336">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3341">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3346">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3351">property type</a>
</h3>

```typescript
type: string;
```


Type of DaemonSet condition.

<h2 class="pdoc-module-header" id="DaemonSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3358">interface DaemonSetList</a>
</h2>

DaemonSetList is a collection of daemon sets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3365">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3370">property items</a>
</h3>

```typescript
items: DaemonSet[];
```


A list of daemon sets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3378">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3384">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="DaemonSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3391">interface DaemonSetSpec</a>
</h2>

DaemonSetSpec is the specification of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3397">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


The minimum number of seconds for which a newly created DaemonSet pod should be ready
without any of its container crashing, for it to be considered available. Defaults to 0
(pod will be considered available as soon as it is ready).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3403">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


The number of old history to retain to allow rollback. This is a pointer to distinguish
between explicit zero and not specified. Defaults to 10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3410">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


A label query over pods that are managed by the daemon set. Must match in order to be
controlled. It must match the pod template's labels. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3418">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


An object that describes the pod that will be created. The DaemonSet will create exactly
one copy of this pod on every node that matches the template's node selector (or on every
node if no node selector is specified). More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3423">property updateStrategy</a>
</h3>

```typescript
updateStrategy: DaemonSetUpdateStrategy;
```


An update strategy to replace existing DaemonSet pods with new pods.

<h2 class="pdoc-module-header" id="DaemonSetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3430">interface DaemonSetStatus</a>
</h2>

DaemonSetStatus represents the current status of a daemon set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3436">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a
collision avoidance mechanism when it needs to create the name for the newest
ControllerRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3441">property conditions</a>
</h3>

```typescript
conditions: DaemonSetCondition[];
```


Represents the latest available observations of a DaemonSet's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3447">property currentNumberScheduled</a>
</h3>

```typescript
currentNumberScheduled: number;
```


The number of nodes that are running at least 1 daemon pod and are supposed to run the
daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3454">property desiredNumberScheduled</a>
</h3>

```typescript
desiredNumberScheduled: number;
```


The total number of nodes that should be running the daemon pod (including nodes correctly
running the daemon pod). More info:
https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3460">property numberAvailable</a>
</h3>

```typescript
numberAvailable: number;
```


The number of nodes that should be running the daemon pod and have one or more of the
daemon pod running and available (ready for at least spec.minReadySeconds)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3466">property numberMisscheduled</a>
</h3>

```typescript
numberMisscheduled: number;
```


The number of nodes that are running the daemon pod, but are not supposed to run the daemon
pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3472">property numberReady</a>
</h3>

```typescript
numberReady: number;
```


The number of nodes that should be running the daemon pod and have one or more of the
daemon pod running and ready.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3478">property numberUnavailable</a>
</h3>

```typescript
numberUnavailable: number;
```


The number of nodes that should be running the daemon pod and have none of the daemon pod
running and available (ready for at least spec.minReadySeconds)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3483">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


The most recent generation observed by the daemon set controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3488">property updatedNumberScheduled</a>
</h3>

```typescript
updatedNumberScheduled: number;
```


The total number of nodes that are running updated daemon pod

<h2 class="pdoc-module-header" id="DaemonSetUpdateStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3495">interface DaemonSetUpdateStrategy</a>
</h2>

DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3499">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateDaemonSet;
```


Rolling update config params. Present only if type = "RollingUpdate".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3504">property type</a>
</h3>

```typescript
type: string;
```


Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.

<h2 class="pdoc-module-header" id="Deployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3513">interface Deployment</a>
</h2>

DEPRECATED - This group version of Deployment is deprecated by apps/v1/Deployment. See the
release notes for more information. Deployment enables declarative updates for Pods and
ReplicaSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3520">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3528">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3533">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3538">property spec</a>
</h3>

```typescript
spec: DeploymentSpec;
```


Specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3543">property status</a>
</h3>

```typescript
status: DeploymentStatus;
```


Most recently observed status of the Deployment.

<h2 class="pdoc-module-header" id="DeploymentCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3550">interface DeploymentCondition</a>
</h2>

DeploymentCondition describes the state of a deployment at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3554">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3559">property lastUpdateTime</a>
</h3>

```typescript
lastUpdateTime: string;
```


The last time this condition was updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3564">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3569">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3574">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3579">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment condition.

<h2 class="pdoc-module-header" id="DeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3586">interface DeploymentList</a>
</h2>

DeploymentList is a list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3593">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3598">property items</a>
</h3>

```typescript
items: Deployment[];
```


Items is the list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3606">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3611">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata.

<h2 class="pdoc-module-header" id="DeploymentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3618">interface DeploymentSpec</a>
</h2>

DeploymentSpec is the specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3624">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3629">property paused</a>
</h3>

```typescript
paused: boolean;
```


Indicates that the deployment is paused.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3638">property progressDeadlineSeconds</a>
</h3>

```typescript
progressDeadlineSeconds: number;
```


The maximum time in seconds for a deployment to make progress before it is considered to be
failed. The deployment controller will continue to process failed deployments and a
condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status.
Note that progress will not be estimated during the time a deployment is paused. Defaults
to 600s.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3644">property replicas</a>
</h3>

```typescript
replicas: number;
```


Number of desired pods. This is a pointer to distinguish between explicit zero and not
specified. Defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3650">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish
between explicit zero and not specified. Defaults to 10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3656">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the
ones affected by this deployment. It must match the pod template's labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3661">property strategy</a>
</h3>

```typescript
strategy: DeploymentStrategy;
```


The deployment strategy to use to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3666">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template describes the pods that will be created.

<h2 class="pdoc-module-header" id="DeploymentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3673">interface DeploymentStatus</a>
</h2>

DeploymentStatus is the most recently observed status of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3678">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


Total number of available pods (ready for at least minReadySeconds) targeted by this
deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3684">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


Count of hash collisions for the Deployment. The Deployment controller uses this field as a
collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3689">property conditions</a>
</h3>

```typescript
conditions: DeploymentCondition[];
```


Represents the latest available observations of a deployment's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3694">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


The generation observed by the deployment controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3699">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


Total number of ready pods targeted by this deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3705">property replicas</a>
</h3>

```typescript
replicas: number;
```


Total number of non-terminated pods targeted by this deployment (their labels match the
selector).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3713">property unavailableReplicas</a>
</h3>

```typescript
unavailableReplicas: number;
```


Total number of unavailable pods targeted by this deployment. This is the total number of
pods that are still required for the deployment to have 100% available capacity. They may
either be pods that are running but not yet available or pods that still have not been
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3719">property updatedReplicas</a>
</h3>

```typescript
updatedReplicas: number;
```


Total number of non-terminated pods targeted by this deployment that have the desired
template spec.

<h2 class="pdoc-module-header" id="DeploymentStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3726">interface DeploymentStrategy</a>
</h2>

DeploymentStrategy describes how to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3730">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateDeployment;
```


Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3735">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.

<h2 class="pdoc-module-header" id="ReplicaSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3744">interface ReplicaSet</a>
</h2>

DEPRECATED - This group version of ReplicaSet is deprecated by apps/v1/ReplicaSet. See the
release notes for more information. ReplicaSet ensures that a specified number of pod
replicas are running at any given time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3751">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3759">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3766">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s)
that the ReplicaSet manages. Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3772">property spec</a>
</h3>

```typescript
spec: ReplicaSetSpec;
```


Spec defines the specification of the desired behavior of the ReplicaSet. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3779">property status</a>
</h3>

```typescript
status: ReplicaSetStatus;
```


Status is the most recently observed status of the ReplicaSet. This data may be out of date
by some window of time. Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="ReplicaSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3786">interface ReplicaSetCondition</a>
</h2>

ReplicaSetCondition describes the state of a replica set at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3790">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


The last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3795">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3800">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3805">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3810">property type</a>
</h3>

```typescript
type: string;
```


Type of replica set condition.

<h2 class="pdoc-module-header" id="ReplicaSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3817">interface ReplicaSetList</a>
</h2>

ReplicaSetList is a collection of ReplicaSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3824">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3830">property items</a>
</h3>

```typescript
items: ReplicaSet[];
```


List of ReplicaSets. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3838">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3844">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ReplicaSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3851">interface ReplicaSetSpec</a>
</h2>

ReplicaSetSpec is the specification of a ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3857">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3864">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the number of desired replicas. This is a pointer to distinguish between
explicit zero and unspecified. Defaults to 1. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3872">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Selector is a label query over pods that should match the replica count. Label keys and
values that must match in order to be controlled by this replica set. It must match the pod
template's labels. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3879">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template is the object that describes the pod that will be created if insufficient replicas
are detected. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

<h2 class="pdoc-module-header" id="ReplicaSetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3886">interface ReplicaSetStatus</a>
</h2>

ReplicaSetStatus represents the current status of a ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3890">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


The number of available replicas (ready for at least minReadySeconds) for this replica set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3895">property conditions</a>
</h3>

```typescript
conditions: ReplicaSetCondition[];
```


Represents the latest available observations of a replica set's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3901">property fullyLabeledReplicas</a>
</h3>

```typescript
fullyLabeledReplicas: number;
```


The number of pods that have labels matching the labels of the pod template of the
replicaset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3906">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


ObservedGeneration reflects the generation of the most recently observed ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3911">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


The number of ready replicas for this replica set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3917">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the most recently oberved number of replicas. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller

<h2 class="pdoc-module-header" id="RollingUpdateDaemonSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3924">interface RollingUpdateDaemonSet</a>
</h2>

Spec to control the desired behavior of daemon set rolling update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3937">property maxUnavailable</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3944">interface RollingUpdateDeployment</a>
</h2>

Spec to control the desired behavior of rolling update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3955">property maxSurge</a>
</h3>

```typescript
maxSurge: number | string;
```


The maximum number of pods that can be scheduled above the desired number of pods. Value
can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not
be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up.
Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up
immediately when the rolling update starts, such that the total number of old and new pods
do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be
scaled up further, ensuring that total number of pods running at any time during the update
is atmost 130% of desired pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3967">property maxUnavailable</a>
</h3>

```typescript
maxUnavailable: number | string;
```


The maximum number of pods that can be unavailable during the update. Value can be an
absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is
calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults
to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of
desired pods immediately when the rolling update starts. Once new pods are ready, old
ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring
that the total number of pods available at all times during the update is at least 70% of
desired pods.

<h2 class="pdoc-module-header" id="RollingUpdateStatefulSetStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3975">interface RollingUpdateStatefulSetStrategy</a>
</h2>

RollingUpdateStatefulSetStrategy is used to communicate parameter for
RollingUpdateStatefulSetStrategyType.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3980">property partition</a>
</h3>

```typescript
partition: number;
```


Partition indicates the ordinal at which the StatefulSet should be partitioned. Default
value is 0.

<h2 class="pdoc-module-header" id="Scale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3987">interface Scale</a>
</h2>

Scale represents a scaling request for a resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3994">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4002">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4008">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4014">property spec</a>
</h3>

```typescript
spec: ScaleSpec;
```


defines the behavior of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4021">property status</a>
</h3>

```typescript
status: ScaleStatus;
```


current status of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
Read-only.

<h2 class="pdoc-module-header" id="ScaleSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4028">interface ScaleSpec</a>
</h2>

ScaleSpec describes the attributes of a scale subresource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4032">property replicas</a>
</h3>

```typescript
replicas: number;
```


desired number of instances for the scaled object.

<h2 class="pdoc-module-header" id="ScaleStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4039">interface ScaleStatus</a>
</h2>

ScaleStatus represents the current status of a scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4043">property replicas</a>
</h3>

```typescript
replicas: number;
```


actual number of observed instances of the scaled object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4049">property selector</a>
</h3>

```typescript
selector: { ... };
```


label query over pods that should match the replicas count. More info:
http://kubernetes.io/docs/user-guide/labels#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4059">property targetSelector</a>
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

<h2 class="pdoc-module-header" id="StatefulSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4072">interface StatefulSet</a>
</h2>

DEPRECATED - This group version of StatefulSet is deprecated by apps/v1/StatefulSet. See the
release notes for more information. StatefulSet represents a set of pods with consistent
identities. Identities are defined as:
 - Network: A single stable DNS and hostname.
 - Storage: As many VolumeClaims as requested.
The StatefulSet guarantees that a given network identity will always map to the same storage
identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4079">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4087">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4090">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4095">property spec</a>
</h3>

```typescript
spec: StatefulSetSpec;
```


Spec defines the desired identities of pods in this set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4101">property status</a>
</h3>

```typescript
status: StatefulSetStatus;
```


Status is the current status of Pods in this StatefulSet. This data may be out of date by
some window of time.

<h2 class="pdoc-module-header" id="StatefulSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4108">interface StatefulSetCondition</a>
</h2>

StatefulSetCondition describes the state of a statefulset at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4112">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4117">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4122">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4127">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4132">property type</a>
</h3>

```typescript
type: string;
```


Type of statefulset condition.

<h2 class="pdoc-module-header" id="StatefulSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4139">interface StatefulSetList</a>
</h2>

StatefulSetList is a collection of StatefulSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4146">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4149">property items</a>
</h3>

```typescript
items: StatefulSet[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4157">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4160">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="StatefulSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4167">interface StatefulSetSpec</a>
</h2>

A StatefulSetSpec is the specification of a StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4176">property podManagementPolicy</a>
</h3>

```typescript
podManagementPolicy: string;
```


podManagementPolicy controls how pods are created during initial scale up, when replacing
pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are
created in increasing order (pod-0, then pod-1, etc) and the controller will wait until
each pod is ready before continuing. When scaling down, the pods are removed in the
opposite order. The alternative policy is `Parallel` which will create pods in parallel to
match the desired scale without waiting, and on scale down will delete all pods at once.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4183">property replicas</a>
</h3>

```typescript
replicas: number;
```


replicas is the desired number of replicas of the given Template. These are replicas in the
sense that they are instantiations of the same Template, but individual replicas also have
a consistent identity. If unspecified, defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4190">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


revisionHistoryLimit is the maximum number of revisions that will be maintained in the
StatefulSet's revision history. The revision history consists of all revisions not
represented by a currently applied StatefulSetSpec version. The default value is 10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4197">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is a label query over pods that should match the replica count. It must match the
pod template's labels. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4206">property serviceName</a>
</h3>

```typescript
serviceName: string;
```


serviceName is the name of the service that governs this StatefulSet. This service must
exist before the StatefulSet, and is responsible for the network identity of the set. Pods
get DNS/hostnames that follow the pattern:
pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is
managed by the StatefulSet controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4213">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


template is the object that describes the pod that will be created if insufficient replicas
are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have
a unique identity from the rest of the StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4219">property updateStrategy</a>
</h3>

```typescript
updateStrategy: StatefulSetUpdateStrategy;
```


updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods
in the StatefulSet when a revision is made to Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4228">property volumeClaimTemplates</a>
</h3>

```typescript
volumeClaimTemplates: PersistentVolumeClaim[];
```


volumeClaimTemplates is a list of claims that pods are allowed to reference. The
StatefulSet controller is responsible for mapping network identities to claims in a way
that maintains the identity of a pod. Every claim in this list must have at least one
matching (by name) volumeMount in one container in the template. A claim in this list takes
precedence over any volumes in the template, with the same name.

<h2 class="pdoc-module-header" id="StatefulSetStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4235">interface StatefulSetStatus</a>
</h2>

StatefulSetStatus represents the current state of a StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4241">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet
controller uses this field as a collision avoidance mechanism when it needs to create the
name for the newest ControllerRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4246">property conditions</a>
</h3>

```typescript
conditions: StatefulSetCondition[];
```


Represents the latest available observations of a statefulset's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4252">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


currentReplicas is the number of Pods created by the StatefulSet controller from the
StatefulSet version indicated by currentRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4258">property currentRevision</a>
</h3>

```typescript
currentRevision: string;
```


currentRevision, if not empty, indicates the version of the StatefulSet used to generate
Pods in the sequence [0,currentReplicas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4265">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


observedGeneration is the most recent generation observed for this StatefulSet. It
corresponds to the StatefulSet's generation, which is updated on mutation by the API
Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4271">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready
Condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4276">property replicas</a>
</h3>

```typescript
replicas: number;
```


replicas is the number of Pods created by the StatefulSet controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4282">property updateRevision</a>
</h3>

```typescript
updateRevision: string;
```


updateRevision, if not empty, indicates the version of the StatefulSet used to generate
Pods in the sequence [replicas-updatedReplicas,replicas)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4288">property updatedReplicas</a>
</h3>

```typescript
updatedReplicas: number;
```


updatedReplicas is the number of Pods created by the StatefulSet controller from the
StatefulSet version indicated by updateRevision.

<h2 class="pdoc-module-header" id="StatefulSetUpdateStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4297">interface StatefulSetUpdateStrategy</a>
</h2>

StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to
perform updates. It includes any additional parameters necessary to perform the update for
the indicated strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4302">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateStatefulSetStrategy;
```


RollingUpdate is used to communicate parameters when Type is
RollingUpdateStatefulSetStrategyType.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4307">property type</a>
</h3>

```typescript
type: string;
```


Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.

