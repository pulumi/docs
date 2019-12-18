---
title: "Kubernetes RBAC in AWS EKS with open source Pulumi packages"
h1: "Simplify Kubernetes RBAC in Amazon EKS with open source Pulumi packages"
authors: ["nishi-davidson"]
tags: ["AWS","Kubernetes","TypeScript","EKS"]
date: "2019-04-24"
meta_desc: "This post contrasts the traditional approach with Pulumi's modern method for simplifying Kubernetes RBAC in Amazon EKS."
---

One of the most common areas Kubernetes operators struggle with in
production involves creating and managing role-based access control
(RBAC). This is so daunting that RBAC is often not implemented, or
implemented halfway, or the configuration becomes impossible to
maintain.

Fortunately, Pulumi makes RBAC on Kuberenetes so easy that you'll never create an insecure cluster again. In this post, we will contrast the traditional way of working
with RBAC on EKS with using Pulumi.
<!--more-->

Here are a few highlights:

- **NO MORE YAMLs!** Configuring YAMLs, operators or custom resources
  is now a thing in the past! You use TypeScript or JavaScript to
  program directly with our cloud SDK and connect all cloud services
  to your Kubernetes services with a simple reference to the object in
  your program.
- **INCREASED DEVELOPMENT VELOCITY:** You intuitively program
  Kubernetes objects with our SDK abstractions using minimal amount of
  code within hours instead of months. You "autocomplete" AWS, EKS,
  Kubernetes specifications within your IDE without understanding the
  entire API.
- **EASY UPDATES:** Changing a `roleRef` in a `RoleBinding`, on one or
  multiple clusters involves updating your TypeScript file `index.ts`
  and running `pulumi up`. The Pulumi console allows you to share your
  stack with your team in your GitHub, GitLab, or Atlassian-based
  organization.
- **WORKFLOW AUTOMATION FOR RBAC AT SCALE:** You can delete or update
  multiple `RoleBindings or Roles` from your Pulumi stack source code.
  As you commit these changes to your repository, you can plan
  automated triggers that validate such changes as part of your CI/CD
  flow, whether you use Travis, CircleCI, AzureDevOps and more. Pulumi
  even has a GitHub Application for surfacing results within pull
  requests.

## Prerequisites to work with Pulumi

[Install `pulumi` CLI]({{< ref "/docs/get-started/install" >}}) and
set up your
[AWS credentials]({{< ref "/docs/get-started/aws" >}}).
Initialize a new
[Pulumi project]({{< ref "/docs/intro/concepts/project" >}}) from available
templates. We use `aws-typescript template` here to install all
dependencies and save the configuration.

    $ brew install pulumi # download pulumi CLI

    $ mkdir eks-rbac && cd eks-rbac

    $ pulumi new aws-typescript

    $ ls -l
    -rw-r--r--   1 nishidavidson  staff     32 Apr 18 14:49 Pulumi.dev.yaml
    -rw-------   1 nishidavidson  staff     84 Apr 18 14:48 Pulumi.yaml
    -rw-------   1 nishidavidson  staff    273 Apr 18 14:48 index.ts
    drwxr-xr-x  92 nishidavidson  staff   2944 Apr 18 14:49 node_modules
    -rw-r--r--   1 nishidavidson  staff  48352 Apr 18 14:49 package-lock.json
    -rw-------   1 nishidavidson  staff    228 Apr 18 14:48 package.json
    -rw-------   1 nishidavidson  staff    522 Apr 18 14:48 tsconfig.json

With Pulumi, you will modify and update the default `index.ts` file with
AWS and EKS resource variable declarations. We show you how to add this
code as we contrast Pulumi's approach with the sequential traditional
approach in the steps below. In the end, you will do a one-time run of
`pulumi up` and watch all the steps in the Traditional Way come alive
simultaneously.

## Step 1: Create three IAM Roles with a Trust-policy to map to Amazon EKS RBAC.

### The Traditional-approach:

You sequentially create three IAM roles (`clusterAdminRole`;
`AutomationRole`; `EnvProdRole`) with aws command line tool as shown
below:

    $ aws iam create-role --role-name clusterAdminRole --assume-role-policy-document file://Role-Trust-Policy.json
     
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

### The Pulumi-approach:

You update the default `index.ts` file in your source code editor such
as VSCode as follows:

