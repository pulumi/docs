---
title: Module authorization/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">authorization</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isLocalSubjectAccessReview">function isLocalSubjectAccessReview</a>
* <a href="#isSelfSubjectAccessReview">function isSelfSubjectAccessReview</a>
* <a href="#isSelfSubjectRulesReview">function isSelfSubjectRulesReview</a>
* <a href="#isSubjectAccessReview">function isSubjectAccessReview</a>
* <a href="#LocalSubjectAccessReview">interface LocalSubjectAccessReview</a>
* <a href="#NonResourceAttributes">interface NonResourceAttributes</a>
* <a href="#NonResourceRule">interface NonResourceRule</a>
* <a href="#ResourceAttributes">interface ResourceAttributes</a>
* <a href="#ResourceRule">interface ResourceRule</a>
* <a href="#SelfSubjectAccessReview">interface SelfSubjectAccessReview</a>
* <a href="#SelfSubjectAccessReviewSpec">interface SelfSubjectAccessReviewSpec</a>
* <a href="#SelfSubjectRulesReview">interface SelfSubjectRulesReview</a>
* <a href="#SelfSubjectRulesReviewSpec">interface SelfSubjectRulesReviewSpec</a>
* <a href="#SubjectAccessReview">interface SubjectAccessReview</a>
* <a href="#SubjectAccessReviewSpec">interface SubjectAccessReviewSpec</a>
* <a href="#SubjectAccessReviewStatus">interface SubjectAccessReviewStatus</a>
* <a href="#SubjectRulesReviewStatus">interface SubjectRulesReviewStatus</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isLocalSubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5107">function isLocalSubjectAccessReview</a>
</h2>

```typescript
isLocalSubjectAccessReview(o: any): boolean
```

<h2 class="pdoc-module-header" id="isSelfSubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5268">function isSelfSubjectAccessReview</a>
</h2>

```typescript
isSelfSubjectAccessReview(o: any): boolean
```

<h2 class="pdoc-module-header" id="isSelfSubjectRulesReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5332">function isSelfSubjectRulesReview</a>
</h2>

```typescript
isSelfSubjectRulesReview(o: any): boolean
```

<h2 class="pdoc-module-header" id="isSubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L5381">function isSubjectAccessReview</a>
</h2>

```typescript
isSubjectAccessReview(o: any): boolean
```

<h2 class="pdoc-module-header" id="LocalSubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4793">interface LocalSubjectAccessReview</a>
</h2>

LocalSubjectAccessReview checks whether or not a user or group can perform an action in a
given namespace. Having a namespace scoped resource makes it much easier to grant namespace
scoped policy that includes permissions checking.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4800">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4808">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4811">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4817">property spec</a>
</h3>

```typescript
spec: SubjectAccessReviewSpec;
```


Spec holds information about the request being evaluated.  spec.namespace must be equal to
the namespace you made the request against.  If empty, it is defaulted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4822">property status</a>
</h3>

```typescript
status: SubjectAccessReviewStatus;
```


Status is filled in by the server and indicates whether the request is allowed or not

<h2 class="pdoc-module-header" id="NonResourceAttributes">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4830">interface NonResourceAttributes</a>
</h2>

NonResourceAttributes includes the authorization attributes available for non-resource
requests to the Authorizer interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4834">property path</a>
</h3>

```typescript
path: string;
```


Path is the URL path of the request

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4839">property verb</a>
</h3>

```typescript
verb: string;
```


Verb is the standard HTTP verb

<h2 class="pdoc-module-header" id="NonResourceRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4846">interface NonResourceRule</a>
</h2>

NonResourceRule holds information that describes a rule for the non-resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4851">property nonResourceURLs</a>
</h3>

```typescript
nonResourceURLs: string[];
```


NonResourceURLs is a set of partial urls that a user should have access to.  *s are
allowed, but only as the full, final step in the path.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4857">property verbs</a>
</h3>

```typescript
verbs: string[];
```


Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch,
head, options.  "*" means all.

<h2 class="pdoc-module-header" id="ResourceAttributes">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4865">interface ResourceAttributes</a>
</h2>

