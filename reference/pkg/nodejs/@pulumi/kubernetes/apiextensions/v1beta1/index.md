---
title: Module apiextensions/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">apiextensions</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isCustomResourceDefinition">function isCustomResourceDefinition</a>
* <a href="#isCustomResourceDefinitionList">function isCustomResourceDefinitionList</a>
* <a href="#CustomResourceDefinition">interface CustomResourceDefinition</a>
* <a href="#CustomResourceDefinitionCondition">interface CustomResourceDefinitionCondition</a>
* <a href="#CustomResourceDefinitionList">interface CustomResourceDefinitionList</a>
* <a href="#CustomResourceDefinitionNames">interface CustomResourceDefinitionNames</a>
* <a href="#CustomResourceDefinitionSpec">interface CustomResourceDefinitionSpec</a>
* <a href="#CustomResourceDefinitionStatus">interface CustomResourceDefinitionStatus</a>
* <a href="#CustomResourceValidation">interface CustomResourceValidation</a>
* <a href="#ExternalDocumentation">interface ExternalDocumentation</a>
* <a href="#JSON">interface JSON</a>
* <a href="#JSONSchemaProps">interface JSONSchemaProps</a>
* <a href="#JSONSchemaPropsOrArray">interface JSONSchemaPropsOrArray</a>
* <a href="#JSONSchemaPropsOrBool">interface JSONSchemaPropsOrBool</a>
* <a href="#JSONSchemaPropsOrStringArray">interface JSONSchemaPropsOrStringArray</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isCustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L520">function isCustomResourceDefinition</a>
</h2>

```typescript
isCustomResourceDefinition(o: any): boolean
```

<h2 class="pdoc-module-header" id="isCustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L586">function isCustomResourceDefinitionList</a>
</h2>

```typescript
isCustomResourceDefinitionList(o: any): boolean
```

<h2 class="pdoc-module-header" id="CustomResourceDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L456">interface CustomResourceDefinition</a>
</h2>

CustomResourceDefinition represents a resource that should be exposed on the API server.  Its
name MUST be in the format <.spec.name>.<.spec.group>.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L463">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L471">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L474">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L479">property spec</a>
</h3>

```typescript
spec: CustomResourceDefinitionSpec;
```


Spec describes how the user wants the resources to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L484">property status</a>
</h3>

```typescript
status: CustomResourceDefinitionStatus;
```


Status indicates the actual state of the CustomResourceDefinition

<h2 class="pdoc-module-header" id="CustomResourceDefinitionCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L491">interface CustomResourceDefinitionCondition</a>
</h2>

CustomResourceDefinitionCondition contains details for the current condition of this pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L495">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L500">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L505">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, one-word, CamelCase reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L510">property status</a>
</h3>

```typescript
status: string;
```


Status is the status of the condition. Can be True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L515">property type</a>
</h3>

```typescript
type: string;
```


Type is the type of the condition.

<h2 class="pdoc-module-header" id="CustomResourceDefinitionList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L522">interface CustomResourceDefinitionList</a>
</h2>

CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L529">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L534">property items</a>
</h3>

```typescript
items: CustomResourceDefinition[];
```


Items individual CustomResourceDefinitions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L542">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L545">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```

<h2 class="pdoc-module-header" id="CustomResourceDefinitionNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L552">interface CustomResourceDefinitionNames</a>
</h2>

CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L556">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is the serialized kind of the resource.  It is normally CamelCase and singular.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L561">property listKind</a>
</h3>

```typescript
listKind: string;
```


ListKind is the serialized kind of the list for this resource.  Defaults to <kind>List.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L567">property plural</a>
</h3>

```typescript
plural: string;
```


Plural is the plural name of the resource to serve.  It must match the name of the
CustomResourceDefinition-registration too: plural.group and it must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L572">property shortNames</a>
</h3>

```typescript
shortNames: string[];
```


ShortNames are short names for the resource.  It must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L578">property singular</a>
</h3>

```typescript
singular: string;
```


Singular is the singular name of the resource.  It must be all lowercase  Defaults to
lowercased <kind>

<h2 class="pdoc-module-header" id="CustomResourceDefinitionSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L585">interface CustomResourceDefinitionSpec</a>
</h2>

CustomResourceDefinitionSpec describes how a user wants their resource to appear

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L589">property group</a>
</h3>

```typescript
group: string;
```


Group is the group this resource belongs in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L594">property names</a>
</h3>

```typescript
names: CustomResourceDefinitionNames;
```


Names are the names used to describe this custom resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L600">property scope</a>
</h3>

```typescript
scope: string;
```


Scope indicates whether this resource is cluster or namespace scoped.  Default is
namespaced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L605">property validation</a>
</h3>

```typescript
validation: CustomResourceValidation;
```


Validation describes the validation methods for CustomResources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L610">property version</a>
</h3>

```typescript
version: string;
```


Version is the version this resource belongs in

<h2 class="pdoc-module-header" id="CustomResourceDefinitionStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L617">interface CustomResourceDefinitionStatus</a>
</h2>

CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L622">property acceptedNames</a>
</h3>

```typescript
acceptedNames: CustomResourceDefinitionNames;
```


AcceptedNames are the names that are actually being used to serve discovery They may be
different than the names in spec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L627">property conditions</a>
</h3>

```typescript
conditions: CustomResourceDefinitionCondition[];
```


Conditions indicate state for particular aspects of a CustomResourceDefinition

<h2 class="pdoc-module-header" id="CustomResourceValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L634">interface CustomResourceValidation</a>
</h2>

CustomResourceValidation is a list of validation methods for CustomResources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L638">property openAPIV3Schema</a>
</h3>

```typescript
openAPIV3Schema: JSONSchemaProps;
```


OpenAPIV3Schema is the OpenAPI v3 schema to be validated against.

<h2 class="pdoc-module-header" id="ExternalDocumentation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L645">interface ExternalDocumentation</a>
</h2>

ExternalDocumentation allows referencing an external resource for extended documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L647">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L650">property url</a>
</h3>

```typescript
url: string;
```

<h2 class="pdoc-module-header" id="JSON">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L658">interface JSON</a>
</h2>

JSON represents any valid JSON value. These types are supported: bool, int64, float64,
string, []interface{}, map[string]interface{} and nil.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L660">property Raw</a>
</h3>

```typescript
Raw: string;
```

<h2 class="pdoc-module-header" id="JSONSchemaProps">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L667">interface JSONSchemaProps</a>
</h2>

JSONSchemaProps is a JSON-Schema following Specification Draft 4 (http://json-schema.org/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L669">property $ref</a>
</h3>

```typescript
$ref: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L672">property $schema</a>
</h3>

