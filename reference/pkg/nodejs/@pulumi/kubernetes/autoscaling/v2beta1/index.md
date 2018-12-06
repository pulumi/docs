---
title: Module autoscaling/v2beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">autoscaling</a> &gt; v2beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCrossVersionObjectReference">function isCrossVersionObjectReference</a>
* <a href="#isHorizontalPodAutoscaler">function isHorizontalPodAutoscaler</a>
* <a href="#isHorizontalPodAutoscalerList">function isHorizontalPodAutoscalerList</a>
* <a href="#CrossVersionObjectReference">interface CrossVersionObjectReference</a>
* <a href="#ExternalMetricSource">interface ExternalMetricSource</a>
* <a href="#ExternalMetricStatus">interface ExternalMetricStatus</a>
* <a href="#HorizontalPodAutoscaler">interface HorizontalPodAutoscaler</a>
* <a href="#HorizontalPodAutoscalerCondition">interface HorizontalPodAutoscalerCondition</a>
* <a href="#HorizontalPodAutoscalerList">interface HorizontalPodAutoscalerList</a>
* <a href="#HorizontalPodAutoscalerSpec">interface HorizontalPodAutoscalerSpec</a>
* <a href="#HorizontalPodAutoscalerStatus">interface HorizontalPodAutoscalerStatus</a>
* <a href="#MetricSpec">interface MetricSpec</a>
* <a href="#MetricStatus">interface MetricStatus</a>
* <a href="#ObjectMetricSource">interface ObjectMetricSource</a>
* <a href="#ObjectMetricStatus">interface ObjectMetricStatus</a>
* <a href="#PodsMetricSource">interface PodsMetricSource</a>
* <a href="#PodsMetricStatus">interface PodsMetricStatus</a>
* <a href="#ResourceMetricSource">interface ResourceMetricSource</a>
* <a href="#ResourceMetricStatus">interface ResourceMetricStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6155">function isCrossVersionObjectReference</a>
</h2>

