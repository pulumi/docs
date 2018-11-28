---
title: Module autoscaling/v2beta2
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">autoscaling</a> &gt; v2beta2

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
* <a href="#MetricIdentifier">interface MetricIdentifier</a>
* <a href="#MetricSpec">interface MetricSpec</a>
* <a href="#MetricStatus">interface MetricStatus</a>
* <a href="#MetricTarget">interface MetricTarget</a>
* <a href="#MetricValueStatus">interface MetricValueStatus</a>
* <a href="#ObjectMetricSource">interface ObjectMetricSource</a>
* <a href="#ObjectMetricStatus">interface ObjectMetricStatus</a>
* <a href="#PodsMetricSource">interface PodsMetricSource</a>
* <a href="#PodsMetricStatus">interface PodsMetricStatus</a>
* <a href="#ResourceMetricSource">interface ResourceMetricSource</a>
* <a href="#ResourceMetricStatus">interface ResourceMetricStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6326">function isCrossVersionObjectReference</a>
</h2>

```typescript
isCrossVersionObjectReference(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6408">function isHorizontalPodAutoscaler</a>
</h2>

```typescript
isHorizontalPodAutoscaler(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6477">function isHorizontalPodAutoscalerList</a>
</h2>

```typescript
isHorizontalPodAutoscalerList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5956">interface CrossVersionObjectReference</a>
</h2>

CrossVersionObjectReference contains enough information to let you identify the referred
resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5960">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5966">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5971">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names

<h2 class="pdoc-module-header" id="ExternalMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5980">interface ExternalMetricSource</a>
</h2>

ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes
object (for example length of queue in cloud messaging service, or QPS from loadbalancer
running outside of cluster).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5984">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5989">property target</a>
</h3>

```typescript
target: MetricTarget;
```


target specifies the target value for the given metric

<h2 class="pdoc-module-header" id="ExternalMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5997">interface ExternalMetricStatus</a>
</h2>

ExternalMetricStatus indicates the current value of a global metric not associated with any
Kubernetes object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6001">property current</a>
</h3>

```typescript
current: MetricValueStatus;
```


current contains the current value for the given metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6006">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h2 class="pdoc-module-header" id="HorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6015">interface HorizontalPodAutoscaler</a>
</h2>

HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which
automatically manages the replica count of any resource implementing the scale subresource
based on the metrics specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6022">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6030">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6036">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


metadata is the standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6042">property spec</a>
</h3>

```typescript
spec: HorizontalPodAutoscalerSpec;
```


spec is the specification for the behaviour of the autoscaler. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6047">property status</a>
</h3>

```typescript
status: HorizontalPodAutoscalerStatus;
```


status is the current information about the autoscaler.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6055">interface HorizontalPodAutoscalerCondition</a>
</h2>

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a
certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6059">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


lastTransitionTime is the last time the condition transitioned from one status to another

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6064">property message</a>
</h3>

```typescript
message: string;
```


message is a human-readable explanation containing details about the transition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6069">property reason</a>
</h3>

```typescript
reason: string;
```


reason is the reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6074">property status</a>
</h3>

```typescript
status: string;
```


status is the status of the condition (True, False, Unknown)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6079">property type</a>
</h3>

```typescript
type: string;
```


type describes the current condition

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6086">interface HorizontalPodAutoscalerList</a>
</h2>

HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6093">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6098">property items</a>
</h3>

```typescript
items: HorizontalPodAutoscaler[];
```


items is the list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6106">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6111">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


metadata is the standard list metadata.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6119">interface HorizontalPodAutoscalerSpec</a>
</h2>

HorizontalPodAutoscalerSpec describes the desired functionality of the
HorizontalPodAutoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6124">property maxReplicas</a>
</h3>

```typescript
maxReplicas: number;
```


maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale
up. It cannot be less that minReplicas.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6135">property metrics</a>
</h3>

```typescript
metrics: MetricSpec[];
```


metrics contains the specifications for which to use to calculate the desired replica count
(the maximum replica count across all metrics will be used).  The desired replica count is
calculated multiplying the ratio between the target value and the current value by the
current number of pods.  Ergo, metrics used must decrease as the pod count is increased,
and vice-versa.  See the individual metric source types for more information about how each
type of metric must respond. If not set, the default metric will be set to 80% average CPU
utilization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6141">property minReplicas</a>
</h3>

```typescript
minReplicas: number;
```


minReplicas is the lower limit for the number of replicas to which the autoscaler can scale
down. It defaults to 1 pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6147">property scaleTargetRef</a>
</h3>

```typescript
scaleTargetRef: CrossVersionObjectReference;
```


scaleTargetRef points to the target resource to scale, and is used to the pods for which
metrics should be collected, as well as to actually change the replica count.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6154">interface HorizontalPodAutoscalerStatus</a>
</h2>

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6159">property conditions</a>
</h3>

```typescript
conditions: HorizontalPodAutoscalerCondition[];
```


conditions is the set of conditions required for this autoscaler to scale its target, and
indicates whether or not those conditions are met.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6164">property currentMetrics</a>
</h3>

```typescript
currentMetrics: MetricStatus[];
```


currentMetrics is the last read state of the metrics used by this autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6170">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


currentReplicas is current number of replicas of pods managed by this autoscaler, as last
seen by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6176">property desiredReplicas</a>
</h3>

```typescript
desiredReplicas: number;
```


desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as
last calculated by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6182">property lastScaleTime</a>
</h3>

```typescript
lastScaleTime: string;
```


lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used
by the autoscaler to control how often the number of pods is changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6187">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


observedGeneration is the most recent generation observed by this autoscaler.

<h2 class="pdoc-module-header" id="MetricIdentifier">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6194">interface MetricIdentifier</a>
</h2>

MetricIdentifier defines the name and optionally selector for a metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6198">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the given metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6205">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


selector is the string-encoded form of a standard kubernetes label selector for the given
metric When set, it is passed as an additional parameter to the metrics server for more
specific metrics scoping. When unset, just the metricName will be used to gather metrics.

<h2 class="pdoc-module-header" id="MetricSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6213">interface MetricSpec</a>
</h2>

MetricSpec specifies how to scale based on a single metric (only `type` and one other
matching field should be set at once).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6220">property external</a>
</h3>

```typescript
external: ExternalMetricSource;
```


external refers to a global metric that is not associated with any Kubernetes object. It
allows autoscaling based on information coming from components running outside of cluster
(for example length of queue in cloud messaging service, or QPS from loadbalancer running
outside of cluster).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6226">property object</a>
</h3>

```typescript
object: ObjectMetricSource;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6233">property pods</a>
</h3>

```typescript
pods: PodsMetricSource;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6241">property resource</a>
</h3>

```typescript
resource: ResourceMetricSource;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6247">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It should be one of "Object", "Pods" or "Resource",
each mapping to a matching field in the object.

<h2 class="pdoc-module-header" id="MetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6254">interface MetricStatus</a>
</h2>

MetricStatus describes the last-read state of a single metric.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6261">property external</a>
</h3>

```typescript
external: ExternalMetricStatus;
```


external refers to a global metric that is not associated with any Kubernetes object. It
allows autoscaling based on information coming from components running outside of cluster
(for example length of queue in cloud messaging service, or QPS from loadbalancer running
outside of cluster).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6267">property object</a>
</h3>

```typescript
object: ObjectMetricStatus;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6274">property pods</a>
</h3>

```typescript
pods: PodsMetricStatus;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6282">property resource</a>
</h3>

```typescript
resource: ResourceMetricStatus;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6288">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each
corresponds to a matching field in the object.

<h2 class="pdoc-module-header" id="MetricTarget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6296">interface MetricTarget</a>
</h2>

MetricTarget defines the target value, average value, or average utilization of a specific
metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6302">property averageUtilization</a>
</h3>

```typescript
averageUtilization: number;
```


averageUtilization is the target value of the average of the resource metric across all
relevant pods, represented as a percentage of the requested value of the resource for the
pods. Currently only valid for Resource metric source type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6308">property averageValue</a>
</h3>

```typescript
averageValue: string;
```


averageValue is the target value of the average of the metric across all relevant pods (as
a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6313">property type</a>
</h3>

```typescript
type: string;
```


type represents whether the metric type is Utilization, Value, or AverageValue

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6318">property value</a>
</h3>

```typescript
value: string;
```


value is the target value of the metric (as a quantity).

<h2 class="pdoc-module-header" id="MetricValueStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6325">interface MetricValueStatus</a>
</h2>

MetricValueStatus holds the current value for a metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6331">property averageUtilization</a>
</h3>

```typescript
averageUtilization: number;
```


currentAverageUtilization is the current value of the average of the resource metric across
all relevant pods, represented as a percentage of the requested value of the resource for
the pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6337">property averageValue</a>
</h3>

```typescript
averageValue: string;
```


averageValue is the current value of the average of the metric across all relevant pods (as
a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6342">property value</a>
</h3>

```typescript
value: string;
```


value is the current value of the metric (as a quantity).

<h2 class="pdoc-module-header" id="ObjectMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6350">interface ObjectMetricSource</a>
</h2>

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for
example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6352">property describedObject</a>
</h3>

```typescript
describedObject: CrossVersionObjectReference;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6357">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6362">property target</a>
</h3>

```typescript
target: MetricTarget;
```


target specifies the target value for the given metric

<h2 class="pdoc-module-header" id="ObjectMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6370">interface ObjectMetricStatus</a>
</h2>

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object
(for example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6374">property current</a>
</h3>

```typescript
current: MetricValueStatus;
```


current contains the current value for the given metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6377">property describedObject</a>
</h3>

```typescript
describedObject: CrossVersionObjectReference;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6382">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h2 class="pdoc-module-header" id="PodsMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6391">interface PodsMetricSource</a>
</h2>

PodsMetricSource indicates how to scale on a metric describing each pod in the current scale
target (for example, transactions-processed-per-second). The values will be averaged together
before being compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6395">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6400">property target</a>
</h3>

```typescript
target: MetricTarget;
```


target specifies the target value for the given metric

<h2 class="pdoc-module-header" id="PodsMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6408">interface PodsMetricStatus</a>
</h2>

PodsMetricStatus indicates the current value of a metric describing each pod in the current
scale target (for example, transactions-processed-per-second).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6412">property current</a>
</h3>

```typescript
current: MetricValueStatus;
```


current contains the current value for the given metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6417">property metric</a>
</h3>

```typescript
metric: MetricIdentifier;
```


metric identifies the target metric by name and selector

<h2 class="pdoc-module-header" id="ResourceMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6429">interface ResourceMetricSource</a>
</h2>

ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  The values will be averaged together before being compared to the target.  Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.  Only one "target" type should
be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6433">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the resource in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6438">property target</a>
</h3>

```typescript
target: MetricTarget;
```


target specifies the target value for the given metric

<h2 class="pdoc-module-header" id="ResourceMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6448">interface ResourceMetricStatus</a>
</h2>

ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top
of those available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6452">property current</a>
</h3>

```typescript
current: MetricValueStatus;
```


current contains the current value for the given metric

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L6457">property name</a>
</h3>

```typescript
name: string;
```


Name is the name of the resource in question.

