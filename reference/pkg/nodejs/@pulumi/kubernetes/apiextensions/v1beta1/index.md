---
title: Module apiextensions/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apiextensions</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCustomResourceDefinition">function isCustomResourceDefinition</a>
* <a href="#isCustomResourceDefinitionList">function isCustomResourceDefinitionList</a>
* <a href="#CustomResourceColumnDefinition">interface CustomResourceColumnDefinition</a>
* <a href="#CustomResourceConversion">interface CustomResourceConversion</a>
* <a href="#CustomResourceDefinition">interface CustomResourceDefinition</a>
* <a href="#CustomResourceDefinitionCondition">interface CustomResourceDefinitionCondition</a>
* <a href="#CustomResourceDefinitionList">interface CustomResourceDefinitionList</a>
* <a href="#CustomResourceDefinitionNames">interface CustomResourceDefinitionNames</a>
* <a href="#CustomResourceDefinitionSpec">interface CustomResourceDefinitionSpec</a>
* <a href="#CustomResourceDefinitionStatus">interface CustomResourceDefinitionStatus</a>
* <a href="#CustomResourceDefinitionVersion">interface CustomResourceDefinitionVersion</a>
* <a href="#CustomResourceSubresourceScale">interface CustomResourceSubresourceScale</a>
* <a href="#CustomResourceSubresources">interface CustomResourceSubresources</a>
* <a href="#CustomResourceValidation">interface CustomResourceValidation</a>
* <a href="#ExternalDocumentation">interface ExternalDocumentation</a>
* <a href="#JSONSchemaProps">interface JSONSchemaProps</a>
* <a href="#ServiceReference">interface ServiceReference</a>
* <a href="#WebhookClientConfig">interface WebhookClientConfig</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L600">function isCustomResourceDefinition</a>
</h2>

```typescript
isCustomResourceDefinition(o: any): boolean
```

<h2 class="pdoc-module-header" id="isCustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L666">function isCustomResourceDefinitionList</a>
</h2>