```typescript
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
    };
}

// Administrator AWS IAM clusterAdminRole with full access to all AWS resources
const clusterAdminRole = createIAMRole("clusterAdminRole");

// Administer Automation role for use in pipelines, e.g. gitlab CI, Teamcity, etc.
const AutomationRole = createIAMRole("AutomationRole");

// Administer Prod role for use in Prod environment
const EnvProdRole = createIAMRole("EnvProdRole");
```

## Step 2: Create one EKS cluster. Validate cluster creation. Add the namespaces you need.

### The Traditional-approach:

You go through the steps below to validate the cluster and k8s resource
deployment based on your tool chain and your understanding of
Kubernetes:

    $ eksctl create cluster eks-nd-test
     
    $ kubectl get no
    NAME                                           STATUS   ROLES    AGE   VERSION
    ip-192-168-41-125.us-east-2.compute.internal   Ready    <none>   11h   v1.11.5
    ip-192-168-5-250.us-east-2.compute.internal    Ready    <none>   11h   v1.11.5
     
    $ kubectl create -f automation-ns.yaml && kubectl create -f prod-ns.yaml
     
    $ cat automation-ns.yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: automation
      labels:
        name: automation

### The Pulumi-approach:

You use our API docs and your source-code editor to autocomplete the
default `index.ts` file.

```typescript
/*
    * 2) Single step deployment of EKS cluster with the most important variables and a Simple Function to create namespaces
    * automation and prod
    */

const vpc = new awsx.Network("vpc", { usePrivateSubnets: false });
const cluster = new eks.Cluster("eks-cluster", {
  vpcId             : vpc.vpcId,
  subnetIds         : vpc.publicSubnetIds,
  instanceType      : "t2.medium",
  nodeRootVolumeSize: 200,
  desiredCapacity   : 1,
  maxSize           : 2,
  minSize           : 1,
  deployDashboard   : false,
  vpcCniOptions     : {
    warmIpTarget    : 4,
  },
  roleMappings      : [
    // Provides full administrator cluster access to the k8s cluster
    {
      groups    : ["system:masters"],
      roleArn   : clusterAdminRole.arn,
      username  : "pulumi:admin-usr",
    },
    // Map IAM role arn "AutomationRoleArn" to the k8s user with name "automation-usr", e.g. gitlab CI
    {
      groups    : ["pulumi:automation-grp"],
      roleArn   : AutomationRole.arn,
      username  : "pulumi:automation-usr",
    },
    // Map IAM role arn "EnvProdRoleArn" to the k8s user with name "prod-usr"
    {
      groups    : ["pulumi:prod-grp"],
      roleArn   : EnvProdRole.arn,
      username  : "pulumi:prod-usr",
    },
  ],
});

export const clusterName = cluster.eksCluster.name;

function createNewNamespace(name: string): k8s.core.v1.Namespace {
  // Create new namespace
  return new k8s.core.v1.Namespace(name, { metadata: { name: name } }, { provider: cluster.provider });
}

// Declare namespaces automation and prod.
const automation = createNewNamespace("automation");
const prod = createNewNamespace("prod");
```

## Step 3: Understand Kubernetes RBAC. Declare the Kubernetes objects on the EKS cluster.

The Kubernetes RBAC API declares four top-level types that can be
defined as YAMLs syntaxes: **a) Role** - represents a set of additive
rules within a namespace; **b) RoleBinding** - grants namespace-wide
access to k8s subjects and resources; **c) ClusterRole** - represents a
set of additive rules within the cluster; **d) ClusterRoleBinding** -
grants cluster-wide access to k8s subjects and resources.

### The Traditional-approach:

You define three k8s users with different privileges in your cluster and
test them sequentially:
User type1 called `pulumi:admin-usr` for users have cluster admin rights

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
      apiGroup: rbac.authorization.k8s.io`

User type2 called `pulumi:automation-usr` for users that have
permissions to all k8s resources in namespace automation. An e.g would
be your CI/CD pipeline

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

User type 3 called prod-usr for users that have read access to all k8s
resources in the namespace prod

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
      apiGroup: rbac.authorization.k8s.io`

    $ kubectl apply -f user1.yaml && kubectl apply -f user2.yaml && kubectl apply -f user3.yaml`
     
    clusterrole.rbac.authorization.k8s.io/ClusterAdminRole created
    clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-binding created
    role.rbac.authorization.k8s.io/AutomationRole created
    rolebinding.rbac.authorization.k8s.io/automation created
    role.rbac.authorization.k8s.io/EnvProdRole created
    rolebinding.rbac.authorization.k8s.io/env-prod-binding created

### The Pulumi-approach:

Update your `index.ts` file with more code as follows:

```typescript
/*
 * 3) Single Step deployment of k8s RBAC configuration for user1, user2 and user3 per our example
 */

