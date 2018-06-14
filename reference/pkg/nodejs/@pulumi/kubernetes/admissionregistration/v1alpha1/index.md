---
title: Module admissionregistration/v1alpha1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">admissionregistration</a> &gt; v1alpha1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Initializer">interface Initializer</a>
* <a href="#InitializerConfiguration">interface InitializerConfiguration</a>
* <a href="#InitializerConfigurationList">interface InitializerConfigurationList</a>
* <a href="#Rule">interface Rule</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="Initializer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10">interface Initializer</a>
</h2>

Initializer describes the name and the failure policy of an initializer, and what resources
it applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L17">property name</a>
</h3>

```typescript
name: string;
```


Name is the identifier of the initializer. It will be added to the object that needs to be
initialized. Name should be fully qualified, e.g., alwayspullimages.kubernetes.io, where
"alwayspullimages" is the name of the webhook, and kubernetes.io is the name of the
organization. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L24">property rules</a>
</h3>

```typescript
rules: Rule[];
```


Rules describes what resources/subresources the initializer cares about. The initializer
cares about an operation if it matches _any_ Rule. Rule.Resources must not include
subresources.

<h2 class="pdoc-module-header" id="InitializerConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L31">interface InitializerConfiguration</a>
</h2>

InitializerConfiguration describes the configuration of initializers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L38">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L46">property initializers</a>
</h3>

```typescript
initializers: Initializer[];
```


Initializers is a list of resources and their default initializers Order-sensitive. When
merging multiple InitializerConfigurations, we sort the initializers from different
InitializerConfigurations by the name of the InitializerConfigurations; the order of the
initializers from the same InitializerConfiguration is preserved.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L54">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L60">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object metadata; More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

<h2 class="pdoc-module-header" id="InitializerConfigurationList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L67">interface InitializerConfigurationList</a>
</h2>

InitializerConfigurationList is a list of InitializerConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L74">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L79">property items</a>
</h3>

```typescript
items: InitializerConfiguration[];
```


List of InitializerConfiguration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L87">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L93">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L101">interface Rule</a>
</h2>

Rule is a tuple of APIGroups, APIVersion, and Resources.It is recommended to make sure that
all the tuple expansions are valid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L106">property apiGroups</a>
</h3>

```typescript
apiGroups: string[];
```


APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present,
the length of the slice must be one. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L112">property apiVersions</a>
</h3>

```typescript
apiVersions: string[];
```


APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is
present, the length of the slice must be one. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L126">property resources</a>
</h3>

```typescript
resources: string[];
```


Resources is a list of resources this rule applies to.

For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all
resources, but not subresources. 'pods/*' means all subresources of pods. '*&#8205;/scale'
means all scale subresources. '*&#8205;/*' means all resources and their subresources.

If wildcard is present, the validation rule will ensure resources do not overlap with each
other.

Depending on the enclosing object, subresources might not be allowed. Required.

