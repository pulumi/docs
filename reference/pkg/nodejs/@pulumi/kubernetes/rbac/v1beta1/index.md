---
title: Module rbac/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">rbac</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isClusterRole">function isClusterRole</a>
* <a href="#isClusterRoleBinding">function isClusterRoleBinding</a>
* <a href="#isClusterRoleBindingList">function isClusterRoleBindingList</a>
* <a href="#isClusterRoleList">function isClusterRoleList</a>
* <a href="#isRole">function isRole</a>
* <a href="#isRoleBinding">function isRoleBinding</a>
* <a href="#isRoleBindingList">function isRoleBindingList</a>
* <a href="#isRoleList">function isRoleList</a>
* <a href="#AggregationRule">interface AggregationRule</a>
* <a href="#ClusterRole">interface ClusterRole</a>
* <a href="#ClusterRoleBinding">interface ClusterRoleBinding</a>
* <a href="#ClusterRoleBindingList">interface ClusterRoleBindingList</a>
* <a href="#ClusterRoleList">interface ClusterRoleList</a>
* <a href="#PolicyRule">interface PolicyRule</a>
* <a href="#Role">interface Role</a>
* <a href="#RoleBinding">interface RoleBinding</a>
* <a href="#RoleBindingList">interface RoleBindingList</a>
* <a href="#RoleList">interface RoleList</a>
* <a href="#RoleRef">interface RoleRef</a>
* <a href="#Subject">interface Subject</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isClusterRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19171">function isClusterRole</a>
</h2>

```typescript
isClusterRole(o: any): boolean
```

<h2 class="pdoc-module-header" id="isClusterRoleBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19214">function isClusterRoleBinding</a>
</h2>

```typescript
isClusterRoleBinding(o: any): boolean
```

<h2 class="pdoc-module-header" id="isClusterRoleBindingList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19250">function isClusterRoleBindingList</a>
</h2>

```typescript
isClusterRoleBindingList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isClusterRoleList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19286">function isClusterRoleList</a>
</h2>

```typescript
isClusterRoleList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19366">function isRole</a>
</h2>

```typescript
isRole(o: any): boolean
```

<h2 class="pdoc-module-header" id="isRoleBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19411">function isRoleBinding</a>
</h2>

```typescript
isRoleBinding(o: any): boolean
```

<h2 class="pdoc-module-header" id="isRoleBindingList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19447">function isRoleBindingList</a>
</h2>