// Grant cluster admin access to all admins with k8s ClusterRole and ClusterRoleBinding
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

// User2 called automation-usr for users that have permissions to all k8s resources in the namespace automation
new k8s.rbac.v1.Role("AutomationRole", {
  metadata: {
    name: "AutomationRole",
    namespace: "automation",
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
    namespace: "automation",
  },
  subjects: [{
     kind: "User",
     name: "pulumi:automation-usr",
     apiGroup: "rbac.authorization.k8s.io",
  }],
  roleRef: {
    kind: "Role",
    name: "AutomationRole",
    apiGroup: "rbac.authorization.k8s.io",
  },
}, {provider: cluster.provider});

// User3 called prod-usr for users that have read access to all k8s resources in the namespace env-prod
new k8s.rbac.v1.Role("EnvProdRole", {
  metadata: {
    name: "EnvProdRole",
    namespace: "prod",
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
    namespace: "prod",
  },
  subjects: [{
     kind: "User",
     name: "pulumi:prod-usr",
     apiGroup: "rbac.authorization.k8s.io",
    }],
  roleRef: {
    kind: "Role",
    name: "EnvProdRole",
    apiGroup: "rbac.authorization.k8s.io",
  },
}, {provider: cluster.provider});

export const kubeconfig = cluster.kubeconfig
```

## Step 4: Update aws-iam-authenticator ConfigMap to map the IAM Roles to the Kubernetes usernames.

### The Traditional-approach:

You get the three IAM role arns for `clusterAdminRole`,
`AutomationRole`, `EnvProdRole` and update the configmap with k8s
usernames `pulumi:admin-usr`, `pulumi:automation-usr` and
`pulumi:prod-usr`.

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
      rolearn: arn:aws:iam::XXXXXXXXXXXX:role/eksctl-eks-rbac-nd-test-nodegroup-NodeInstanceRole-NP542EG8JX8U
      username: system:node:`

### The Pulumi-approach:

This step is not required as you have already updated the EKS ConfigMap
at cluster creation time in STEP 2 using "RoleMappings". Simply run
`pulumi up` with the full `index.ts` file. Watch all your components
come alive simultaneously.
Setting up RBAC on one EKS cluster is a long convoluted sequential
process that requires multiple validations along the way. Imagine the
complexity involved when working with multiple tools for an environment
that requires multiple groups with many users, namespaces, and clusters.

#### **Testing the Pulumi approach worked**

Make sure you run `pulumi up` with this `index.ts`
[file](https://gist.github.com/d-nishi/ab462ea779e0615f29e8cfbb668272d7).

    $ pulumi stack output kubeconfig | jq > kubeconfig.yaml
    $ export KUBECONFIG = kubeconfig.yaml

Assume the IAM role `AutomationRole` with access to all Kubernetes
resources in namespace automation and test if the permissions work.

      "users": [
        {
          "name": "aws",
          "user": {
            "exec": {
              "apiVersion": "client.authentication.k8s.io/v1alpha1",
              "args": [
                "token",
                "-i",
                "eks-cluster-eksCluster-196b0de",
                "-r",
                "arn:aws:iam::xxxxxxxxxxxx:role/AutomationRole"
              ],
              "command": "aws-iam-authenticator"
            }
          }
        }
      ]
    }
     
    $ kubectl get po --namespace=automation
    No resources found.
     
    $ kubectl get po --namespace=prod
    Error from server (Forbidden): pods is forbidden: User "pulumi: automation-usr" cannot list resource "pods" in API group "" in the namespace "prod"

Upon assuming the IAM role `AutomationRole` which is mapped to
Kubernernetes username `pulumi:automation-usr` in the EKS cluster
configmap, you are only restricted to the resources and verbs allowed in
the namespace "automation" and not in namespace "prod".

## Next Step

In this post, we discussed how setting up Kubernetes RBAC with Pulumi is
simple, comprehensive,
non-sequential and part of your everyday programming experience. You can find the [complete pulumi code for our example](https://gist.github.com/d-nishi/a4e54dfc973ea047ec46c8deb5193f4e) and try it out yourself.

Pulumi is open source and free to use. For more examples, visit our GitHub examples page
[here](https://github.com/pulumi/examples). To learn more about Pulumi and how to manage Kubernetes through code, have a look at our ["Get Started with Kubernetes" guide]({{< ref "/docs/get-started/kubernetes" >}}).
