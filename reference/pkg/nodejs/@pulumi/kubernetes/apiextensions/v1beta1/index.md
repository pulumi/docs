---
title: Module apiextensions/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apiextensions</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCustomResourceDefinition">function isCustomResourceDefinition</a>
* <a href="#isCustomResourceDefinitionList">function isCustomResourceDefinitionList</a>
* <a href="#CustomResourceColumnDefinition">interface CustomResourceColumnDefinition</a>
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

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L578">function isCustomResourceDefinition</a>
</h2>

```typescript
isCustomResourceDefinition(o: any): boolean
```

<h2 class="pdoc-module-header" id="isCustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L644">function isCustomResourceDefinitionList</a>
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

<h2 class="pdoc-module-header" id="CustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L513">interface CustomResourceDefinition</a>
</h2>

CustomResourceDefinition represents a resource that should be exposed on the API server.  Its
name MUST be in the format <.spec.name>.<.spec.group>.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L520">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L528">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L531">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L536">property spec</a>
</h3>

```typescript
spec: CustomResourceDefinitionSpec;
```


Spec describes how the user wants the resources to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L541">property status</a>
</h3>

```typescript
status: CustomResourceDefinitionStatus;
```


Status indicates the actual state of the CustomResourceDefinition

<h2 class="pdoc-module-header" id="CustomResourceDefinitionCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L548">interface CustomResourceDefinitionCondition</a>
</h2>

CustomResourceDefinitionCondition contains details for the current condition of this pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L552">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L557">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L562">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, one-word, CamelCase reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L567">property status</a>
</h3>

```typescript
status: string;
```


Status is the status of the condition. Can be True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L572">property type</a>
</h3>

```typescript
type: string;
```


Type is the type of the condition.

<h2 class="pdoc-module-header" id="CustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L579">interface CustomResourceDefinitionList</a>
</h2>

CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L586">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L591">property items</a>
</h3>

```typescript
items: CustomResourceDefinition[];
```


Items individual CustomResourceDefinitions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L599">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L602">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="CustomResourceDefinitionNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L609">interface CustomResourceDefinitionNames</a>
</h2>

CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L613">property categories</a>
</h3>

```typescript
categories: string[];
```


Categories is a list of grouped resources custom resources belong to (e.g. 'all')

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L618">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is the serialized kind of the resource.  It is normally CamelCase and singular.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L623">property listKind</a>
</h3>

```typescript
listKind: string;
```


ListKind is the serialized kind of the list for this resource.  Defaults to <kind>List.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L629">property plural</a>
</h3>

```typescript
plural: string;
```


Plural is the plural name of the resource to serve.  It must match the name of the
CustomResourceDefinition-registration too: plural.group and it must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L634">property shortNames</a>
</h3>

```typescript
shortNames: string[];
```


ShortNames are short names for the resource.  It must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L640">property singular</a>
</h3>

```typescript
singular: string;
```


Singular is the singular name of the resource.  It must be all lowercase  Defaults to
lowercased <kind>

<h2 class="pdoc-module-header" id="CustomResourceDefinitionSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L647">interface CustomResourceDefinitionSpec</a>
</h2>

CustomResourceDefinitionSpec describes how a user wants their resource to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L652">property additionalPrinterColumns</a>
</h3>

```typescript
additionalPrinterColumns: CustomResourceColumnDefinition[];
```


AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name.
Defaults to a created-at column.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L657">property group</a>
</h3>

```typescript
group: string;
```


Group is the group this resource belongs in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L662">property names</a>
</h3>

```typescript
names: CustomResourceDefinitionNames;
```


Names are the names used to describe this custom resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L668">property scope</a>
</h3>

```typescript
scope: string;
```


Scope indicates whether this resource is cluster or namespace scoped.  Default is
namespaced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L673">property subresources</a>
</h3>

```typescript
subresources: CustomResourceSubresources;
```


Subresources describes the subresources for CustomResources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L678">property validation</a>
</h3>

```typescript
validation: CustomResourceValidation;
```


Validation describes the validation methods for CustomResources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L685">property version</a>
</h3>

```typescript
version: string;
```


Version is the version this resource belongs in Should be always first item in Versions
field if provided. Optional, but at least one of Version or Versions must be set.
Deprecated: Please use `Versions`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L700">property versions</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L707">interface CustomResourceDefinitionStatus</a>
</h2>

CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L712">property acceptedNames</a>
</h3>

```typescript
acceptedNames: CustomResourceDefinitionNames;
```


AcceptedNames are the names that are actually being used to serve discovery They may be
different than the names in spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L717">property conditions</a>
</h3>

```typescript
conditions: CustomResourceDefinitionCondition[];
```


Conditions indicate state for particular aspects of a CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L726">property storedVersions</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L731">interface CustomResourceDefinitionVersion</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L735">property name</a>
</h3>

```typescript
name: string;
```


Name is the version name, e.g. “v1”, “v2beta1”, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L740">property served</a>
</h3>

