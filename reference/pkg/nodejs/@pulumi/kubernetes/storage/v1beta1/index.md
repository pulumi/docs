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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20387">function isStorageClass</a>
</h2>

```typescript
isStorageClass(o: any): boolean
```

<h2 class="pdoc-module-header" id="isStorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20424">function isStorageClassList</a>
</h2>

```typescript
isStorageClassList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isVolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20471">function isVolumeAttachment</a>
</h2>

```typescript
isVolumeAttachment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isVolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20508">function isVolumeAttachmentList</a>
</h2>

```typescript
isVolumeAttachmentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="StorageClass">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19225">interface StorageClass</a>
</h2>

StorageClass describes the parameters for a class of storage for which PersistentVolumes can
be dynamically provisioned.

StorageClasses are non-namespaced; the name of the storage class according to etcd is in
ObjectMeta.Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19229">property allowVolumeExpansion</a>
</h3>

```typescript
allowVolumeExpansion: boolean;
```


AllowVolumeExpansion shows whether the storage class allow volume expand

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19237">property allowedTopologies</a>
</h3>

```typescript
allowedTopologies: TopologySelectorTerm[];
```


Restrict the node topologies where volumes can be dynamically provisioned. Each volume
plugin defines its own supported topology specifications. An empty TopologySelectorTerm
list means there is no topology restriction. This field is only honored by servers that
enable the VolumeScheduling feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19245">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19253">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19259">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19266">property mountOptions</a>
</h3>

```typescript
mountOptions: string[];
```


Dynamically provisioned PersistentVolumes of this storage class are created with these
mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one
is invalid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19272">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


Parameters holds the parameters for the provisioner that should create volumes of this
storage class.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19277">property provisioner</a>
</h3>

```typescript
provisioner: string;
```


Provisioner indicates the type of the provisioner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19283">property reclaimPolicy</a>
</h3>

```typescript
reclaimPolicy: string;
```


Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19290">property volumeBindingMode</a>
</h3>

```typescript
volumeBindingMode: string;
```


VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.
When unset, VolumeBindingImmediate is used. This field is only honored by servers that
enable the VolumeScheduling feature.

<h2 class="pdoc-module-header" id="StorageClassList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19297">interface StorageClassList</a>
</h2>

StorageClassList is a collection of storage classes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19304">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19309">property items</a>
</h3>

```typescript
items: StorageClass[];
```


Items is the list of StorageClasses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19317">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19323">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="VolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19333">interface VolumeAttachment</a>
</h2>

VolumeAttachment captures the intent to attach or detach the specified volume to/from the
specified node.

VolumeAttachment objects are non-namespaced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19340">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19348">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19354">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19360">property spec</a>
</h3>

```typescript
spec: VolumeAttachmentSpec;
```


Specification of the desired attach/detach volume behavior. Populated by the Kubernetes
system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19366">property status</a>
</h3>

```typescript
status: VolumeAttachmentStatus;
```


Status of the VolumeAttachment request. Populated by the entity completing the attach or
detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19373">interface VolumeAttachmentList</a>
</h2>

VolumeAttachmentList is a collection of VolumeAttachment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19380">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19385">property items</a>
</h3>

```typescript
items: VolumeAttachment[];
```


Items is the list of VolumeAttachments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19393">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19399">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="VolumeAttachmentSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19408">interface VolumeAttachmentSource</a>
</h2>

VolumeAttachmentSource represents a volume that should be attached. Right now only
PersistenVolumes can be attached via external attacher, in future we may allow also inline
volumes in pods. Exactly one member can be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19412">property persistentVolumeName</a>
</h3>

```typescript
persistentVolumeName: string;
```


Name of the persistent volume to attach.

<h2 class="pdoc-module-header" id="VolumeAttachmentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19419">interface VolumeAttachmentSpec</a>
</h2>

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19424">property attacher</a>
</h3>

```typescript
attacher: string;
```


Attacher indicates the name of the volume driver that MUST handle this request. This is the
name returned by GetPluginName().

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19429">property nodeName</a>
</h3>

```typescript
nodeName: string;
```


The node that the volume should be attached to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19434">property source</a>
</h3>

```typescript
source: VolumeAttachmentSource;
```


Source represents the volume that should be attached.

<h2 class="pdoc-module-header" id="VolumeAttachmentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19441">interface VolumeAttachmentStatus</a>
</h2>

VolumeAttachmentStatus is the status of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19446">property attachError</a>
</h3>

```typescript
attachError: VolumeError;
```


The last error encountered during attach operation, if any. This field must only be set by
the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19452">property attached</a>
</h3>

```typescript
attached: boolean;
```


Indicates the volume is successfully attached. This field must only be set by the entity
completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19459">property attachmentMetadata</a>
</h3>

```typescript
attachmentMetadata: { ... };
```


Upon successful attach, this field is populated with any information returned by the attach
operation that must be passed into subsequent WaitForAttach or Mount calls. This field must
only be set by the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19465">property detachError</a>
</h3>

```typescript
detachError: VolumeError;
```


The last error encountered during detach operation, if any. This field must only be set by
the entity completing the detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19472">interface VolumeError</a>
</h2>

VolumeError captures an error encountered during a volume operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19477">property message</a>
</h3>

```typescript
message: string;
```


String detailing the error encountered during Attach or Detach operation. This string maybe
logged, so it should not contain sensitive information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19482">property time</a>
</h3>

```typescript
time: string;
```


Time the error was encountered.