```typescript
isCustomResourceDefinitionList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CustomResourceColumnDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L468">interface CustomResourceColumnDefinition</a>
</h2>

CustomResourceColumnDefinition specifies a column for server side printing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L472">property JSONPath</a>
</h3>

```typescript
JSONPath: string;
```


JSONPath is a simple JSON path, i.e. with array notation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L477">property description</a>
</h3>

```typescript
description: string;
```


description is a human readable description of this column.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L486">property format</a>
</h3>

```typescript
format: string;
```


format is an optional OpenAPI type definition for this column. The 'name' format is applied
to the primary identifier column to assist in clients identifying column is the resource
name. See
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for
more.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L491">property name</a>
</h3>

```typescript
name: string;
```


name is a human readable name for the column.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L498">property priority</a>
</h3>

```typescript
priority: number;
```


priority is an integer defining the relative importance of this column compared to others.
Lower numbers are considered higher priority. Columns that may be omitted in limited space
scenarios should be given a higher priority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L505">property type</a>
</h3>

```typescript
type: string;
```


type is an OpenAPI type definition for this column. See
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for
more.

<h2 class="pdoc-module-header" id="CustomResourceConversion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L512">interface CustomResourceConversion</a>
</h2>

CustomResourceConversion describes how to convert different versions of a CR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L519">property strategy</a>
</h3>

```typescript
strategy: string;
```


`strategy` specifies the conversion strategy. Allowed values are: - `None`: The converter
only change the apiVersion and would not touch any other field in the CR. - `Webhook`: API
Server will call to an external webhook to do the conversion. Additional information is
needed for this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L526">property webhookClientConfig</a>
</h3>

```typescript
webhookClientConfig: WebhookClientConfig;
```


`webhookClientConfig` is the instructions for how to call the webhook if strategy is
`Webhook`. This field is alpha-level and is only honored by servers that enable the
CustomResourceWebhookConversion feature.

<h2 class="pdoc-module-header" id="CustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L534">interface CustomResourceDefinition</a>
</h2>

CustomResourceDefinition represents a resource that should be exposed on the API server.  Its
name MUST be in the format <.spec.name>.<.spec.group>.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L541">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L549">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L552">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L557">property spec</a>
</h3>

```typescript
spec: CustomResourceDefinitionSpec;
```


Spec describes how the user wants the resources to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L562">property status</a>
</h3>

```typescript
status: CustomResourceDefinitionStatus;
```


Status indicates the actual state of the CustomResourceDefinition

<h2 class="pdoc-module-header" id="CustomResourceDefinitionCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L569">interface CustomResourceDefinitionCondition</a>
</h2>

CustomResourceDefinitionCondition contains details for the current condition of this pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L573">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L578">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L583">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, one-word, CamelCase reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L588">property status</a>
</h3>

```typescript
status: string;
```


Status is the status of the condition. Can be True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L593">property type</a>
</h3>

```typescript
type: string;
```


Type is the type of the condition.

<h2 class="pdoc-module-header" id="CustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L600">interface CustomResourceDefinitionList</a>
</h2>

CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L607">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L612">property items</a>
</h3>

```typescript
items: CustomResourceDefinition[];
```


Items individual CustomResourceDefinitions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L620">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L623">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="CustomResourceDefinitionNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L630">interface CustomResourceDefinitionNames</a>
</h2>

CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L634">property categories</a>
</h3>

```typescript
categories: string[];
```


Categories is a list of grouped resources custom resources belong to (e.g. 'all')

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L639">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is the serialized kind of the resource.  It is normally CamelCase and singular.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L644">property listKind</a>
</h3>

```typescript
listKind: string;
```


ListKind is the serialized kind of the list for this resource.  Defaults to <kind>List.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L650">property plural</a>
</h3>

```typescript
plural: string;
```


Plural is the plural name of the resource to serve.  It must match the name of the
CustomResourceDefinition-registration too: plural.group and it must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L655">property shortNames</a>
</h3>

```typescript
shortNames: string[];
```


ShortNames are short names for the resource.  It must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L661">property singular</a>
</h3>

```typescript
singular: string;
```


Singular is the singular name of the resource.  It must be all lowercase  Defaults to
lowercased <kind>

<h2 class="pdoc-module-header" id="CustomResourceDefinitionSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L668">interface CustomResourceDefinitionSpec</a>
</h2>

CustomResourceDefinitionSpec describes how a user wants their resource to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L674">property additionalPrinterColumns</a>
</h3>

```typescript
additionalPrinterColumns: CustomResourceColumnDefinition[];
```


AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name.
Defaults to a created-at column. Optional, the global columns for all versions. Top-level
and per-version columns are mutually exclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L679">property conversion</a>
</h3>

```typescript
conversion: CustomResourceConversion;
```


`conversion` defines conversion settings for the CRD.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L684">property group</a>
</h3>

```typescript
group: string;
```


Group is the group this resource belongs in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L689">property names</a>
</h3>

```typescript
names: CustomResourceDefinitionNames;
```


Names are the names used to describe this custom resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L695">property scope</a>
</h3>

```typescript
scope: string;
```


Scope indicates whether this resource is cluster or namespace scoped.  Default is
namespaced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L702">property subresources</a>
</h3>

```typescript
subresources: CustomResourceSubresources;
```


Subresources describes the subresources for CustomResource Optional, the global
subresources for all versions. Top-level and per-version subresources are mutually
exclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L709">property validation</a>
</h3>

```typescript
validation: CustomResourceValidation;
```


Validation describes the validation methods for CustomResources Optional, the global
validation schema for all versions. Top-level and per-version schemas are mutually
exclusive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L716">property version</a>
</h3>

```typescript
version: string;
```


Version is the version this resource belongs in Should be always first item in Versions
field if provided. Optional, but at least one of Version or Versions must be set.
Deprecated: Please use `Versions`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L731">property versions</a>
</h3>

```typescript
versions: CustomResourceDefinitionVersion[];
```


Versions is the list of all supported versions for this resource. If Version field is
provided, this field is optional. Validation: All versions must use the same validation
schema for now. i.e., top level Validation field is applied to all of these versions.
Order: The version name will be used to compute the order. If the version string is
"kube-like", it will sort above non "kube-like" version strings, which are ordered
lexicographically. "Kube-like" versions start with a "v", then are followed by a number
(the major version), then optionally the string "alpha" or "beta" and another number (the
minor version). These are sorted first by GA > beta > alpha (where GA is a version with no
suffix such as beta or alpha), and then by comparing major version, then minor version. An
example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1,
v11alpha2, foo1, foo10.

<h2 class="pdoc-module-header" id="CustomResourceDefinitionStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L738">interface CustomResourceDefinitionStatus</a>
</h2>

CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L743">property acceptedNames</a>
</h3>

```typescript
acceptedNames: CustomResourceDefinitionNames;
```


AcceptedNames are the names that are actually being used to serve discovery They may be
different than the names in spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L748">property conditions</a>
</h3>

```typescript
conditions: CustomResourceDefinitionCondition[];
```


Conditions indicate state for particular aspects of a CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L757">property storedVersions</a>
</h3>

```typescript
storedVersions: string[];
```


StoredVersions are all versions of CustomResources that were ever persisted. Tracking these
versions allows a migration path for stored versions in etcd. The field is mutable so the
migration controller can first finish a migration to another version (i.e. that no old
objects are left in the storage), and then remove the rest of the versions from this list.
None of the versions in this list can be removed from the spec.Versions field.

<h2 class="pdoc-module-header" id="CustomResourceDefinitionVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L764">interface CustomResourceDefinitionVersion</a>
</h2>

CustomResourceDefinitionVersion describes a version for CRD.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L775">property additionalPrinterColumns</a>
</h3>

```typescript
additionalPrinterColumns: CustomResourceColumnDefinition[];
```


AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name.
Defaults to a created-at column. Top-level and per-version columns are mutually exclusive.
Per-version columns must not all be set to identical values (top-level columns should be
used instead) This field is alpha-level and is only honored by servers that enable the
CustomResourceWebhookConversion feature. NOTE: CRDs created prior to 1.13 populated the
top-level additionalPrinterColumns field by default. To apply an update that changes to
per-version additionalPrinterColumns, the top-level additionalPrinterColumns field must be
explicitly set to null

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L780">property name</a>
</h3>

```typescript
name: string;
```


Name is the version name, e.g. “v1”, “v2beta1”, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L789">property schema</a>
</h3>

```typescript
schema: CustomResourceValidation;
```


Schema describes the schema for CustomResource used in validation, pruning, and defaulting.
Top-level and per-version schemas are mutually exclusive. Per-version schemas must not all
be set to identical values (top-level validation schema should be used instead) This field
is alpha-level and is only honored by servers that enable the
CustomResourceWebhookConversion feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L794">property served</a>
</h3>

```typescript
served: boolean;
```


Served is a flag enabling/disabling this version from being served via REST APIs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L800">property storage</a>
</h3>

```typescript
storage: boolean;
```


Storage flags the version as storage version. There must be exactly one flagged as storage
version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L808">property subresources</a>
</h3>

```typescript
subresources: CustomResourceSubresources;
```


Subresources describes the subresources for CustomResource Top-level and per-version
subresources are mutually exclusive. Per-version subresources must not all be set to
identical values (top-level subresources should be used instead) This field is alpha-level
and is only honored by servers that enable the CustomResourceWebhookConversion feature.

<h2 class="pdoc-module-header" id="CustomResourceSubresourceScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L816">interface CustomResourceSubresourceScale</a>
</h2>

CustomResourceSubresourceScale defines how to serve the scale subresource for
CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L824">property labelSelectorPath</a>
</h3>

```typescript
labelSelectorPath: string;
```


LabelSelectorPath defines the JSON path inside of a CustomResource that corresponds to
Scale.Status.Selector. Only JSON paths without the array notation are allowed. Must be a
JSON Path under .status. Must be set to work with HPA. If there is no value under the given
path in the CustomResource, the status label selector value in the /scale subresource will
default to the empty string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L832">property specReplicasPath</a>
</h3>

```typescript
specReplicasPath: string;
```


SpecReplicasPath defines the JSON path inside of a CustomResource that corresponds to
Scale.Spec.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON
Path under .spec. If there is no value under the given path in the CustomResource, the
/scale subresource will return an error on GET.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L840">property statusReplicasPath</a>
</h3>

```typescript
statusReplicasPath: string;
```


StatusReplicasPath defines the JSON path inside of a CustomResource that corresponds to
Scale.Status.Replicas. Only JSON paths without the array notation are allowed. Must be a
JSON Path under .status. If there is no value under the given path in the CustomResource,
the status replica value in the /scale subresource will default to 0.

<h2 class="pdoc-module-header" id="CustomResourceSubresources">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L847">interface CustomResourceSubresources</a>
</h2>

CustomResourceSubresources defines the status and scale subresources for CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L851">property scale</a>
</h3>

```typescript
scale: CustomResourceSubresourceScale;
```


Scale denotes the scale subresource for CustomResources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L856">property status</a>
</h3>

```typescript
status: any;
```


Status denotes the status subresource for CustomResources

<h2 class="pdoc-module-header" id="CustomResourceValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L863">interface CustomResourceValidation</a>
</h2>

CustomResourceValidation is a list of validation methods for CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L867">property openAPIV3Schema</a>
</h3>

```typescript
openAPIV3Schema: JSONSchemaProps;
```


OpenAPIV3Schema is the OpenAPI v3 schema to be validated against.

<h2 class="pdoc-module-header" id="ExternalDocumentation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L874">interface ExternalDocumentation</a>
</h2>

ExternalDocumentation allows referencing an external resource for extended documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L876">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L879">property url</a>
</h3>

```typescript
url: string;
```

<h2 class="pdoc-module-header" id="JSONSchemaProps">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L886">interface JSONSchemaProps</a>
</h2>

JSONSchemaProps is a JSON-Schema following Specification Draft 4 (http://json-schema.org/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L888">property $ref</a>
</h3>

```typescript
$ref: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L891">property $schema</a>
</h3>