```typescript
$schema: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L675">property additionalItems</a>
</h3>

```typescript
additionalItems: JSONSchemaPropsOrBool;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L678">property additionalProperties</a>
</h3>

```typescript
additionalProperties: JSONSchemaPropsOrBool;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L681">property allOf</a>
</h3>

```typescript
allOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L684">property anyOf</a>
</h3>

```typescript
anyOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L687">property default</a>
</h3>

```typescript
default: JSON;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L690">property definitions</a>
</h3>

```typescript
definitions: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L693">property dependencies</a>
</h3>

```typescript
dependencies: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L696">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L699">property enum</a>
</h3>

```typescript
enum: JSON[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L702">property example</a>
</h3>

```typescript
example: JSON;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L705">property exclusiveMaximum</a>
</h3>

```typescript
exclusiveMaximum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L708">property exclusiveMinimum</a>
</h3>

```typescript
exclusiveMinimum: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L711">property externalDocs</a>
</h3>

```typescript
externalDocs: ExternalDocumentation;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L714">property format</a>
</h3>

```typescript
format: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L717">property id</a>
</h3>

```typescript
id: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L720">property items</a>
</h3>

```typescript
items: JSONSchemaPropsOrArray;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L723">property maxItems</a>
</h3>

```typescript
maxItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L726">property maxLength</a>
</h3>

```typescript
maxLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L729">property maxProperties</a>
</h3>

```typescript
maxProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L732">property maximum</a>
</h3>

```typescript
maximum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L735">property minItems</a>
</h3>

```typescript
minItems: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L738">property minLength</a>
</h3>

```typescript
minLength: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L741">property minProperties</a>
</h3>

```typescript
minProperties: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L744">property minimum</a>
</h3>

```typescript
minimum: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L747">property multipleOf</a>
</h3>

```typescript
multipleOf: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L750">property not</a>
</h3>

```typescript
not: JSONSchemaProps;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L753">property oneOf</a>
</h3>

```typescript
oneOf: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L756">property pattern</a>
</h3>

```typescript
pattern: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L759">property patternProperties</a>
</h3>

```typescript
patternProperties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L762">property properties</a>
</h3>

```typescript
properties: object;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L765">property required</a>
</h3>

```typescript
required: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L768">property title</a>
</h3>

```typescript
title: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L771">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L774">property uniqueItems</a>
</h3>

```typescript
uniqueItems: boolean;
```

<h2 class="pdoc-module-header" id="JSONSchemaPropsOrArray">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L782">interface JSONSchemaPropsOrArray</a>
</h2>

JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of
JSONSchemaProps. Mainly here for serialization purposes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L784">property JSONSchemas</a>
</h3>

```typescript
JSONSchemas: JSONSchemaProps[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L787">property Schema</a>
</h3>

```typescript
Schema: JSONSchemaProps;
```

<h2 class="pdoc-module-header" id="JSONSchemaPropsOrBool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L795">interface JSONSchemaPropsOrBool</a>
</h2>

JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the
boolean property.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L797">property Allows</a>
</h3>

```typescript
Allows: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L800">property Schema</a>
</h3>

```typescript
Schema: JSONSchemaProps;
```

<h2 class="pdoc-module-header" id="JSONSchemaPropsOrStringArray">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L807">interface JSONSchemaPropsOrStringArray</a>
</h2>

JSONSchemaPropsOrStringArray represents a JSONSchemaProps or a string array.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L809">property Property</a>
</h3>

```typescript
Property: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L812">property Schema</a>
</h3>

```typescript
Schema: JSONSchemaProps;
```

