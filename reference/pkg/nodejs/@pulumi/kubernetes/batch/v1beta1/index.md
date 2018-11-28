---
title: Module batch/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">batch</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCronJob">function isCronJob</a>
* <a href="#isCronJobList">function isCronJobList</a>
* <a href="#CronJob">interface CronJob</a>
* <a href="#CronJobList">interface CronJobList</a>
* <a href="#CronJobSpec">interface CronJobSpec</a>
* <a href="#CronJobStatus">interface CronJobStatus</a>
* <a href="#JobTemplateSpec">interface JobTemplateSpec</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCronJob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6126">function isCronJob</a>
</h2>

```typescript
isCronJob(o: any): boolean
```

<h2 class="pdoc-module-header" id="isCronJobList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L6163">function isCronJobList</a>
</h2>

```typescript
isCronJobList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CronJob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5741">interface CronJob</a>
</h2>

CronJob represents the configuration of a single cron job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5748">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5756">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5762">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5768">property spec</a>
</h3>

```typescript
spec: CronJobSpec;
```


Specification of the desired behavior of a cron job, including the schedule. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5774">property status</a>
</h3>

```typescript
status: CronJobStatus;
```


Current status of a cron job. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="CronJobList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5781">interface CronJobList</a>
</h2>

CronJobList is a collection of cron jobs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5788">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5793">property items</a>
</h3>

```typescript
items: CronJob[];
```


items is the list of CronJobs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5801">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5807">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="CronJobSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5814">interface CronJobSpec</a>
</h2>

CronJobSpec describes how the job execution will look like and when it will actually run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5821">property concurrencyPolicy</a>
</h3>

```typescript
concurrencyPolicy: string;
```


Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow"
(default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs,
skipping next run if previous run hasn't finished yet; - "Replace": cancels currently
running job and replaces it with a new one

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5827">property failedJobsHistoryLimit</a>
</h3>

```typescript
failedJobsHistoryLimit: number;
```


The number of failed finished jobs to retain. This is a pointer to distinguish between
explicit zero and not specified. Defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5832">property jobTemplate</a>
</h3>

```typescript
jobTemplate: JobTemplateSpec;
```


Specifies the job that will be created when executing a CronJob.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5837">property schedule</a>
</h3>

```typescript
schedule: string;
```


The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5843">property startingDeadlineSeconds</a>
</h3>

```typescript
startingDeadlineSeconds: number;
```


Optional deadline in seconds for starting the job if it misses scheduled time for any
reason.  Missed jobs executions will be counted as failed ones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5849">property successfulJobsHistoryLimit</a>
</h3>

```typescript
successfulJobsHistoryLimit: number;
```


The number of successful finished jobs to retain. This is a pointer to distinguish between
explicit zero and not specified. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5855">property suspend</a>
</h3>

```typescript
suspend: boolean;
```


This flag tells the controller to suspend subsequent executions, it does not apply to
already started executions.  Defaults to false.

<h2 class="pdoc-module-header" id="CronJobStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5862">interface CronJobStatus</a>
</h2>

CronJobStatus represents the current state of a cron job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5866">property active</a>
</h3>

```typescript
active: ObjectReference[];
```


A list of pointers to currently running jobs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5871">property lastScheduleTime</a>
</h3>

```typescript
lastScheduleTime: string;
```


Information when was the last time the job was successfully scheduled.

<h2 class="pdoc-module-header" id="JobTemplateSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5878">interface JobTemplateSpec</a>
</h2>

JobTemplateSpec describes the data a Job should have when created from a template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5883">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata of the jobs created from this template. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5889">property spec</a>
</h3>

```typescript
spec: JobSpec;
```


Specification of the desired behavior of the job. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