```typescript
$schema: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L894">property additionalItems</a>
</h3>

```typescript
additionalItems: JSONSchemaProps | boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L897">property additionalProperties</a>
</h3>

```typescript
additionalProperties: JSONSchemaProps | boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L900">property allOf</a>
</h3>

```typescript
allOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L903">property anyOf</a>
</h3>

```typescript
anyOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L906">property default</a>
</h3>

```typescript
default: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L909">property definitions</a>
</h3>

```typescript
definitions: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L912">property dependencies</a>
</h3>

```typescript
dependencies: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L915">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L918">property enum</a>
</h3>

```typescript
enum: any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L921">property example</a>
</h3>

```typescript
example: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L924">property exclusiveMaximum</a>
</h3>

```typescript
exclusiveMaximum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L927">property exclusiveMinimum</a>
</h3>

```typescript
exclusiveMinimum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L930">property externalDocs</a>
</h3>

```typescript
externalDocs: ExternalDocumentation;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L933">property format</a>
</h3>

```typescript
format: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L936">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L939">property items</a>
</h3>

```typescript
items: JSONSchemaProps | any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L942">property maxItems</a>
</h3>

```typescript
maxItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L945">property maxLength</a>
</h3>

```typescript
maxLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L948">property maxProperties</a>
</h3>

```typescript
maxProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L951">property maximum</a>
</h3>

