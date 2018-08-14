---
title: Module autoscaling/v2beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">autoscaling</a> &gt; v2beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCrossVersionObjectReference">function isCrossVersionObjectReference</a>
* <a href="#isHorizontalPodAutoscaler">function isHorizontalPodAutoscaler</a>
* <a href="#isHorizontalPodAutoscalerList">function isHorizontalPodAutoscalerList</a>
* <a href="#CrossVersionObjectReference">interface CrossVersionObjectReference</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5447">function isCrossVersionObjectReference</a>
</h2>

```typescript
isCrossVersionObjectReference(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5492">function isHorizontalPodAutoscaler</a>
</h2>

```typescript
isHorizontalPodAutoscaler(o: any): boolean
```

<h2 class="pdoc-module-header" id="isHorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5561">function isHorizontalPodAutoscalerList</a>
</h2>

```typescript
isHorizontalPodAutoscalerList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CrossVersionObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5114">interface CrossVersionObjectReference</a>
</h2>

CrossVersionObjectReference contains enough information to let you identify the referred
resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5118">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5124">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5129">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names

<h2 class="pdoc-module-header" id="HorizontalPodAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5138">interface HorizontalPodAutoscaler</a>
</h2>

HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which
automatically manages the replica count of any resource implementing the scale subresource
based on the metrics specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5145">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5153">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5159">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


metadata is the standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5165">property spec</a>
</h3>

```typescript
spec: HorizontalPodAutoscalerSpec;
```


spec is the specification for the behaviour of the autoscaler. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5170">property status</a>
</h3>

```typescript
status: HorizontalPodAutoscalerStatus;
```


status is the current information about the autoscaler.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5178">interface HorizontalPodAutoscalerCondition</a>
</h2>

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a
certain point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5182">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


lastTransitionTime is the last time the condition transitioned from one status to another

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5187">property message</a>
</h3>

```typescript
message: string;
```


message is a human-readable explanation containing details about the transition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5192">property reason</a>
</h3>

```typescript
reason: string;
```


reason is the reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5197">property status</a>
</h3>

```typescript
status: string;
```


status is the status of the condition (True, False, Unknown)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5202">property type</a>
</h3>

```typescript
type: string;
```


type describes the current condition

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5209">interface HorizontalPodAutoscalerList</a>
</h2>

HorizontalPodAutoscaler is a list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5216">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5221">property items</a>
</h3>

```typescript
items: HorizontalPodAutoscaler[];
```


items is the list of horizontal pod autoscaler objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5229">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5234">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


metadata is the standard list metadata.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5242">interface HorizontalPodAutoscalerSpec</a>
</h2>

HorizontalPodAutoscalerSpec describes the desired functionality of the
HorizontalPodAutoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5247">property maxReplicas</a>
</h3>

```typescript
maxReplicas: number;
```


maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale
up. It cannot be less that minReplicas.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5257">property metrics</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5263">property minReplicas</a>
</h3>

```typescript
minReplicas: number;
```


minReplicas is the lower limit for the number of replicas to which the autoscaler can scale
down. It defaults to 1 pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5269">property scaleTargetRef</a>
</h3>

```typescript
scaleTargetRef: CrossVersionObjectReference;
```


scaleTargetRef points to the target resource to scale, and is used to the pods for which
metrics should be collected, as well as to actually change the replica count.

<h2 class="pdoc-module-header" id="HorizontalPodAutoscalerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5276">interface HorizontalPodAutoscalerStatus</a>
</h2>

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5281">property conditions</a>
</h3>

```typescript
conditions: HorizontalPodAutoscalerCondition[];
```


conditions is the set of conditions required for this autoscaler to scale its target, and
indicates whether or not those conditions are met.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5286">property currentMetrics</a>
</h3>

```typescript
currentMetrics: MetricStatus[];
```


currentMetrics is the last read state of the metrics used by this autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5292">property currentReplicas</a>
</h3>

```typescript
currentReplicas: number;
```


currentReplicas is current number of replicas of pods managed by this autoscaler, as last
seen by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5298">property desiredReplicas</a>
</h3>

```typescript
desiredReplicas: number;
```


desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as
last calculated by the autoscaler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5304">property lastScaleTime</a>
</h3>

```typescript
lastScaleTime: string;
```


lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used
by the autoscaler to control how often the number of pods is changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5309">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


observedGeneration is the most recent generation observed by this autoscaler.

<h2 class="pdoc-module-header" id="MetricSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5317">interface MetricSpec</a>
</h2>

MetricSpec specifies how to scale based on a single metric (only `type` and one other
matching field should be set at once).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5322">property object</a>
</h3>

