---
title: Module storage/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">storage</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isStorageClass">function isStorageClass</a>
* <a href="#isStorageClassList">function isStorageClassList</a>
* <a href="#StorageClass">interface StorageClass</a>
* <a href="#StorageClassList">interface StorageClassList</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isStorageClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19446">function isStorageClass</a>
</h2>

```typescript
isStorageClass(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19483">function isStorageClassList</a>
</h2>

```typescript
isStorageClassList(o: any): boolean
```

<h2 class="pdoc-module-header" id="StorageClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18336">interface StorageClass</a>
</h2>

StorageClass describes the parameters for a class of storage for which PersistentVolumes can
be dynamically provisioned.

StorageClasses are non-namespaced; the name of the storage class according to etcd is in
ObjectMeta.Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18340">property allowVolumeExpansion</a>
</h3>

```typescript
allowVolumeExpansion: boolean;
```


AllowVolumeExpansion shows whether the storage class allow volume expand

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18348">property allowedTopologies</a>
</h3>

```typescript
allowedTopologies: TopologySelectorTerm[];
```


Restrict the node topologies where volumes can be dynamically provisioned. Each volume
plugin defines its own supported topology specifications. An empty TopologySelectorTerm
list means there is no topology restriction. This field is only honored by servers that
enable the VolumeScheduling feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18356">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18364">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18370">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18377">property mountOptions</a>
</h3>

```typescript
mountOptions: string[];
```


Dynamically provisioned PersistentVolumes of this storage class are created with these
mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one
is invalid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18383">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


Parameters holds the parameters for the provisioner that should create volumes of this
storage class.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18388">property provisioner</a>
</h3>

```typescript
provisioner: string;
```


Provisioner indicates the type of the provisioner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18394">property reclaimPolicy</a>
</h3>

```typescript
reclaimPolicy: string;
```


Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18401">property volumeBindingMode</a>
</h3>

```typescript
volumeBindingMode: string;
```


VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.
When unset, VolumeBindingImmediate is used. This field is only honored by servers that
enable the VolumeScheduling feature.

<h2 class="pdoc-module-header" id="StorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18408">interface StorageClassList</a>
</h2>

StorageClassList is a collection of storage classes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18415">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18420">property items</a>
</h3>

```typescript
items: StorageClass[];
```


Items is the list of StorageClasses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18428">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18434">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

