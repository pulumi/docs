---
title: Module authentication/v1beta1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">authentication</a> &gt; v1beta1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#TokenReview">interface TokenReview</a>
* <a href="#TokenReviewSpec">interface TokenReviewSpec</a>
* <a href="#TokenReviewStatus">interface TokenReviewStatus</a>
* <a href="#UserInfo">interface UserInfo</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="TokenReview">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3976">interface TokenReview</a>
</h2>

TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may
be cached by the webhook token authenticator plugin in the kube-apiserver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3983">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3991">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3994">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L3999">property spec</a>
</h3>

```typescript
spec: TokenReviewSpec;
```


Spec holds information about the request being evaluated

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4004">property status</a>
</h3>

```typescript
status: TokenReviewStatus;
```


Status is filled in by the server and indicates whether the request can be authenticated.

<h2 class="pdoc-module-header" id="TokenReviewSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4011">interface TokenReviewSpec</a>
</h2>

TokenReviewSpec is a description of the token authentication request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4015">property token</a>
</h3>

```typescript
token: string;
```


Token is the opaque bearer token.

<h2 class="pdoc-module-header" id="TokenReviewStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4022">interface TokenReviewStatus</a>
</h2>

TokenReviewStatus is the result of the token authentication request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4026">property authenticated</a>
</h3>

```typescript
authenticated: boolean;
```


Authenticated indicates that the token was associated with a known user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4031">property error</a>
</h3>

```typescript
error: string;
```


Error indicates that the token couldn't be checked

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4036">property user</a>
</h3>

```typescript
user: UserInfo;
```


User is the UserInfo associated with the provided token.

<h2 class="pdoc-module-header" id="UserInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4043">interface UserInfo</a>
</h2>

UserInfo holds the information about the user needed to implement the user.Info interface.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4047">property extra</a>
</h3>

```typescript
extra: object;
```


Any additional information provided by the authenticator.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4052">property groups</a>
</h3>

```typescript
groups: string[];
```


The names of groups this user is a part of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4058">property uid</a>
</h3>

```typescript
uid: string;
```


A unique value that identifies this user across time. If this user is deleted and another
user by the same name is added, they will have different UIDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L4063">property username</a>
</h3>

```typescript
username: string;
```


The name that uniquely identifies this user among all active users.

