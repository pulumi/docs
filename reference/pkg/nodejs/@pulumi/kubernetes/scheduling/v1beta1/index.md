---
title: Module scheduling/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">scheduling</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isPriorityClass">function isPriorityClass</a>
* <a href="#isPriorityClassList">function isPriorityClassList</a>
* <a href="#PriorityClass">interface PriorityClass</a>
* <a href="#PriorityClassList">interface PriorityClassList</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isPriorityClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19692">function isPriorityClass</a>
</h2>

```typescript
isPriorityClass(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPriorityClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19729">function isPriorityClassList</a>
</h2>

```typescript
isPriorityClassList(o: any): boolean
```

<h2 class="pdoc-module-header" id="PriorityClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18602">interface PriorityClass</a>
</h2>

PriorityClass defines mapping from a priority class name to the priority integer value. The
value can be any valid integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18609">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18615">property description</a>
</h3>

```typescript
description: string;
```


description is an arbitrary string that usually provides guidelines on when this priority
class should be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18624">property globalDefault</a>
</h3>

```typescript
globalDefault: boolean;
```


globalDefault specifies whether this PriorityClass should be considered as the default
priority for pods that do not have any priority class. Only one PriorityClass can be marked
as `globalDefault`. However, if more than one PriorityClasses exists with their
`globalDefault` field set to true, the smallest value of such global default
PriorityClasses will be used as the default priority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18632">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18638">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18644">property value</a>
</h3>

```typescript
value: number;
```


The value of this priority class. This is the actual priority that pods receive when they
have the name of this class in their pod spec.

<h2 class="pdoc-module-header" id="PriorityClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18651">interface PriorityClassList</a>
</h2>

PriorityClassList is a collection of priority classes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18658">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18663">property items</a>
</h3>

```typescript
items: PriorityClass[];
```


items is the list of PriorityClasses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18671">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18677">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

