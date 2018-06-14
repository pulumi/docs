---
title: Module settings/v1alpha1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">settings</a> &gt; v1alpha1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#PodPreset">interface PodPreset</a>
* <a href="#PodPresetList">interface PodPresetList</a>
* <a href="#PodPresetSpec">interface PodPresetSpec</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="PodPreset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16190">interface PodPreset</a>
</h2>

PodPreset is a policy resource that defines additional runtime requirements for a Pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16197">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16205">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16208">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16211">property spec</a>
</h3>

```typescript
spec: PodPresetSpec;
```

<h2 class="pdoc-module-header" id="PodPresetList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16218">interface PodPresetList</a>
</h2>

PodPresetList is a list of PodPreset objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16225">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16230">property items</a>
</h3>

```typescript
items: PodPreset[];
```


Items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16238">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16244">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="PodPresetSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16251">interface PodPresetSpec</a>
</h2>

PodPresetSpec is a description of a pod preset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16255">property env</a>
</h3>

```typescript
env: EnvVar[];
```


Env defines the collection of EnvVar to inject into containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16260">property envFrom</a>
</h3>

```typescript
envFrom: EnvFromSource[];
```


EnvFrom defines the collection of EnvFromSource to inject into containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16265">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


Selector is a label query over a set of resources, in this case pods. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16270">property volumeMounts</a>
</h3>

```typescript
volumeMounts: VolumeMount[];
```


VolumeMounts defines the collection of VolumeMount to inject into containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16275">property volumes</a>
</h3>

```typescript
volumes: Volume[];
```


Volumes defines the collection of Volume to inject into the pod.