```typescript
object: ObjectMetricSource;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5329">property pods</a>
</h3>

```typescript
pods: PodsMetricSource;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5337">property resource</a>
</h3>

```typescript
resource: ResourceMetricSource;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5342">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It should match one of the fields below.

<h2 class="pdoc-module-header" id="MetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5349">interface MetricStatus</a>
</h2>

MetricStatus describes the last-read state of a single metric.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5354">property object</a>
</h3>

```typescript
object: ObjectMetricStatus;
```


object refers to a metric describing a single kubernetes object (for example,
hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5361">property pods</a>
</h3>

```typescript
pods: PodsMetricStatus;
```


pods refers to a metric describing each pod in the current scale target (for example,
transactions-processed-per-second).  The values will be averaged together before being
compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5369">property resource</a>
</h3>

```typescript
resource: ResourceMetricStatus;
```


resource refers to a resource metric (such as those specified in requests and limits) known
to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5374">property type</a>
</h3>

```typescript
type: string;
```


type is the type of metric source.  It will match one of the fields below.

<h2 class="pdoc-module-header" id="ObjectMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5382">interface ObjectMetricSource</a>
</h2>

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for
example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5386">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5391">property target</a>
</h3>

```typescript
target: CrossVersionObjectReference;
```


target is the described Kubernetes object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5396">property targetValue</a>
</h3>

```typescript
targetValue: string;
```


targetValue is the target value of the metric (as a quantity).

<h2 class="pdoc-module-header" id="ObjectMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5404">interface ObjectMetricStatus</a>
</h2>

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object
(for example, hits-per-second on an Ingress object).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5408">property currentValue</a>
</h3>

```typescript
currentValue: string;
```


currentValue is the current value of the metric (as a quantity).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5413">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5418">property target</a>
</h3>

```typescript
target: CrossVersionObjectReference;
```


target is the described Kubernetes object.

<h2 class="pdoc-module-header" id="PodsMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5427">interface PodsMetricSource</a>
</h2>

PodsMetricSource indicates how to scale on a metric describing each pod in the current scale
target (for example, transactions-processed-per-second). The values will be averaged together
before being compared to the target value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5431">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5437">property targetAverageValue</a>
</h3>

```typescript
targetAverageValue: string;
```


targetAverageValue is the target value of the average of the metric across all relevant
pods (as a quantity)

<h2 class="pdoc-module-header" id="PodsMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5445">interface PodsMetricStatus</a>
</h2>

PodsMetricStatus indicates the current value of a metric describing each pod in the current
scale target (for example, transactions-processed-per-second).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5450">property currentAverageValue</a>
</h3>

```typescript
currentAverageValue: string;
```


currentAverageValue is the current value of the average of the metric across all relevant
pods (as a quantity)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5455">property metricName</a>
</h3>

```typescript
metricName: string;
```


metricName is the name of the metric in question

<h2 class="pdoc-module-header" id="ResourceMetricSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5467">interface ResourceMetricSource</a>
</h2>

ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  The values will be averaged together before being compared to the target.  Such
metrics are built in to Kubernetes, and have special scaling options on top of those
available to normal per-pod metrics using the "pods" source.  Only one "target" type should
be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5471">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the resource in question.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5478">property targetAverageUtilization</a>
</h3>

```typescript
targetAverageUtilization: number;
```


targetAverageUtilization is the target value of the average of the resource metric across
all relevant pods, represented as a percentage of the requested value of the resource for
the pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5485">property targetAverageValue</a>
</h3>

```typescript
targetAverageValue: string;
```


targetAverageValue is the target value of the average of the resource metric across all
relevant pods, as a raw value (instead of as a percentage of the request), similar to the
"pods" metric source type.

<h2 class="pdoc-module-header" id="ResourceMetricStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5495">interface ResourceMetricStatus</a>
</h2>

ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as
specified in requests and limits, describing each pod in the current scale target (e.g. CPU
or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top
of those available to normal per-pod metrics using the "pods" source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5502">property currentAverageUtilization</a>
</h3>

```typescript
currentAverageUtilization: number;
```


currentAverageUtilization is the current value of the average of the resource metric across
all relevant pods, represented as a percentage of the requested value of the resource for
the pods.  It will only be present if `targetAverageValue` was set in the corresponding
metric specification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5510">property currentAverageValue</a>
</h3>

```typescript
currentAverageValue: string;
```


currentAverageValue is the current value of the average of the resource metric across all
relevant pods, as a raw value (instead of as a percentage of the request), similar to the
"pods" metric source type. It will always be set, regardless of the corresponding metric
specification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5515">property name</a>
</h3>

```typescript
name: string;
```


name is the name of the resource in question.

