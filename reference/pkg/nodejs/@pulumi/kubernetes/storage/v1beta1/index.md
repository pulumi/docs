---
title: Module storage/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">storage</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isStorageClass">function isStorageClass</a>
* <a href="#isStorageClassList">function isStorageClassList</a>
* <a href="#isVolumeAttachment">function isVolumeAttachment</a>
* <a href="#isVolumeAttachmentList">function isVolumeAttachmentList</a>
* <a href="#StorageClass">interface StorageClass</a>
* <a href="#StorageClassList">interface StorageClassList</a>
* <a href="#VolumeAttachment">interface VolumeAttachment</a>
* <a href="#VolumeAttachmentList">interface VolumeAttachmentList</a>
* <a href="#VolumeAttachmentSource">interface VolumeAttachmentSource</a>
* <a href="#VolumeAttachmentSpec">interface VolumeAttachmentSpec</a>
* <a href="#VolumeAttachmentStatus">interface VolumeAttachmentStatus</a>
* <a href="#VolumeError">interface VolumeError</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isStorageClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19740">function isStorageClass</a>
</h2>

```typescript
isStorageClass(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19777">function isStorageClassList</a>
</h2>

```typescript
isStorageClassList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isVolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19824">function isVolumeAttachment</a>
</h2>

```typescript
isVolumeAttachment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isVolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19861">function isVolumeAttachmentList</a>
</h2>

```typescript
isVolumeAttachmentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="StorageClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18610">interface StorageClass</a>
</h2>

StorageClass describes the parameters for a class of storage for which PersistentVolumes can
be dynamically provisioned.

StorageClasses are non-namespaced; the name of the storage class according to etcd is in
ObjectMeta.Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18614">property allowVolumeExpansion</a>
</h3>

```typescript
allowVolumeExpansion: boolean;
```


AllowVolumeExpansion shows whether the storage class allow volume expand

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18622">property allowedTopologies</a>
</h3>

```typescript
allowedTopologies: TopologySelectorTerm[];
```


Restrict the node topologies where volumes can be dynamically provisioned. Each volume
plugin defines its own supported topology specifications. An empty TopologySelectorTerm
list means there is no topology restriction. This field is only honored by servers that
enable the VolumeScheduling feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18630">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18638">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18644">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18651">property mountOptions</a>
</h3>

```typescript
mountOptions: string[];
```


Dynamically provisioned PersistentVolumes of this storage class are created with these
mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one
is invalid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18657">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


Parameters holds the parameters for the provisioner that should create volumes of this
storage class.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18662">property provisioner</a>
</h3>

```typescript
provisioner: string;
```


Provisioner indicates the type of the provisioner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18668">property reclaimPolicy</a>
</h3>

```typescript
reclaimPolicy: string;
```


Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18675">property volumeBindingMode</a>
</h3>

```typescript
volumeBindingMode: string;
```


VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.
When unset, VolumeBindingImmediate is used. This field is only honored by servers that
enable the VolumeScheduling feature.

<h2 class="pdoc-module-header" id="StorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18682">interface StorageClassList</a>
</h2>

StorageClassList is a collection of storage classes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18689">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18694">property items</a>
</h3>

```typescript
items: StorageClass[];
```


Items is the list of StorageClasses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18702">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18708">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="VolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18718">interface VolumeAttachment</a>
</h2>

VolumeAttachment captures the intent to attach or detach the specified volume to/from the
specified node.

VolumeAttachment objects are non-namespaced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18725">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18733">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18739">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18745">property spec</a>
</h3>

```typescript
spec: VolumeAttachmentSpec;
```


Specification of the desired attach/detach volume behavior. Populated by the Kubernetes
system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18751">property status</a>
</h3>

```typescript
status: VolumeAttachmentStatus;
```


Status of the VolumeAttachment request. Populated by the entity completing the attach or
detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18758">interface VolumeAttachmentList</a>
</h2>

VolumeAttachmentList is a collection of VolumeAttachment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18765">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18770">property items</a>
</h3>

```typescript
items: VolumeAttachment[];
```


Items is the list of VolumeAttachments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18778">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18784">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="VolumeAttachmentSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18793">interface VolumeAttachmentSource</a>
</h2>

VolumeAttachmentSource represents a volume that should be attached. Right now only
PersistenVolumes can be attached via external attacher, in future we may allow also inline
volumes in pods. Exactly one member can be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18797">property persistentVolumeName</a>
</h3>

```typescript
persistentVolumeName: string;
```


Name of the persistent volume to attach.

<h2 class="pdoc-module-header" id="VolumeAttachmentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18804">interface VolumeAttachmentSpec</a>
</h2>

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18809">property attacher</a>
</h3>

```typescript
attacher: string;
```


Attacher indicates the name of the volume driver that MUST handle this request. This is the
name returned by GetPluginName().

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18814">property nodeName</a>
</h3>

```typescript
nodeName: string;
```


The node that the volume should be attached to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18819">property source</a>
</h3>

```typescript
source: VolumeAttachmentSource;
```


Source represents the volume that should be attached.

<h2 class="pdoc-module-header" id="VolumeAttachmentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18826">interface VolumeAttachmentStatus</a>
</h2>

VolumeAttachmentStatus is the status of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18831">property attachError</a>
</h3>

```typescript
attachError: VolumeError;
```


The last error encountered during attach operation, if any. This field must only be set by
the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18837">property attached</a>
</h3>

```typescript
attached: boolean;
```


Indicates the volume is successfully attached. This field must only be set by the entity
completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18844">property attachmentMetadata</a>
</h3>

```typescript
attachmentMetadata: { ... };
```


Upon successful attach, this field is populated with any information returned by the attach
operation that must be passed into subsequent WaitForAttach or Mount calls. This field must
only be set by the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18850">property detachError</a>
</h3>

```typescript
detachError: VolumeError;
```


The last error encountered during detach operation, if any. This field must only be set by
the entity completing the detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18857">interface VolumeError</a>
</h2>

VolumeError captures an error encountered during a volume operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18862">property message</a>
</h3>

```typescript
message: string;
```


String detailing the error encountered during Attach or Detach operation. This string maybe
logged, so it should not contain sensitive information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18867">property time</a>
</h3>

```typescript
time: string;
```


Time the error was encountered.