```typescript
maximum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L954">property minItems</a>
</h3>

```typescript
minItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L957">property minLength</a>
</h3>

```typescript
minLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L960">property minProperties</a>
</h3>

```typescript
minProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L963">property minimum</a>
</h3>

```typescript
minimum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L966">property multipleOf</a>
</h3>

```typescript
multipleOf: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L969">property not</a>
</h3>

```typescript
not: JSONSchemaProps;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L972">property oneOf</a>
</h3>

```typescript
oneOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L975">property pattern</a>
</h3>

```typescript
pattern: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L978">property patternProperties</a>
</h3>

```typescript
patternProperties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L981">property properties</a>
</h3>

```typescript
properties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L984">property required</a>
</h3>

```typescript
required: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L987">property title</a>
</h3>

```typescript
title: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L990">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L993">property uniqueItems</a>
</h3>

```typescript
uniqueItems: boolean;
```

<h2 class="pdoc-module-header" id="ServiceReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1000">interface ServiceReference</a>
</h2>

ServiceReference holds a reference to Service.legacy.k8s.io

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1004">property name</a>
</h3>

```typescript
name: string;
```


`name` is the name of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1009">property namespace</a>
</h3>

```typescript
namespace: string;
```


`namespace` is the namespace of the service. Required

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1014">property path</a>
</h3>

```typescript
path: string;
```


`path` is an optional URL path which will be sent in any request to this service.

<h2 class="pdoc-module-header" id="WebhookClientConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1022">interface WebhookClientConfig</a>
</h2>

WebhookClientConfig contains the information to make a TLS connection with the webhook. It
has the same field as admissionregistration.v1beta1.WebhookClientConfig.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1027">property caBundle</a>
</h3>

```typescript
caBundle: string;
```


`caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server
certificate. If unspecified, system trust roots on the apiserver are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1037">property service</a>
</h3>

```typescript
service: ServiceReference;
```


`service` is a reference to the service for this webhook. Either `service` or `url` must be
specified.

If the webhook is running within the cluster, then you should use `service`.

Port 443 will be used if it is open, otherwise it is an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L1061">property url</a>
</h3>

```typescript
url: string;
```


`url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`).
Exactly one of `url` or `service` must be specified.

The `host` should not refer to a service running in the cluster; use the `service` field
instead. The host might be resolved via external DNS in some apiservers (e.g.,
`kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation).
`host` may also be an IP address.

Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take
great care to run this webhook on all hosts which run an apiserver which might need to make
calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn
up in a new cluster.

The scheme must be "https"; the URL must begin with "https://".

A path is optional, and if present may be any string permissible in a URL. You may use the
path to pass an arbitrary string to the webhook, for example, a cluster identifier.

Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments
("#...") and query parameters ("?...") are not allowed, either.