ResourceAttributes includes the authorization attributes available for resource requests to
the Authorizer interface

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4869">property group</a>
</h3>

```typescript
group: string;
```


Group is the API Group of the Resource.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4875">property name</a>
</h3>

```typescript
name: string;
```


Name is the name of the resource being requested for a "get" or deleted for a "delete". ""
(empty) means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4883">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace is the namespace of the action being requested.  Currently, there is no
distinction between no namespace and all namespaces "" (empty) is defaulted for
LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means
"all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4888">property resource</a>
</h3>

```typescript
resource: string;
```


Resource is one of the existing resource types.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4893">property subresource</a>
</h3>

```typescript
subresource: string;
```


Subresource is one of the existing resource types.  "" means none.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4899">property verb</a>
</h3>

```typescript
verb: string;
```


Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete,
proxy.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4904">property version</a>
</h3>

```typescript
version: string;
```


Version is the API Version of the Resource.  "*" means all.

<h2 class="pdoc-module-header" id="ResourceRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4912">interface ResourceRule</a>
</h2>

ResourceRule is the list of actions the subject is allowed to perform on resources. The list
ordering isn't significant, may contain duplicates, and possibly be incomplete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4918">property apiGroups</a>
</h3>

```typescript
apiGroups: string[];
```


APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups
are specified, any action requested against one of the enumerated resources in any API
group will be allowed.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4924">property resourceNames</a>
</h3>

```typescript
resourceNames: string[];
```


ResourceNames is an optional white list of names that the rule applies to.  An empty set
means that everything is allowed.  "*" means all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4932">property resources</a>
</h3>

```typescript
resources: string[];
```


Resources is a list of resources this rule applies to.  "*" means all in the specified
apiGroups.
 "*&#8205;/foo" represents the subresource 'foo' for all resources in the specified
apiGroups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4938">property verbs</a>
</h3>

```typescript
verbs: string[];
```


Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update,
delete, proxy.  "*" means all.

<h2 class="pdoc-module-header" id="SelfSubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4947">interface SelfSubjectAccessReview</a>
</h2>

SelfSubjectAccessReview checks whether or the current user can perform an action.  Not
filling in a spec.namespace means "in all namespaces".  Self is a special case, because users
should always be able to check whether they can perform an action

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4954">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4962">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4965">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4970">property spec</a>
</h3>

```typescript
spec: SelfSubjectAccessReviewSpec;
```


Spec holds information about the request being evaluated.  user and groups must be empty

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4975">property status</a>
</h3>

```typescript
status: SubjectAccessReviewStatus;
```


Status is filled in by the server and indicates whether the request is allowed or not

<h2 class="pdoc-module-header" id="SelfSubjectAccessReviewSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4983">interface SelfSubjectAccessReviewSpec</a>
</h2>

SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of
ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4987">property nonResourceAttributes</a>
</h3>

```typescript
nonResourceAttributes: NonResourceAttributes;
```


NonResourceAttributes describes information for a non-resource access request

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4992">property resourceAttributes</a>
</h3>

```typescript
resourceAttributes: ResourceAttributes;
```


ResourceAuthorizationAttributes describes information for a resource access request

<h2 class="pdoc-module-header" id="SelfSubjectRulesReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5006">interface SelfSubjectRulesReview</a>
</h2>

SelfSubjectRulesReview enumerates the set of actions the current user can perform within a
namespace. The returned list of actions may be incomplete depending on the server's
authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview
should be used by UIs to show/hide actions, or to quickly let an end user reason about their
permissions. It should NOT Be used by external systems to drive authorization decisions as
this raises confused deputy, cache lifetime/revocation, and correctness concerns.
SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization
decisions to the API server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5013">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5021">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5024">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5029">property spec</a>
</h3>

```typescript
spec: SelfSubjectRulesReviewSpec;
```


Spec holds information about the request being evaluated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5034">property status</a>
</h3>

```typescript
status: SubjectRulesReviewStatus;
```


Status is filled in by the server and indicates the set of actions a user can perform.

