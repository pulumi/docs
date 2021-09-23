---
date: "2020-06-02"
title: "Access Control for Pods on Amazon EKS"
authors: ["mike-metral"]
tags: ["aws", "Kubernetes", "eks", "rbac"]
meta_desc: "Amazon EKS clusters can use IAM roles and policies for Pods to assign fine-grained access control of AWS services."
meta_image: cluster.png
---

Amazon [EKS][aws-eks] clusters can use [IAM][aws-iam] roles and policies for Pods
to assign fine-grained access control of AWS services. The AWS IAM entities map into Kubernetes
[RBAC][k8s-rbac] to configure the permissions of Pods that work with AWS
services.

Together, AWS IAM and Kubernetes RBAC enable least-privileged access for your
apps, scoped to the appropriate policies and user requirements.

[k8s-rbac]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/

<!--more-->

## Overview

In <100 lines of code we'll demonstrate how EKS Pods can use AWS IAM to create
fine-grained permissions for apps that integrate with other AWS services.

* [Pod Access Control](#pod-access-control)
* [Create an OIDC provider](#create-an-oidc-provider)
* [Create IAM for a S3 app](#create-iam-for-a-s3-app)
* [Deploy a S3 app](#deploy-a-s3-app)
* [Wrap-Up](#wrap-up)
* [Next Steps](#next-steps)

## Pod Access Control

AWS EKS supports using IAM entities in a Pod [Service Account][k8s-sa] by
leveraging an [OIDC provider][aws-oidc] connected to the Kubernetes cluster.

Continuing with the example from the [AWS blog post][aws-pod-iam], when an [S3 app written in Go][s3-app] pushes
an object to a bucket with the AWS SDK, it will need write access to S3.

When a Pod is launched with a particular Service Account, the OIDC provider works
with Kubernetes to verify the Pod's identity, and in turn collaborates with the
[AWS Secure Token Service (STS)][aws-sts] to grant the Pod temporary
credentials to use with the IAM role.

## Create an OIDC provider

Creating an OIDC provider is as simple as toggling the `createOidcProvider` option
in the definition of your EKS cluster.

When enabled, the OIDC provider will be created and associated with the
cluster's OIDC provider URL.

```typescript
import * as eks from '@pulumi/eks'

// Create an EKS cluster with default settings.
// Create and attach an OIDC provider to the cluster.
const cluster = new eks.Cluster('myCluster', {
      createOidcProvider: true,
});
```

## Create IAM for a S3 app

We'll use the OIDC provider URL and Amazon Resource Name (ARN) to compose the
[AssumeRoleWithWebIdentity][aws-assume-role-web], and S3 IAM policies that will
be attached to a new S3 IAM role.

After the role is configured, a Service Account for the S3 Pod will be
created, and annotated with the ARN of the S3 role to bind the two together.

```typescript
import * as aws from '@pulumi/aws'
import * as k8s from '@pulumi/kubernetes'
import * as pulumi from '@pulumi/pulumi'

// Create a pulumi Kubernetes provider using the cluster's kubeconfig.
const k8sProvider = new k8s.Provider('k8s', {
  kubeconfig: cluster.kubeconfig.apply(JSON.stringify),
});

// Create a k8s namespace in the cluster.
const namespace = new k8s.core.v1.Namespace('apps', undefined, { k8sProvider });

// Get the OIDC provider's URL for the cluster.
const clusterOidcProvider = cluster.core.oidcProvider.url;

// Create the new IAM policy for the Service Account using the AssumeRoleWebWebIdentity action.
const saName = 's3'
const saAssumeRolePolicy = pulumi
  .all([clusterOidcProviderUrl, clusterOidcProvider.arn, appsNamespaceName])
  .apply(([url, arn, namespace]) =>
    aws.iam.getPolicyDocument({
      statements: [
        {
          actions: ['sts:AssumeRoleWithWebIdentity'],
          conditions: [
            {
              test: 'StringEquals',
              values: [`system:serviceaccount:${namespace.metadata.name}:${saName}`],
              variable: `${url.replace('https://', '')}:sub`,
            },
          ],
          effect: 'Allow',
          principals: [{identifiers: [arn], type: 'Federated'}],
        },
      ],
    })
  );

// Create a new IAM role that assumes the AssumeRoleWebWebIdentity policy.
const saRole = new aws.iam.Role(saName, {
  assumeRolePolicy: saAssumeRolePolicy.json,
});

// Attach the IAM role to an AWS S3 access policy.
const saS3Rpa = new aws.iam.RolePolicyAttachment(saName, {
  policyArn: 'arn:aws:iam::aws:policy/AmazonS3FullAccess',
  role: saRole,
});

// Create a Service Account with the IAM role annotated to use with the Pod.
const sa = new k8s.core.v1.ServiceAccount(
  saName,
  {
    metadata: {
      namespace: namespace.metadata.name,
      name: saName,
      annotations: {
        'eks.amazonaws.com/role-arn': saRole.arn,
      },
    },
  },
  { k8sProvider });
```

## Deploy a S3 app

We'll deploy the [S3 app][peks-oidc] to use the new IAM-backed Service Account.

Once the Pod is running, the Service Account annotation will be automatically
managed by a [Kubernetes dynamic admission controller][k8s-dynamic-webhook] run
by EKS on your behalf.

The [AWS EKS webhook][eks-webhook] manages Pod identity, and injects STS
credentials into the Pod to use with the S3 role.

With the credentials, the app can successfully upload data to S3.

```typescript
import * as aws from "@pulumi/aws";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const bucket = new aws.s3.Bucket("pod-irsa-job-bucket");
const bucketName = bucket.id;
const regionName = pulumi.output(aws.getRegion({}, {async: true})).name;
const s3Pod = new k8s.core.v1.Pod(podName,
    {
        metadata: {labels: labels, namespace: appsNamespaceName},
        spec: {
            serviceAccountName: sa.metadata.name,
            containers: [
                {
                    name: podName,
                    image: "amazonlinux:2018.03",
                    command: ["sh", "-c",
                        pulumi.interpolate`curl -sL -o /s3-echoer https://git.io/JfnGX && chmod +x /s3-echoer && echo This is an in-cluster test | /s3-echoer ${bucketName} && sleep 3600`,
                    ],
                    env: [
                        {name: "AWS_DEFAULT_REGION", value: regionName},
                        {name: "ENABLE_IRP", value: "true"},
                    ],
                },
            ],
        },
    }, { provider: provider },
);
```

## Wrap-Up

Leveraging AWS IAM for Pod workloads is a secure and effective means of limiting
privileged execution, and provides a native experience for users.

Pod IAM can be extended further by also using the Kubernetes RBAC system. This
allows configuring permissions for Kubernetes API resources, and handle scenarios
such as limiting the namespace an IAM role can use, and what resources can be
managed in the namespace.

## Next Steps

Learn more about how [Pulumi works with Kubernetes][pulumi-k8s], and [get started][p-get-started]
if you're new.

Check out code examples for the S3 app referenced in this post,
along with other access control scenarios for EKS.

* [S3 app: EKS and an OIDC provider for Pod IAM.][peks-oidc]
* [Create an EKS cluster with Kubernetes RBAC for a Developer scoped IAM role.][peks-scoped-kubeconfigs]
* [More EKS examples][eks-examples]

Watch the video below for more details on how OIDC and Kubernetes RBAC works in
EKS. We demonstrate how to deploy [fluentd-cloudwatch][fluentd-cloudwatch] with
IAM to forward Pod logs to [AWS CloudWatch][aws-cw].

You can also follow us on [Twitter](https://twitter.com/pulumicorp),
subscribe to [PulumiTV](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw) on YouTube,
or join our [Community Slack](https://slack.pulumi.com/) channel if you have any questions.

{{< youtube "7qN9ABgmK9M" >}}

[peks-oidc]: https://github.com/pulumi/pulumi-eks/tree/master/examples/oidc-iam-sa
[peks-scoped-kubeconfigs]: https://github.com/pulumi/pulumi-eks/tree/master/examples/scoped-kubeconfigs
[fluentd-cloudwatch]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html
[aws-cw]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
[aws-eks]: https://aws.amazon.com/eks/
[aws-iam]: https://aws.amazon.com/iam/
[aws-pod-iam]: https://aws.amazon.com/blogs/opensource/introducing-fine-grained-iam-roles-service-accounts/
[aws-oidc]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html
[s3-app]: https://github.com/mhausenblas/s3-echoer
[aws-sts]: https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html
[eks-examples]: https://github.com/pulumi/pulumi-eks/tree/master/examples
[aws-assume-role-web]: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html
[k8s-dynamic-webhook]: https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers
[eks-webhook]: https://github.com/aws/amazon-eks-pod-identity-webhook/
[k8s-sa]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[pulumi-k8s]: {{< relref "/registry/packages/kubernetes" >}}
[p-get-started]: {{< relref "/docs/get-started/kubernetes" >}}
