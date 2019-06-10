---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
---


One of the most common areas Kubernetes operators struggle with in
production involves creating and managing role-based access control
(RBAC). This is so daunting that RBAC is often not implemented, or
implemented halfway, or the configuration becomes impossible to
maintain. In this post, we will contrast the traditional way of working
with RBAC on EKS with using Pulumi --- Pulumi makes RBAC on Kubernetes
so easy that you'll never create an insecure cluster again!

##### Prerequisites to work with Pulumi:

-   [Install `pulumi`
    CLI ](https://pulumi.io/quickstart/install.html)and set up your [AWS
    credentials](https://pulumi.io/quickstart/aws/setup.html)
-   Initialize a new [Pulumi
    project](https://pulumi.io/reference/project.html) from available
    templates. We use `aws-typescript template` here to install all
    dependencies and save the configuration.

$ brew install pulumi *# download pulumi CLI*

$ pulumi new aws-typescript --dir eks-rbac *# create new pulumi
project and stack*

$ cd eks-rbac && ls -l *# check out all the configurations and node.js
dependencies installed*

-rw-r--r-- 1 nishidavidson staff 32 Apr 18 14:49 Pulumi.dev.yaml
-rw------- 1 nishidavidson staff 84 Apr 18 14:48 Pulumi.yaml
-rw------- 1 nishidavidson staff 273 Apr 18 14:48 index.ts
drwxr-xr-x 92 nishidavidson staff 2944 Apr 18 14:49 node_modules
-rw-r--r-- 1 nishidavidson staff 48352 Apr 18 14:49 package-lock.json
-rw------- 1 nishidavidson staff 228 Apr 18 14:48 package.json
-rw------- 1 nishidavidson staff 522 Apr 18 14:48 tsconfig.json 

With Pulumi, you will modify and update the default `index.ts` file
with AWS and EKS resource variable declarations. We show you how to add
this code as we contrast Pulumi's approach with the sequential
traditional approach in the steps below. In the end, you will do a
one-time run of `pulumi up` and watch all the steps in the Traditional
Way come alive simultaneously.

##### STEP 1: Create three IAM Roles with a Trust-policy to map to EKS RBAC.

###### The Traditional-approach:

You sequentially create three IAM roles (`clusterAdminRole`;
`AutomationRole`; `EnvProdRole`) with aws command line tool as shown
below:

 $ aws iam create-role --role-name clusterAdminRole
--assume-role-policy-document file://Role-Trust-Policy.json
{
"Role": {
"AssumeRolePolicyDocument": {
"Version": "2012-10-17",
"Statement": [
{
"Action": "sts:AssumeRole",
"Principal": {
"AWS": "arn:aws:iam::xxxxxxxxxxxx:root"
},
"Effect": "Allow",
"Sid": ""
}
]
},
"RoleId": "AROASHIVKXX3SFFMUUEU6",
"CreateDate": "2019-04-17T17:43:03Z",
"RoleName": "clusterAdminRole",
"Path": "/",
"Arn": "arn:aws:iam::xxxxxxxxxxxx:role/clusterAdminRole"
}
}

$ cat Role-Trust-Policy.json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": "sts:AssumeRole",
"Resource": "*"
}
]
}

###### The Pulumi-approach:

You update the default `index.ts` file in your source code editor such
as VSCode as follows:

import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

/*
* 1) Single step deployment of three IAM Roles
*/

function createIAMRole(name: string): aws.iam.Role {
// Create an IAM Role...
return new aws.iam.Role(`${name}`, {
assumeRolePolicy: `{
"Version": "2012-10-17",
"Statement":[
{
"Sid": "",
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::153052954103:root"
},
"Action": "sts:AssumeRole"
}
]
}
`,
tags: {
"clusterAccess": `${name}-usr`,
},
});
}

// Administrator AWS IAM clusterAdminRole with full access to all AWS
resources
const clusterAdminRole = createIAMRole("clusterAdminRole");
// Administer Automation role for use in pipelines, e.g. gitlab CI,
Teamcity, etc.
const AutomationRole = createIAMRole("AutomationRole");
// Administer Prod role for use in Prod environment
const EnvProdRole = createIAMRole("EnvProdRole"); 

##### STEP 2: Create one EKS cluster. Validate the cluster was created. Add the namespaces you need.

###### The Traditional-approach:

You go through the steps below to validate the cluster and k8s resource
deployment based on your tool chain and your understanding of
Kubernetes:

$ eksctl create cluster eks-nd-test`

$ kubectl get no
NAME STATUS ROLES AGE VERSION
ip-192-168-41-125.us-east-2.compute.internal Ready <none> 11h v1.11.5
ip-192-168-5-250.us-east-2.compute.internal Ready <none> 11h v1.11.5

$ kubectl create -f automation-ns.yaml && kubectl create -f
prod-ns.yaml

$ cat automation-ns.yaml

apiVersion: v1
kind: Namespace
metadata:
name: automation
labels:
name: automation

```

 

###### ###The Pulumi-approach:

You use our [[API
docs](https://www.google.com/url?q=https://pulumi.io/reference/pkg/nodejs/@pulumi/eks/index.html&sa=D&ust=1556085106572000)](https://pulumi.io/reference/pkg/nodejs/@pulumi/eks/index.html)
and your source-code editor to *autocomplete* the default `index.ts`
file.

function createNewNamespace(name: string): k8s.core.v1.Namespace {
//Create new namespace
return new k8s.core.v1.Namespace(name, { metadata: { name: name } }, {
provider: cluster.provider });
}

//declare namespaces automation and prod
const automation = createNewNamespace("automation");
const prod = createNewNamespace("prod");

######  

##### ##STEP 3: Understand Kubernetes RBAC. Declare the k8s YAMLs to the EKS cluster.

The Kubernetes RBAC API declares four top-level types that can be
defined as YAMLs syntaxes: *a)* Role - represents a set of additive
rules within a namespace; *b)* RoleBinding - grants namespace-wide
access to k8s subjects and resources; *c)* ClusterRole - represents a
set of additive rules within the cluster; *d)* ClusterRoleBinding -
grants cluster-wide access to k8s subjects and resources.

###### ###The Traditional-approach:

You define three k8s users with different privileges in your cluster and
test them sequentially:

 

User type1 called admin-usr for users have cluster admin rights

User type2 called automation-usr for users that have permissions to all
k8s resources in namespace automation. An e.g would be your CI/CD
pipeline

User type 3 called prod-usr for users that have read access to all k8s
resources in the namespace prod

$ cat user1.yaml

kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: ClusterAdminRole
# no namespace needed
rules:
- apiGroups: ["*"]
resources: ["*"]
verbs: ["*"]

 

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: cluster-admin-binding
subjects:
- kind: User
name: "pulumi:admin-usr"
apiGroup: rbac.authorization.k8s.io
roleRef:
kind: ClusterRole
name: ClusterAdminRole
apiGroup: rbac.authorization.k8s.io

$ cat user2.yaml

kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: AutomationRole
namespace: automation
rules:
- apiGroups: ["*"]
resources: ["*"]
verbs: ["*"]

 

---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: automation-binding
namespace: automation
subjects:
- kind: User
name: "pulumi:automation-usr"
apiGroup: rbac.authorization.k8s.io
roleRef:
kind: Role
name: AutomationRole
apiGroup: rbac.authorization.k8s.io

$ cat user3.yaml

kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: EnvProdRole
namespace: prod
rules:
- apiGroups: ["*"]
resources: ["*"]
verbs: ["get", "list", "watch"]

---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: env-prod-binding

namespace: prod
subjects:
- kind: User
name: "pulumi:prod-usr"
apiGroup: rbac.authorization.k8s.io
roleRef:
kind: Role
name: EnvProdRole
apiGroup: rbac.authorization.k8s.io

######  

```bash

$ kubectl apply -f user1.yaml && kubectl apply -f user2.yaml && kubectl
apply -f user3.yaml

clusterrole.rbac.authorization.k8s.io/ClusterAdminRole created
clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-binding
created
role.rbac.authorization.k8s.io/AutomationRole created
rolebinding.rbac.authorization.k8s.io/automation created
role.rbac.authorization.k8s.io/EnvProdRole created
rolebinding.rbac.authorization.k8s.io/env-prod-binding created

```

 

###### ###The Pulumi-approach:

Update your `index.ts` file with more code as follows:

```typescript

/*
* 3) Single Step deployment of k8s RBAC configuration for user1, user2
and user3 per our example
*/

// User1 - Grant cluster admin access to all admins
new k8s.rbac.v1.ClusterRole("clusterAdminRole", {
metadata: {
name: "clusterAdminRole",
},
rules: [{
apiGroups: ["*"],
resources: ["*"],
verbs: ["*"],
}]
}, {provider: cluster.provider});
new k8s.rbac.v1.ClusterRoleBinding("cluster-admin-binding", {
metadata: {
name: "cluster-admin-binding",
},
subjects: [{
kind: "User",
name: "pulumi:admin-usr",
}],
roleRef: {
kind: "ClusterRole",
name: "clusterAdminRole",
apiGroup: "rbac.authorization.k8s.io",
},
}, {provider: cluster.provider});

// User2 called automation-usr for users with permissions to all k8s
resources in namespace automation
new k8s.rbac.v1.Role("AutomationRole", {
metadata: {
name: "AutomationRole",
},
rules: [{
apiGroups: ["*"],
resources: ["*"],
verbs: ["*"],
}]
}, {provider: cluster.provider});
new k8s.rbac.v1.RoleBinding("automation-binding", {
metadata: {
name: "automation-binding",
},
subjects: [{
kind: "User",
name: "pulumi:automation-usr",
}],
roleRef: {
kind: "Role",
name: "AutomationRole",
apiGroup: "rbac.authorization.k8s.io",
},
}, {provider: cluster.provider});

// User3 called prod-usr for users with read access to all k8s resources
in namespace env-prod
new k8s.rbac.v1.Role("EnvProdRole", {
metadata: {
name: "EnvProdRole",
},
rules: [{
apiGroups: ["*"],
resources: ["*"],
verbs: ["get", "watch", "list"],
}],
}, {provider: cluster.provider});
new k8s.rbac.v1.RoleBinding("env-prod-binding", {
metadata: {
name: "env-prod-binding",
},
subjects: [{
kind: "User",
name: "pulumi:prod-usr",
}],
roleRef: {
kind: "Role",
name: "EnvProdRole",
apiGroup: "rbac.authorization.k8s.io",
},
}, {provider: cluster.provider});

```

######  

##### ##STEP 4: Update aws-iam-authenticator ConfigMap to map three IAM Roles to three k8s usernames.

###### *###The Traditional-approach:*

You get the three IAM role arns for `clusterAdminRole`,
`AutomationRole`, `EnvProdRole` and update the configmap with k8s
usernames `pulumi:admin-usr`, `pulumi:automation-usr` and
`pulumi:prod-usr`.

```yaml

mapRoles:
----
- groups:
- system:masters
rolearn: arn:aws:iam::XXXXXXXXXXXX:role/clusterAdminRole

username: pulumi:admin-usr
- groups:
rolearn: arn:aws:iam::XXXXXXXXXXXX:role/AutomationRole

username: pulumi:automation-usr
- groups:
rolearn: arn:aws:iam::XXXXXXXXXXXX:role/EnvProdRole

username: pulumi:prod-usr
- groups:
- system:bootstrappers
- system:nodes
rolearn:
arn:aws:iam::XXXXXXXXXXXX:role/eksctl-eks-rbac-nd-test-nodegroup-NodeInstanceRole-NP542EG8JX8U
username: system:node:

```

 

###### ###*The Pulumi-approach:*

This step is not required as you have already updated the EKS ConfigMap
at cluster creation time in *STEP 2* using "RoleMappings". Simply run
`pulumi up` with the full `index.ts` file. Watch all your components
come alive simultaneously.

Setting up RBAC on one EKS cluster is a long convoluted sequential
process that requires multiple validations along the way. Imagine the
complexity involved when working with multiple tools for an environment
that requires multiple groups with many users, namespaces, and clusters.

##### ##The Traditional-approach: Customer *NIGHTMARES*!

-   *YAML APOCALYPSE!* The YAML configurations that this increased
    scale inevitably requires becomes cumbersome for most operators.
-   *CHANGE -- YIKES!* Changing a `roleRef` in a `RoleBinding`,
    involves deleting the previous `RoleBinding` and creating a new
    one.
-   *WORKFLOW AUTOMATION:* In workflows driven by automation, where
    infrastructure as code is often seen as the gold standard, this
    doesn't fit in very well.
-   *RBAC AT SCALE:* Auditing and managing the current users to see
    what access they have across one or multiple clusters is hard. You
    can't just delete a `RoleBinding` from a repo and hope for some
    kind of automated task to manage the change for you.