```typescript
isCrossVersionObjectReference(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6259">function isHorizontalPodAutoscaler</a>
</h2>

```typescript
isHorizontalPodAutoscaler(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6328">function isHorizontalPodAutoscalerList</a>
</h2>

```typescript
isHorizontalPodAutoscalerList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5793">interface CrossVersionObjectReference</a>
</h2>

CrossVersionObjectReference contains enough information to let you identify the referred
resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5797">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5803">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5808">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names

<h2 class="pdoc-module-header" id="ExternalMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5817">interface ExternalMetricSource</a>
</h2>

ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes
object (for example length of queue in cloud messaging service, or QPS from loadbalancer
running outside of cluster). Exactly one "target" type should be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5821">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5826">property metricSelector</a>
</h3>

```typescript
metricSelector: LabelSelector;
```


metricSelector is used to identify a specific time series within a given metric.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5832">property targetAverageValue</a>
</h3>

```typescript
targetAverageValue: string;
```


targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually
exclusive with TargetValue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5838">property targetValue</a>
</h3>

```typescript
targetValue: string;
```


targetValue is the target value of the metric (as a quantity). Mutually exclusive with
TargetAverageValue.

<h2 class="pdoc-module-header" id="ExternalMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5846">interface ExternalMetricStatus</a>
</h2>

ExternalMetricStatus indicates the current value of a global metric not associated with any
Kubernetes object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5850">property currentAverageValue</a>
</h3>

```typescript
currentAverageValue: string;
```


currentAverageValue is the current value of metric averaged over autoscaled pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5855">property currentValue</a>
</h3>

```typescript
currentValue: string;
```


currentValue is the current value of the metric (as a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5860">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of a metric used for autoscaling in metric system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5865">property metricSelector</a>
</h3>

```typescript
metricSelector: LabelSelector;
```


metricSelector is used to identify a specific time series within a given metric.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5874">interface HorizontalPodAutoscaler</a>
</h2>

HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which
automatically manages the replica count of any resource implementing the scale subresource
based on the metrics specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5881">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5889">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5895">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


metadata is the standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5901">property spec</a>
</h3>

```typescript
spec: HorizontalPodAutoscalerSpec;
```


spec is the specification for the behaviour of the autoscaler. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5906">property status</a>
</h3>

```typescript
status: HorizontalPodAutoscalerStatus;
```


status is the current information about the autoscaler.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5914">interface HorizontalPodAutoscalerCondition</a>
</h2>

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a
certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5918">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


lastTransitionTime is the last time the condition transitioned from one status to another

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5923">property message</a>
</h3>

```typescript
message: string;
```


message is a human-readable explanation containing details about the transition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5928">property reason</a>
</h3>

```typescript
reason: string;
```


reason is the reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5933">property status</a>
</h3>

```typescript
status: string;
```


status is the status of the condition (True, False, Unknown)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5938">property type</a>
</h3>

```typescript
type: string;
```


type describes the current condition

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5945">interface HorizontalPodAutoscalerList</a>
</h2>

HorizontalPodAutoscaler is a list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5952">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5957">property items</a>
</h3>

```typescript
items: HorizontalPodAutoscaler[];
```


items is the list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5965">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5970">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


metadata is the standard list metadata.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5978">interface HorizontalPodAutoscalerSpec</a>
</h2>

HorizontalPodAutoscalerSpec describes the desired functionality of the
HorizontalPodAutoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5983">property maxReplicas</a>
</h3>

```typescript
maxReplicas: number;
```


maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale
up. It cannot be less that minReplicas.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5993">property metrics</a>
</h3>

```typescript
metrics: MetricSpec[];
```


metrics contains the specifications for which to use to calculate the desired replica count
(the maximum replica count across all metrics will be used).  The desired replica count is
calculated multiplying the ratio between the target value and the current value by the
current number of pods.  Ergo, metrics used must decrease as the pod count is increased,
and vice-versa.  See the individual metric source types for more information about how each
type of metric must respond.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5999">property minReplicas</a>
</h3>

```typescript
minReplicas: number;
```


minReplicas is the lower limit for the number of replicas to which the autoscaler can scale
down. It defaults to 1 pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6005">property scaleTargetRef</a>
</h3>

```typescript
scaleTargetRef: CrossVersionObjectReference;
```


scaleTargetRef points to the target resource to scale, and is used to the pods for which
metrics should be collected, as well as to actually change the replica count.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6012">interface HorizontalPodAutoscalerStatus</a>
</h2>

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6017">property conditions</a>
</h3>

```typescript
conditions: HorizontalPodAutoscalerCondition[];
```


conditions is the set of conditions required for this autoscaler to scale its target, and
indicates whether or not those conditions are met.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6022">property currentMetrics</a>
</h3>

```typescript
currentMetrics: MetricStatus[];
```


currentMetrics is the last read state of the metrics used by this autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6028">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


currentReplicas is current number of replicas of pods managed by this autoscaler, as last
seen by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6034">property desiredReplicas</a>
</h3>

```typescript
desiredReplicas: number;
```


desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as
last calculated by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6040">property lastScaleTime</a>
</h3>

```typescript
lastScaleTime: string;
```


lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used
by the autoscaler to control how often the number of pods is changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6045">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


observedGeneration is the most recent generation observed by this autoscaler.

<h2 class="pdoc-module-header" id="MetricSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6053">interface MetricSpec</a>
</h2>

MetricSpec specifies how to scale based on a single metric (only `type` and one other
matching field should be set at once).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6060">property external</a>
</h3>

```typescript
external: ExternalMetricSource;
```


external refers to a global metric that is not associated with any Kubernetes object. It
allows autoscaling based on information coming from components running outside of cluster
(for example length of queue in cloud messaging service, or QPS from loadbalancer running
outside of cluster).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6066">property object</a>
</h3>

```typescript
object: ObjectMetricSource;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6073">property pods</a>
</h3>

```typescript
pods: PodsMetricSource;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6081">property resource</a>
</h3>

```typescript
resource: ResourceMetricSource;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6087">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It should be one of "Object", "Pods" or "Resource",
each mapping to a matching field in the object.

<h2 class="pdoc-module-header" id="MetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6094">interface MetricStatus</a>
</h2>

MetricStatus describes the last-read state of a single metric.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6101">property external</a>
</h3>

```typescript
external: ExternalMetricStatus;
```


external refers to a global metric that is not associated with any Kubernetes object. It
allows autoscaling based on information coming from components running outside of cluster
(for example length of queue in cloud messaging service, or QPS from loadbalancer running
outside of cluster).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6107">property object</a>
</h3>

```typescript
object: ObjectMetricStatus;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6114">property pods</a>
</h3>

```typescript
pods: PodsMetricStatus;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6122">property resource</a>
</h3>

```typescript
resource: ResourceMetricStatus;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6128">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each
corresponds to a matching field in the object.

<h2 class="pdoc-module-header" id="ObjectMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6136">interface ObjectMetricSource</a>
</h2>

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for
example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6141">property averageValue</a>
</h3>

```typescript
averageValue: string;
```


averageValue is the target value of the average of the metric across all relevant pods (as
a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6146">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6153">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is the string-encoded form of a standard kubernetes label selector for the given
metric When set, it is passed as an additional parameter to the metrics server for more
specific metrics scoping When unset, just the metricName will be used to gather metrics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6158">property target</a>
</h3>

```typescript
target: CrossVersionObjectReference;
```


target is the described Kubernetes object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6163">property targetValue</a>
</h3>

```typescript
targetValue: string;
```


targetValue is the target value of the metric (as a quantity).

<h2 class="pdoc-module-header" id="ObjectMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6171">interface ObjectMetricStatus</a>
</h2>

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object
(for example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6176">property averageValue</a>
</h3>

```typescript
averageValue: string;
```


averageValue is the current value of the average of the metric across all relevant pods (as
a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6181">property currentValue</a>
</h3>

```typescript
currentValue: string;
```


currentValue is the current value of the metric (as a quantity).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6186">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6194">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is the string-encoded form of a standard kubernetes label selector for the given
metric When set in the ObjectMetricSource, it is passed as an additional parameter to the
metrics server for more specific metrics scoping. When unset, just the metricName will be
used to gather metrics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6199">property target</a>
</h3>

```typescript
target: CrossVersionObjectReference;
```


target is the described Kubernetes object.

<h2 class="pdoc-module-header" id="PodsMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6208">interface PodsMetricSource</a>
</h2>

PodsMetricSource indicates how to scale on a metric describing each pod in the current scale
target (for example, transactions-processed-per-second). The values will be averaged together
before being compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6212">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6219">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is the string-encoded form of a standard kubernetes label selector for the given
metric When set, it is passed as an additional parameter to the metrics server for more
specific metrics scoping When unset, just the metricName will be used to gather metrics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6225">property targetAverageValue</a>
</h3>

```typescript
targetAverageValue: string;
```


targetAverageValue is the target value of the average of the metric across all relevant
pods (as a quantity)

<h2 class="pdoc-module-header" id="PodsMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6233">interface PodsMetricStatus</a>
</h2>

PodsMetricStatus indicates the current value of a metric describing each pod in the current
scale target (for example, transactions-processed-per-second).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6238">property currentAverageValue</a>
</h3>

```typescript
currentAverageValue: string;
```


currentAverageValue is the current value of the average of the metric across all relevant
pods (as a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6243">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6251">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is the string-encoded form of a standard kubernetes label selector for the given
metric When set in the PodsMetricSource, it is passed as an additional parameter to the
metrics server for more specific metrics scoping. When unset, just the metricName will be
used to gather metrics.

<h2 class="pdoc-module-header" id="ResourceMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6263">interface ResourceMetricSource</a>
</h2>

ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  The values will be averaged together before being compared to the target.  Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.  Only one "target" type should
be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6267">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the resource in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6274">property targetAverageUtilization</a>
</h3>

```typescript
targetAverageUtilization: number;
```


targetAverageUtilization is the target value of the average of the resource metric across
all relevant pods, represented as a percentage of the requested value of the resource for
the pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6281">property targetAverageValue</a>
</h3>

```typescript
targetAverageValue: string;
```


targetAverageValue is the target value of the average of the resource metric across all
relevant pods, as a raw value (instead of as a percentage of the request), similar to the
"pods" metric source type.

<h2 class="pdoc-module-header" id="ResourceMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6291">interface ResourceMetricStatus</a>
</h2>

ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top
of those available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6298">property currentAverageUtilization</a>
</h3>

```typescript
currentAverageUtilization: number;
```


currentAverageUtilization is the current value of the average of the resource metric across
all relevant pods, represented as a percentage of the requested value of the resource for
the pods.  It will only be present if `targetAverageValue` was set in the corresponding
metric specification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6306">property currentAverageValue</a>
</h3>

```typescript
currentAverageValue: string;
```


currentAverageValue is the current value of the average of the resource metric across all
relevant pods, as a raw value (instead of as a percentage of the request), similar to the
"pods" metric source type. It will always be set, regardless of the corresponding metric
specification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6311">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the resource in question.

