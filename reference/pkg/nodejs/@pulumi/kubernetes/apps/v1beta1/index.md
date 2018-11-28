---
title: Module apps/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apps</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isControllerRevision">function isControllerRevision</a>
* <a href="#isControllerRevisionList">function isControllerRevisionList</a>
* <a href="#isDeployment">function isDeployment</a>
* <a href="#isDeploymentList">function isDeploymentList</a>
* <a href="#isDeploymentRollback">function isDeploymentRollback</a>
* <a href="#isScale">function isScale</a>
* <a href="#isStatefulSet">function isStatefulSet</a>
* <a href="#isStatefulSetList">function isStatefulSetList</a>
* <a href="#ControllerRevision">interface ControllerRevision</a>
* <a href="#ControllerRevisionList">interface ControllerRevisionList</a>
* <a href="#Deployment">interface Deployment</a>
* <a href="#DeploymentCondition">interface DeploymentCondition</a>
* <a href="#DeploymentList">interface DeploymentList</a>
* <a href="#DeploymentRollback">interface DeploymentRollback</a>
* <a href="#DeploymentSpec">interface DeploymentSpec</a>
* <a href="#DeploymentStatus">interface DeploymentStatus</a>
* <a href="#DeploymentStrategy">interface DeploymentStrategy</a>
* <a href="#RollbackConfig">interface RollbackConfig</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2517">function isControllerRevision</a>
</h2>

```typescript
isControllerRevision(o: any): boolean
```

<h2 class="pdoc-module-header" id="isControllerRevisionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2553">function isControllerRevisionList</a>
</h2>

```typescript
isControllerRevisionList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2596">function isDeployment</a>
</h2>

```typescript
isDeployment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2669">function isDeploymentList</a>
</h2>