```typescript
served: boolean;
```


Served is a flag enabling/disabling this version from being served via REST APIs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L746">property storage</a>
</h3>

```typescript
storage: boolean;
```


Storage flags the version as storage version. There must be exactly one flagged as storage
version.

<h2 class="pdoc-module-header" id="CustomResourceSubresourceScale">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L754">interface CustomResourceSubresourceScale</a>
</h2>

CustomResourceSubresourceScale defines how to serve the scale subresource for
CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L762">property labelSelectorPath</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L770">property specReplicasPath</a>
</h3>

```typescript
specReplicasPath: string;
```


SpecReplicasPath defines the JSON path inside of a CustomResource that corresponds to
Scale.Spec.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON
Path under .spec. If there is no value under the given path in the CustomResource, the
/scale subresource will return an error on GET.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L778">property statusReplicasPath</a>
</h3>

```typescript
statusReplicasPath: string;
```


StatusReplicasPath defines the JSON path inside of a CustomResource that corresponds to
Scale.Status.Replicas. Only JSON paths without the array notation are allowed. Must be a
JSON Path under .status. If there is no value under the given path in the CustomResource,
the status replica value in the /scale subresource will default to 0.

<h2 class="pdoc-module-header" id="CustomResourceSubresources">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L785">interface CustomResourceSubresources</a>
</h2>

CustomResourceSubresources defines the status and scale subresources for CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L789">property scale</a>
</h3>

```typescript
scale: CustomResourceSubresourceScale;
```


Scale denotes the scale subresource for CustomResources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L794">property status</a>
</h3>

```typescript
status: any;
```


Status denotes the status subresource for CustomResources

<h2 class="pdoc-module-header" id="CustomResourceValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L801">interface CustomResourceValidation</a>
</h2>

CustomResourceValidation is a list of validation methods for CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L805">property openAPIV3Schema</a>
</h3>

```typescript
openAPIV3Schema: JSONSchemaProps;
```


OpenAPIV3Schema is the OpenAPI v3 schema to be validated against.

<h2 class="pdoc-module-header" id="ExternalDocumentation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L812">interface ExternalDocumentation</a>
</h2>

ExternalDocumentation allows referencing an external resource for extended documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L814">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L817">property url</a>
</h3>

```typescript
url: string;
```

<h2 class="pdoc-module-header" id="JSONSchemaProps">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L824">interface JSONSchemaProps</a>
</h2>

JSONSchemaProps is a JSON-Schema following Specification Draft 4 (http://json-schema.org/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L826">property $ref</a>
</h3>

```typescript
$ref: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L829">property $schema</a>
</h3>

```typescript
$schema: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L832">property additionalItems</a>
</h3>

```typescript
additionalItems: JSONSchemaProps | boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L835">property additionalProperties</a>
</h3>

```typescript
additionalProperties: JSONSchemaProps | boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L838">property allOf</a>
</h3>

```typescript
allOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L841">property anyOf</a>
</h3>

```typescript
anyOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L844">property default</a>
</h3>

```typescript
default: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L847">property definitions</a>
</h3>

```typescript
definitions: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L850">property dependencies</a>
</h3>

```typescript
dependencies: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L853">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L856">property enum</a>
</h3>

```typescript
enum: any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L859">property example</a>
</h3>

```typescript
example: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L862">property exclusiveMaximum</a>
</h3>

```typescript
exclusiveMaximum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L865">property exclusiveMinimum</a>
</h3>

```typescript
exclusiveMinimum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L868">property externalDocs</a>
</h3>

```typescript
externalDocs: ExternalDocumentation;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L871">property format</a>
</h3>

```typescript
format: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L874">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L877">property items</a>
</h3>

```typescript
items: JSONSchemaProps | any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L880">property maxItems</a>
</h3>

```typescript
maxItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L883">property maxLength</a>
</h3>

```typescript
maxLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L886">property maxProperties</a>
</h3>

```typescript
maxProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L889">property maximum</a>
</h3>

```typescript
maximum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L892">property minItems</a>
</h3>

```typescript
minItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L895">property minLength</a>
</h3>

```typescript
minLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L898">property minProperties</a>
</h3>

```typescript
minProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L901">property minimum</a>
</h3>

```typescript
minimum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L904">property multipleOf</a>
</h3>

```typescript
multipleOf: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L907">property not</a>
</h3>

```typescript
not: JSONSchemaProps;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L910">property oneOf</a>
</h3>

```typescript
oneOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L913">property pattern</a>
</h3>

```typescript
pattern: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L916">property patternProperties</a>
</h3>

```typescript
patternProperties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L919">property properties</a>
</h3>

```typescript
properties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L922">property required</a>
</h3>

```typescript
required: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L925">property title</a>
</h3>

```typescript
title: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L928">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L931">property uniqueItems</a>
</h3>

```typescript
uniqueItems: boolean;
```

