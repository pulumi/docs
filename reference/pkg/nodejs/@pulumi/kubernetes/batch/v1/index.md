---
title: Module batch/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">batch</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isJob">function isJob</a>
* <a href="#isJobList">function isJobList</a>
* <a href="#Job">interface Job</a>
* <a href="#JobCondition">interface JobCondition</a>
* <a href="#JobList">interface JobList</a>
* <a href="#JobSpec">interface JobSpec</a>
* <a href="#JobStatus">interface JobStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isJob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5902">function isJob</a>
</h2>

```typescript
isJob(o: any): boolean
```

<h2 class="pdoc-module-header" id="isJobList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5976">function isJobList</a>
</h2>

```typescript
isJobList(o: any): boolean
```

<h2 class="pdoc-module-header" id="Job">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5528">interface Job</a>
</h2>

Job represents the configuration of a single job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5535">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5543">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5549">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5555">property spec</a>
</h3>

```typescript
spec: JobSpec;
```


Specification of the desired behavior of a job. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5561">property status</a>
</h3>

```typescript
status: JobStatus;
```


Current status of a job. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="JobCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5568">interface JobCondition</a>
</h2>

JobCondition describes current state of a job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5572">property lastProbeTime</a>
</h3>

```typescript
lastProbeTime: string;
```


Last time the condition was checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5577">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transit from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5582">property message</a>
</h3>

```typescript
message: string;
```


Human readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5587">property reason</a>
</h3>

```typescript
reason: string;
```


(brief) reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5592">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5597">property type</a>
</h3>

```typescript
type: string;
```


Type of job condition, Complete or Failed.

<h2 class="pdoc-module-header" id="JobList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5604">interface JobList</a>
</h2>

JobList is a collection of jobs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5611">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5616">property items</a>
</h3>

```typescript
items: Job[];
```


items is the list of Jobs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5624">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5630">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="JobSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5637">interface JobSpec</a>
</h2>

JobSpec describes how the job execution will look like.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5642">property activeDeadlineSeconds</a>
</h3>

```typescript
activeDeadlineSeconds: number;
```


Specifies the duration in seconds relative to the startTime that the job may be active
before the system tries to terminate it; value must be positive integer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5647">property backoffLimit</a>
</h3>

```typescript
backoffLimit: number;
```


Specifies the number of retries before marking this job failed. Defaults to 6

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5656">property completions</a>
</h3>

```typescript
completions: number;
```


Specifies the desired number of successfully finished pods the job should be run with.
Setting to nil means that the success of any pod signals the success of all pods, and
allows parallelism to have any positive value.  Setting to 1 means that parallelism is
limited to 1 and the success of that pod signals the success of the job. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5668">property manualSelector</a>
</h3>

```typescript
manualSelector: boolean;
```


manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector`
unset unless you are certain what you are doing. When false or unset, the system pick
labels unique to this job and appends those labels to the pod template.  When true, the
user is responsible for picking unique labels and specifying the selector.  Failure to pick
a unique label may cause this and other jobs to not function correctly.  However, You may
see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API.
More info:
https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5677">property parallelism</a>
</h3>

```typescript
parallelism: number;
```


Specifies the maximum desired number of pods the job should run at any given time. The
actual number of pods running in steady state will be less than this number when
((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to
do is less than max parallelism. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5684">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


A label query over pods that should match the pod count. Normally, the system sets this
field for you. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5690">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Describes the pod that will be created when executing a job. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/

<h2 class="pdoc-module-header" id="JobStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5697">interface JobStatus</a>
</h2>

JobStatus represents the current state of a Job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5701">property active</a>
</h3>

```typescript
active: number;
```


The number of actively running pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5708">property completionTime</a>
</h3>

```typescript
completionTime: string;
```


Represents time when the job was completed. It is not guaranteed to be set in
happens-before order across separate operations. It is represented in RFC3339 form and is
in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5714">property conditions</a>
</h3>

```typescript
conditions: JobCondition[];
```


The latest available observations of an object's current state. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5719">property failed</a>
</h3>

```typescript
failed: number;
```


The number of pods which reached phase Failed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5726">property startTime</a>
</h3>

```typescript
startTime: string;
```


Represents time when the job was acknowledged by the job controller. It is not guaranteed
to be set in happens-before order across separate operations. It is represented in RFC3339
form and is in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5731">property succeeded</a>
</h3>

```typescript
succeeded: number;
```


The number of pods which reached phase Succeeded.