##### ##The Pulumi-approach: Customer Benefits:

-   *NO MORE YAMLs!* Configuring YAMLs, operators or custom resources
    is now a thing in the past! You use Typescript or Javascript
    [[d]](../../../com/pulumi/blog/index.html)[[e]](../../../com/pulumi/blog/index.html)[[f]](../../../com/pulumi/blog/index.html)[[g]](../../../com/pulumi/blog/index.html)[[h]](../../../com/pulumi/blog/index.html)to
    program directly with our cloud SDK and connect all cloud services
    to your Kubernetes services with a simple reference to the object in
    your program.
-   *INCREASED DEVELOPMENT VELOCITY:* You intuitively program
    Kubernetes objects with our SDK abstractions using minimal amount of
    code within hours instead of months. You "autocomplete" AWS, EKS,
    Kubernetes specifications within your IDE without understanding the
    entire API.
-   *EASY UPDATES:* You change deployed k8s resources on one or
    multiple clusters by updating your typescript file `index.ts` and
    running `pulumi up`.The [Pulumi
    console](https://app.pulumi.com/) allows you to share your stack
    with your team in your GitHub, GitLab, or Atlassian-based
    organization.
-   *WORKFLOW AUTOMATION FOR RBAC AT SCALE:* You can delete or update
    multiple `RoleBindings or Roles` from your Pulumi stack source
    code. As you commit these changes to your repository, you can plan
    automated triggers that
    validate[[i]](../../../com/pulumi/blog/index.html)[[j]](../../../com/pulumi/blog/index.html)[[k]](../../../com/pulumi/blog/index.html)[[l]](../../../com/pulumi/blog/index.html)
    such changes as part of your CI/CD flow, whether you use
    [Travis](https://pulumi.io/reference/cd-travis.html),
    [CircleCI](https://pulumi.io/reference/cd-circleci.html),
    [AzureDevOps](https://pulumi.io/reference/cd-azure-devops.html),
    etc. Pulumi even has a [GitHub
    Application](https://pulumi.io/reference/cd-github.html) for
    surfacing results within pull requests.

In this post, we discussed how setting up Kubernetes RBAC with Pulumi is
simple, comprehensive,

non-sequential and part of your everyday programming experience instead
of being a YAML and DSL tool chain drudgery. You can find the complete
pulumi code for our example
[here](https://gist.github.com/d-nishi/a4e54dfc973ea047ec46c8deb5193f4e).
For more examples visit our GitHub examples page
[here](https://github.com/pulumi/examples).

 

[[a]](../../../com/pulumi/blog/index.html)+nishi@pulumi.com not a big
deal, but since there is so much overlap in the policy definitions, what
do you think of creating the resource inside of a function. And then
just parameterize it on the things that are truly different?

function createKubernetesRole(name) {
// Create an IAM Role...
new aws.iam.Role(`kubernetesRole-${name}`, {
...
}

createKubernetesRole("admin-usr");
createKubernetesRole("automation-usr");
createKubernetesRole("prod-usr");


That might go a very long way towards cleaning this section up -- and
highlight the advantage of using real code for your infrastructure :)

[[b]](../../../com/pulumi/blog/index.html)I can do this for only this
section - so am testing 1 last time before releasing.

[[c]](../../../com/pulumi/blog/index.html)done - it worked.

[[d]](../../../com/pulumi/blog/index.html)Could be good to add "...
(or one of the other great languages Pulumi supports)..."

[[e]](../../../com/pulumi/blog/index.html)Unless there's a limitation
of supporting k8s with our other languages?

[[f]](../../../com/pulumi/blog/index.html)currently only Typescript
and Javascript is supported :(

[[g]](../../../com/pulumi/blog/index.html)Python should work also?

[[h]](../../../com/pulumi/blog/index.html)we dont have python support
for EKS right now.

[[i]](../../../com/pulumi/blog/index.html)Perhaps simplify this to
"... the next time you deploy your Pulumi program, that change will be
applied". The "pan for" and "automated task to validate" don't
quite make sense to me.

[[j]](../../../com/pulumi/blog/index.html)+chris@pulumi.com -
reworded this. I know we have nothing yet. What do you think of this?

[[k]](../../../com/pulumi/blog/index.html)Maybe plug our GitHub App?
https://pulumi.io/reference/cd-github.html

[[l]](../../../com/pulumi/blog/index.html)Done.

