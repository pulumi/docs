---
title: Module storage/v1alpha1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">storage</a> &gt; v1alpha1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isVolumeAttachment">function isVolumeAttachment</a>
* <a href="#isVolumeAttachmentList">function isVolumeAttachmentList</a>
* <a href="#VolumeAttachment">interface VolumeAttachment</a>
* <a href="#VolumeAttachmentList">interface VolumeAttachmentList</a>
* <a href="#VolumeAttachmentSource">interface VolumeAttachmentSource</a>
* <a href="#VolumeAttachmentSpec">interface VolumeAttachmentSpec</a>
* <a href="#VolumeAttachmentStatus">interface VolumeAttachmentStatus</a>
* <a href="#VolumeError">interface VolumeError</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isVolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20180">function isVolumeAttachment</a>
</h2>

```typescript
isVolumeAttachment(o: any): boolean
```

<h2 class="pdoc-module-header" id="isVolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L20217">function isVolumeAttachmentList</a>
</h2>

```typescript
isVolumeAttachmentList(o: any): boolean
```

<h2 class="pdoc-module-header" id="VolumeAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19062">interface VolumeAttachment</a>
</h2>

VolumeAttachment captures the intent to attach or detach the specified volume to/from the
specified node.

VolumeAttachment objects are non-namespaced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19069">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19077">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19083">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19089">property spec</a>
</h3>

```typescript
spec: VolumeAttachmentSpec;
```


Specification of the desired attach/detach volume behavior. Populated by the Kubernetes
system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19095">property status</a>
</h3>

```typescript
status: VolumeAttachmentStatus;
```


Status of the VolumeAttachment request. Populated by the entity completing the attach or
detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeAttachmentList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19102">interface VolumeAttachmentList</a>
</h2>

VolumeAttachmentList is a collection of VolumeAttachment objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19109">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19114">property items</a>
</h3>

```typescript
items: VolumeAttachment[];
```


Items is the list of VolumeAttachments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19122">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19128">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="VolumeAttachmentSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19137">interface VolumeAttachmentSource</a>
</h2>

VolumeAttachmentSource represents a volume that should be attached. Right now only
PersistenVolumes can be attached via external attacher, in future we may allow also inline
volumes in pods. Exactly one member can be set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19141">property persistentVolumeName</a>
</h3>

```typescript
persistentVolumeName: string;
```


Name of the persistent volume to attach.

<h2 class="pdoc-module-header" id="VolumeAttachmentSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19148">interface VolumeAttachmentSpec</a>
</h2>

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19153">property attacher</a>
</h3>

```typescript
attacher: string;
```


Attacher indicates the name of the volume driver that MUST handle this request. This is the
name returned by GetPluginName().

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19158">property nodeName</a>
</h3>

```typescript
nodeName: string;
```


The node that the volume should be attached to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19163">property source</a>
</h3>

```typescript
source: VolumeAttachmentSource;
```


Source represents the volume that should be attached.

<h2 class="pdoc-module-header" id="VolumeAttachmentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19170">interface VolumeAttachmentStatus</a>
</h2>

VolumeAttachmentStatus is the status of a VolumeAttachment request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19175">property attachError</a>
</h3>

```typescript
attachError: VolumeError;
```


The last error encountered during attach operation, if any. This field must only be set by
the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19181">property attached</a>
</h3>

```typescript
attached: boolean;
```


Indicates the volume is successfully attached. This field must only be set by the entity
completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19188">property attachmentMetadata</a>
</h3>

```typescript
attachmentMetadata: { ... };
```


Upon successful attach, this field is populated with any information returned by the attach
operation that must be passed into subsequent WaitForAttach or Mount calls. This field must
only be set by the entity completing the attach operation, i.e. the external-attacher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19194">property detachError</a>
</h3>

```typescript
detachError: VolumeError;
```


The last error encountered during detach operation, if any. This field must only be set by
the entity completing the detach operation, i.e. the external-attacher.

<h2 class="pdoc-module-header" id="VolumeError">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19201">interface VolumeError</a>
</h2>

VolumeError captures an error encountered during a volume operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19206">property message</a>
</h3>

```typescript
message: string;
```


String detailing the error encountered during Attach or Detach operation. This string maybe
logged, so it should not contain sensitive information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L19211">property time</a>
</h3>

```typescript
time: string;
```


Time the error was encountered.