```typescript
isDeploymentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isDeploymentRollback">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2710">function isDeploymentRollback</a>
</h2>

```typescript
isDeploymentRollback(o: any): boolean
```

<h2 class="pdoc-module-header" id="isScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L2944">function isScale</a>
</h2>

```typescript
isScale(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStatefulSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3030">function isStatefulSet</a>
</h2>

```typescript
isStatefulSet(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStatefulSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L3094">function isStatefulSetList</a>
</h2>

```typescript
isStatefulSetList(o: any): boolean
```

<h2 class="pdoc-module-header" id="ControllerRevision">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2349">interface ControllerRevision</a>
</h2>

DEPRECATED - This group version of ControllerRevision is deprecated by
apps/v1beta2/ControllerRevision. See the release notes for more information.
ControllerRevision implements an immutable snapshot of state data. Clients are responsible
for serializing and deserializing the objects that contain their internal state. Once a
ControllerRevision has been successfully created, it can not be updated. The API Server will
fail validation of all requests that attempt to mutate the Data field. ControllerRevisions
may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet
controllers for update and rollback, this object is beta. However, it may be subject to name
and representation changes in future releases, and clients should not depend on its
stability. It is primarily for internal use by controllers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2356">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2361">property data</a>
</h3>

```typescript
data: RawExtension;
```


Data is the serialized representation of the state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2369">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2375">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2380">property revision</a>
</h3>

```typescript
revision: number;
```


Revision indicates the revision of the state represented by Data.

<h2 class="pdoc-module-header" id="ControllerRevisionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2387">interface ControllerRevisionList</a>
</h2>

ControllerRevisionList is a resource containing a list of ControllerRevision objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2394">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2399">property items</a>
</h3>

```typescript
items: ControllerRevision[];
```


Items is the list of ControllerRevisions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2407">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2412">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="Deployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2421">interface Deployment</a>
</h2>

DEPRECATED - This group version of Deployment is deprecated by apps/v1beta2/Deployment. See
the release notes for more information. Deployment enables declarative updates for Pods and
ReplicaSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2428">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2436">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2441">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2446">property spec</a>
</h3>

```typescript
spec: DeploymentSpec;
```


Specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2451">property status</a>
</h3>

```typescript
status: DeploymentStatus;
```


Most recently observed status of the Deployment.

<h2 class="pdoc-module-header" id="DeploymentCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2458">interface DeploymentCondition</a>
</h2>

DeploymentCondition describes the state of a deployment at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2462">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2467">property lastUpdateTime</a>
</h3>

```typescript
lastUpdateTime: string;
```


The last time this condition was updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2472">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2477">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2482">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2487">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment condition.

<h2 class="pdoc-module-header" id="DeploymentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2494">interface DeploymentList</a>
</h2>

DeploymentList is a list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2501">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2506">property items</a>
</h3>

```typescript
items: Deployment[];
```


Items is the list of Deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2514">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2519">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata.

<h2 class="pdoc-module-header" id="DeploymentRollback">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2526">interface DeploymentRollback</a>
</h2>

DEPRECATED. DeploymentRollback stores the information required to rollback a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2533">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2541">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2546">property name</a>
</h3>

```typescript
name: string;
```


Required: This must match the Name of a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2551">property rollbackTo</a>
</h3>

```typescript
rollbackTo: RollbackConfig;
```


The config of this deployment rollback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2556">property updatedAnnotations</a>
</h3>

```typescript
updatedAnnotations: { ... };
```


The annotations to be updated to a deployment

<h2 class="pdoc-module-header" id="DeploymentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2563">interface DeploymentSpec</a>
</h2>

DeploymentSpec is the specification of the desired behavior of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2569">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2574">property paused</a>
</h3>

```typescript
paused: boolean;
```


Indicates that the deployment is paused.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2583">property progressDeadlineSeconds</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2589">property replicas</a>
</h3>

```typescript
replicas: number;
```


Number of desired pods. This is a pointer to distinguish between explicit zero and not
specified. Defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2595">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish
between explicit zero and not specified. Defaults to 2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2601">property rollbackTo</a>
</h3>

```typescript
rollbackTo: RollbackConfig;
```


DEPRECATED. The config this deployment is rolling back to. Will be cleared after rollback
is done.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2607">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the
ones affected by this deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2612">property strategy</a>
</h3>

```typescript
strategy: DeploymentStrategy;
```


The deployment strategy to use to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2617">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template describes the pods that will be created.

<h2 class="pdoc-module-header" id="DeploymentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2624">interface DeploymentStatus</a>
</h2>

DeploymentStatus is the most recently observed status of the Deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2629">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


Total number of available pods (ready for at least minReadySeconds) targeted by this
deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2635">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


Count of hash collisions for the Deployment. The Deployment controller uses this field as a
collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2640">property conditions</a>
</h3>

```typescript
conditions: DeploymentCondition[];
```


Represents the latest available observations of a deployment's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2645">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


The generation observed by the deployment controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2650">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


Total number of ready pods targeted by this deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2656">property replicas</a>
</h3>

```typescript
replicas: number;
```


Total number of non-terminated pods targeted by this deployment (their labels match the
selector).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2664">property unavailableReplicas</a>
</h3>

```typescript
unavailableReplicas: number;
```


Total number of unavailable pods targeted by this deployment. This is the total number of
pods that are still required for the deployment to have 100% available capacity. They may
either be pods that are running but not yet available or pods that still have not been
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2670">property updatedReplicas</a>
</h3>

```typescript
updatedReplicas: number;
```


Total number of non-terminated pods targeted by this deployment that have the desired
template spec.

<h2 class="pdoc-module-header" id="DeploymentStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2677">interface DeploymentStrategy</a>
</h2>

DeploymentStrategy describes how to replace existing pods with new ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2681">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateDeployment;
```


Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2686">property type</a>
</h3>

```typescript
type: string;
```


Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.

<h2 class="pdoc-module-header" id="RollbackConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2693">interface RollbackConfig</a>
</h2>

DEPRECATED.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2697">property revision</a>
</h3>

```typescript
revision: number;
```


The revision to rollback to. If set to 0, rollback to the last revision.

<h2 class="pdoc-module-header" id="RollingUpdateDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2704">interface RollingUpdateDeployment</a>
</h2>

Spec to control the desired behavior of rolling update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2715">property maxSurge</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2727">property maxUnavailable</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2735">interface RollingUpdateStatefulSetStrategy</a>
</h2>

RollingUpdateStatefulSetStrategy is used to communicate parameter for
RollingUpdateStatefulSetStrategyType.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2739">property partition</a>
</h3>

```typescript
partition: number;
```


Partition indicates the ordinal at which the StatefulSet should be partitioned.

<h2 class="pdoc-module-header" id="Scale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2746">interface Scale</a>
</h2>

Scale represents a scaling request for a resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2753">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2761">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2767">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2773">property spec</a>
</h3>

```typescript
spec: ScaleSpec;
```


defines the behavior of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2780">property status</a>
</h3>

```typescript
status: ScaleStatus;
```


current status of the scale. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
Read-only.

<h2 class="pdoc-module-header" id="ScaleSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2787">interface ScaleSpec</a>
</h2>

ScaleSpec describes the attributes of a scale subresource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2791">property replicas</a>
</h3>

```typescript
replicas: number;
```


desired number of instances for the scaled object.

<h2 class="pdoc-module-header" id="ScaleStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2798">interface ScaleStatus</a>
</h2>

ScaleStatus represents the current status of a scale subresource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2802">property replicas</a>
</h3>

```typescript
replicas: number;
```


actual number of observed instances of the scaled object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2808">property selector</a>
</h3>

```typescript
selector: { ... };
```


label query over pods that should match the replicas count. More info:
http://kubernetes.io/docs/user-guide/labels#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2818">property targetSelector</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2831">interface StatefulSet</a>
</h2>

DEPRECATED - This group version of StatefulSet is deprecated by apps/v1beta2/StatefulSet. See
the release notes for more information. StatefulSet represents a set of pods with consistent
identities. Identities are defined as:
 - Network: A single stable DNS and hostname.
 - Storage: As many VolumeClaims as requested.
The StatefulSet guarantees that a given network identity will always map to the same storage
identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2838">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2846">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2849">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2854">property spec</a>
</h3>

```typescript
spec: StatefulSetSpec;
```


Spec defines the desired identities of pods in this set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2860">property status</a>
</h3>

```typescript
status: StatefulSetStatus;
```


Status is the current status of Pods in this StatefulSet. This data may be out of date by
some window of time.

<h2 class="pdoc-module-header" id="StatefulSetCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2867">interface StatefulSetCondition</a>
</h2>

StatefulSetCondition describes the state of a statefulset at a certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2871">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2876">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2881">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2886">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2891">property type</a>
</h3>

```typescript
type: string;
```


Type of statefulset condition.

<h2 class="pdoc-module-header" id="StatefulSetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2898">interface StatefulSetList</a>
</h2>

StatefulSetList is a collection of StatefulSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2905">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2908">property items</a>
</h3>

```typescript
items: StatefulSet[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2916">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2919">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="StatefulSetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2926">interface StatefulSetSpec</a>
</h2>

A StatefulSetSpec is the specification of a StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2935">property podManagementPolicy</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2942">property replicas</a>
</h3>

```typescript
replicas: number;
```


replicas is the desired number of replicas of the given Template. These are replicas in the
sense that they are instantiations of the same Template, but individual replicas also have
a consistent identity. If unspecified, defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2949">property revisionHistoryLimit</a>
</h3>

```typescript
revisionHistoryLimit: number;
```


revisionHistoryLimit is the maximum number of revisions that will be maintained in the
StatefulSet's revision history. The revision history consists of all revisions not
represented by a currently applied StatefulSetSpec version. The default value is 10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2956">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is a label query over pods that should match the replica count. If empty,
defaulted to labels on the pod template. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2965">property serviceName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2972">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


template is the object that describes the pod that will be created if insufficient replicas
are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have
a unique identity from the rest of the StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2978">property updateStrategy</a>
</h3>

```typescript
updateStrategy: StatefulSetUpdateStrategy;
```


updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods
in the StatefulSet when a revision is made to Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2987">property volumeClaimTemplates</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L2994">interface StatefulSetStatus</a>
</h2>

StatefulSetStatus represents the current state of a StatefulSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3000">property collisionCount</a>
</h3>

```typescript
collisionCount: number;
```


collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet
controller uses this field as a collision avoidance mechanism when it needs to create the
name for the newest ControllerRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3005">property conditions</a>
</h3>

```typescript
conditions: StatefulSetCondition[];
```


Represents the latest available observations of a statefulset's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3011">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


currentReplicas is the number of Pods created by the StatefulSet controller from the
StatefulSet version indicated by currentRevision.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3017">property currentRevision</a>
</h3>

```typescript
currentRevision: string;
```


currentRevision, if not empty, indicates the version of the StatefulSet used to generate
Pods in the sequence [0,currentReplicas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3024">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


observedGeneration is the most recent generation observed for this StatefulSet. It
corresponds to the StatefulSet's generation, which is updated on mutation by the API
Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3030">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready
Condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3035">property replicas</a>
</h3>

```typescript
replicas: number;
```


replicas is the number of Pods created by the StatefulSet controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3041">property updateRevision</a>
</h3>

```typescript
updateRevision: string;
```


updateRevision, if not empty, indicates the version of the StatefulSet used to generate
Pods in the sequence [replicas-updatedReplicas,replicas)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3047">property updatedReplicas</a>
</h3>

```typescript
updatedReplicas: number;
```


updatedReplicas is the number of Pods created by the StatefulSet controller from the
StatefulSet version indicated by updateRevision.

<h2 class="pdoc-module-header" id="StatefulSetUpdateStrategy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3056">interface StatefulSetUpdateStrategy</a>
</h2>

StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to
perform updates. It includes any additional parameters necessary to perform the update for
the indicated strategy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3061">property rollingUpdate</a>
</h3>

```typescript
rollingUpdate: RollingUpdateStatefulSetStrategy;
```


RollingUpdate is used to communicate parameters when Type is
RollingUpdateStatefulSetStrategyType.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3066">property type</a>
</h3>

```typescript
type: string;
```


Type indicates the type of the StatefulSetUpdateStrategy.