<h2 class="pdoc-module-header" id="SelfSubjectRulesReviewSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5039">interface SelfSubjectRulesReviewSpec</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5043">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace to evaluate rules for. Required.

<h2 class="pdoc-module-header" id="SubjectAccessReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5050">interface SubjectAccessReview</a>
</h2>

SubjectAccessReview checks whether or not a user or group can perform an action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5057">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5065">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5068">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5073">property spec</a>
</h3>

```typescript
spec: SubjectAccessReviewSpec;
```


Spec holds information about the request being evaluated

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5078">property status</a>
</h3>

```typescript
status: SubjectAccessReviewStatus;
```


Status is filled in by the server and indicates whether the request is allowed or not

<h2 class="pdoc-module-header" id="SubjectAccessReviewSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5086">interface SubjectAccessReviewSpec</a>
</h2>

SubjectAccessReviewSpec is a description of the access request.  Exactly one of
ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5091">property extra</a>
</h3>

```typescript
extra: object;
```


Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is
input to the authorizer it needs a reflection here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5096">property group</a>
</h3>

```typescript
group: string[];
```


Groups is the groups you're testing for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5101">property nonResourceAttributes</a>
</h3>

```typescript
nonResourceAttributes: NonResourceAttributes;
```


NonResourceAttributes describes information for a non-resource access request

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5106">property resourceAttributes</a>
</h3>

```typescript
resourceAttributes: ResourceAttributes;
```


ResourceAuthorizationAttributes describes information for a resource access request

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5111">property uid</a>
</h3>

```typescript
uid: string;
```


UID information about the requesting user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5117">property user</a>
</h3>

```typescript
user: string;
```


User is the user you're testing for. If you specify "User" but not "Group", then is it
interpreted as "What if User were not a member of any groups

<h2 class="pdoc-module-header" id="SubjectAccessReviewStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5124">interface SubjectAccessReviewStatus</a>
</h2>

SubjectAccessReviewStatus

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5128">property allowed</a>
</h3>

```typescript
allowed: boolean;
```


Allowed is required. True if the action would be allowed, false otherwise.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5135">property denied</a>
</h3>

```typescript
denied: boolean;
```


Denied is optional. True if the action would be denied, otherwise false. If both allowed is
false and denied is false, then the authorizer has no opinion on whether to authorize the
action. Denied may not be true if Allowed is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5143">property evaluationError</a>
</h3>

```typescript
evaluationError: string;
```


EvaluationError is an indication that some error occurred during the authorization check.
It is entirely possible to get an error and be able to continue determine authorization
status in spite of it. For instance, RBAC can be missing a role, but enough roles are still
present and bound to reason about the request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5148">property reason</a>
</h3>

```typescript
reason: string;
```


Reason is optional.  It indicates why a request was allowed or denied.

<h2 class="pdoc-module-header" id="SubjectRulesReviewStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5158">interface SubjectRulesReviewStatus</a>
</h2>

SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete
depending on the set of authorizers the server is configured with and any errors experienced
during evaluation. Because authorization rules are additive, if a rule appears in a list it's
safe to assume the subject has that permission, even if that list is incomplete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5164">property evaluationError</a>
</h3>

```typescript
evaluationError: string;
```


EvaluationError can appear in combination with Rules. It indicates an error occurred during
rule evaluation, such as an authorizer that doesn't support rule evaluation, and that
ResourceRules and/or NonResourceRules may be incomplete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5171">property incomplete</a>
</h3>

```typescript
incomplete: boolean;
```


Incomplete is true when the rules returned by this call are incomplete. This is most
commonly encountered when an authorizer, such as an external authorizer, doesn't support
rules evaluation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5177">property nonResourceRules</a>
</h3>

```typescript
nonResourceRules: NonResourceRule[];
```


NonResourceRules is the list of actions the subject is allowed to perform on non-resources.
The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L5183">property resourceRules</a>
</h3>

```typescript
resourceRules: ResourceRule[];
```


ResourceRules is the list of actions the subject is allowed to perform on resources. The
list ordering isn't significant, may contain duplicates, and possibly be incomplete.