```typescript
isRoleBindingList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isRoleList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L19483">function isRoleList</a>
</h2>

```typescript
isRoleList(o: any): boolean
```

<h2 class="pdoc-module-header" id="AggregationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18120">interface AggregationRule</a>
</h2>

AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18126">property clusterRoleSelectors</a>
</h3>

```typescript
clusterRoleSelectors: LabelSelector[];
```


ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and
create the rules. If any of the selectors match, then the ClusterRole's permissions will be
added

<h2 class="pdoc-module-header" id="ClusterRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18134">interface ClusterRole</a>
</h2>

ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a
unit by a RoleBinding or ClusterRoleBinding.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18140">property aggregationRule</a>
</h3>

```typescript
aggregationRule: AggregationRule;
```


AggregationRule is an optional field that describes how to build the Rules for this
ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct
changes to Rules will be stomped by the controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18148">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18156">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18161">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18166">property rules</a>
</h3>

```typescript
rules: PolicyRule[];
```


Rules holds all the PolicyRules for this ClusterRole

<h2 class="pdoc-module-header" id="ClusterRoleBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18174">interface ClusterRoleBinding</a>
</h2>

ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a
ClusterRole in the global namespace, and adds who information via Subject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18181">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18189">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18194">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18200">property roleRef</a>
</h3>

```typescript
roleRef: RoleRef;
```


RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be
resolved, the Authorizer must return an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18205">property subjects</a>
</h3>

```typescript
subjects: Subject[];
```


Subjects holds references to the objects the role applies to.

<h2 class="pdoc-module-header" id="ClusterRoleBindingList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18212">interface ClusterRoleBindingList</a>
</h2>

ClusterRoleBindingList is a collection of ClusterRoleBindings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18219">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18224">property items</a>
</h3>

```typescript
items: ClusterRoleBinding[];
```


Items is a list of ClusterRoleBindings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18232">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18237">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard object's metadata.

<h2 class="pdoc-module-header" id="ClusterRoleList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18244">interface ClusterRoleList</a>
</h2>

ClusterRoleList is a collection of ClusterRoles

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18251">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18256">property items</a>
</h3>

```typescript
items: ClusterRole[];
```


Items is a list of ClusterRoles

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18264">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18269">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard object's metadata.

<h2 class="pdoc-module-header" id="PolicyRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18277">interface PolicyRule</a>
</h2>

PolicyRule holds information that describes a policy rule, but does not contain information
about who the rule applies to or which namespace the rule applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18283">property apiGroups</a>
</h3>

```typescript
apiGroups: string[];
```


APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups
are specified, any action requested against one of the enumerated resources in any API
group will be allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18292">property nonResourceURLs</a>
</h3>

```typescript
nonResourceURLs: string[];
```


NonResourceURLs is a set of partial urls that a user should have access to.  *s are
allowed, but only as the full, final step in the path Since non-resource URLs are not
namespaced, this field is only applicable for ClusterRoles referenced from a
ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets")
or non-resource URL paths (such as "/api"),  but not both.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18298">property resourceNames</a>
</h3>

```typescript
resourceNames: string[];
```


ResourceNames is an optional white list of names that the rule applies to.  An empty set
means that everything is allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18305">property resources</a>
</h3>

```typescript
resources: string[];
```


Resources is a list of resources this rule applies to.  '*' represents all resources in the
specified apiGroups. '*&#8205;/foo' represents the subresource 'foo' for all resources in
the specified apiGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18311">property verbs</a>
</h3>

```typescript
verbs: string[];
```


Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions
contained in this rule.  VerbAll represents all kinds.

<h2 class="pdoc-module-header" id="Role">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18319">interface Role</a>
</h2>

Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a
RoleBinding.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18326">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18334">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18339">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18344">property rules</a>
</h3>

```typescript
rules: PolicyRule[];
```


Rules holds all the PolicyRules for this Role

<h2 class="pdoc-module-header" id="RoleBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18354">interface RoleBinding</a>
</h2>

RoleBinding references a role, but does not contain it.  It can reference a Role in the same
namespace or a ClusterRole in the global namespace. It adds who information via Subjects and
namespace information by which namespace it exists in.  RoleBindings in a given namespace
only have effect in that namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18361">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18369">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18374">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18380">property roleRef</a>
</h3>

```typescript
roleRef: RoleRef;
```


RoleRef can reference a Role in the current namespace or a ClusterRole in the global
namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18385">property subjects</a>
</h3>

```typescript
subjects: Subject[];
```


Subjects holds references to the objects the role applies to.

<h2 class="pdoc-module-header" id="RoleBindingList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18392">interface RoleBindingList</a>
</h2>

RoleBindingList is a collection of RoleBindings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18399">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18404">property items</a>
</h3>

```typescript
items: RoleBinding[];
```


Items is a list of RoleBindings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18412">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18417">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard object's metadata.

<h2 class="pdoc-module-header" id="RoleList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18424">interface RoleList</a>
</h2>

RoleList is a collection of Roles

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18431">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18436">property items</a>
</h3>

```typescript
items: Role[];
```


Items is a list of Roles

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18444">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18449">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard object's metadata.

<h2 class="pdoc-module-header" id="RoleRef">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18456">interface RoleRef</a>
</h2>

RoleRef contains information that points to the role being used

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18460">property apiGroup</a>
</h3>

```typescript
apiGroup: string;
```


APIGroup is the group for the resource being referenced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18465">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is the type of resource being referenced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18470">property name</a>
</h3>

```typescript
name: string;
```


Name is the name of resource being referenced

<h2 class="pdoc-module-header" id="Subject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18479">interface Subject</a>
</h2>

Subject contains a reference to the object or user identities a role binding applies to.
This can either hold a direct API object reference, or a value for non-objects such as user
and group names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18484">property apiGroup</a>
</h3>

```typescript
apiGroup: string;
```


APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount
subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18491">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of object being referenced. Values defined by this API group are "User", "Group", and
"ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer
should report an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18496">property name</a>
</h3>

```typescript
name: string;
```


Name of the object being referenced.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L18502">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or
"Group", and this value is not empty the Authorizer should report an error.

