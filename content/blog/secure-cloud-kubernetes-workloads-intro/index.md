---
title: "Securely access cloud resources in Kubernetes workloads"
date: 2020-10-13T20:56:15-07:00
draft: true
meta_desc: An introduction for running accessing cloud resources securely for Kubernetes workloads
meta_image: meta.png
authors:
    - lee-briggs
tags:
    - kubernetes
    - security
    - cloud-engineering
---

As you build your cloud-native Kubernetes applications, you might eventually find you need to access cloud resources which reside outside your Kubernetes cluster. Perhaps you need to store static files in an object store (Amazon S3, Google Cloud Storage or Azure Blog Storage) or use a queuing system to pass messages to other services (Amazon SQS, Azure Service Bus or Google Pub/Sub).

Once you start to access these services from within your application, you'll need to find some way to authenticate to the cloud providers API, and that involves somehow managing credentials. It can be tempting at this point to create a "user" in your cloud provider and then create credentials like AWS Access Keys or a Google Cloud Service Account Key and store those inside your Kubernetes workload. A common approach is to store these credentials as a Kubernetes secret and then consume that secret as an environment variable in your running pods:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
data:
  username: bXktYXBw
  password: Mzk1MjgkdmRnN0pi
---
apiVersion: v1
kind: Pod
metadata:
  name: secret-test-pod
spec:
  containers:
    - name: test-container
      image: nginx
      volumeMounts:
        # name must match the volume name below
        - name: secret-volume
          mountPath: /etc/secret-volume
  # The secret data is exposed to Containers in the Pod through a Volume.
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
```

This method works and will allow access to cloud resources from your app. You can approach this with a security-conscious mindset and make sure the permissions that the keys are associated with are narrowly scoped (following the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)). However, unfortunately, if you have an information security team looking over your shoulder, they will still see this practice and be extremely concerned.

In this first in a series of posts, we'll talk about why this might be a problem, examine the mindset of a malicious user attacking your Kubernetes cluster and introduce the mechanisms for avoiding these patterns.

<!--more-->

## The Static Credential Problem

Static credentials (such as AWS Access Keys) are easy to use for consumers, but they create a myriad of problems from a security perspective. To understand these problems, it's essential to take a quick look at how potential attackers might operate.

It's rare for a malicious user to find the keys to the kingdom immediately when they decide to target you. Commonly, an attacker will find a small bug or hole in your application or infrastructure and then attempt to use that bug to escalate their privileges to move horizontally or vertically through your infrastructure. Navigating through the gaps in your infrastructure takes time. The longer an attacker has access to your systems, the more likely they are to be able to escalate their access to the point where they can access sensitive data.

A well-secured environment attempts to limit the capability for an attacker to [pivot](https://en.wikipedia.org/wiki/Exploit_(computer_security)#Pivoting) by adding more layers for them to get through and restricting the amount of time they have to get through those layers.

If you decide to use static credentials, the most important thing to consider is that they can be easily stolen and copied by an attacker. They (usually) live indefinitely and will continue to work until someone manually revokes them.
Alongside this, by hard coding these credentials into a Kubernetes secret, it presents multiple layers from which an attacker could steal them:

- The Kubernetes API (by retrieving the secret)
- Inside the running pod (by grabbing the environment variables, where they're in plaintext)

## Introducing roles

Some variant of "machine identity" is offered by all the major cloud providers, and you've probably used them when deploying workloads to virtual machines. At a basic level, the idea is that you'd assign a "role" to the virtual machine, and the cloud provider automatically provides authenticated access to its API. This way, you never have to store credentials locally, where they could potentially get compromised.

It's reasonably straightforward using roles on a virtual machine, but if you're using Kubernetes an issue arises. Kubernetes worker nodes can be assigned a role, but that role gets shared across all pods running on that node. Suppose your worker nodes are running pods with multiple applications that have different requirements. In that case, you have the unfortunate option of assigning roles to your nodes which have access to _all_ the resources for _all_ your pods, which could present an opportunity for an attacker to pivot quickly.

To mitigate this, many cloud providers offer a solution to push roles all the way down to the Kubernetes pod. I'll introduce those options here, and in subsequent posts show some real world examples of how you're able to leverage these solutions.

### AWS EKS

EKS is the youngest of the managed Kubernetes offerings and was the last of the three to provider the native capability to push IAM roles down to pods. Previously, operators could install third-party solutions like [KIAM](https://github.com/uswitch/kiam) and [Kube2IAM](https://github.com/jtblin/kube2iam) in their clusters, and both of these solutions are widely used and well tested.

EKS now offers a native solution, which involves creating a cluster with an OpenID connect issuer attached to it. You can read more about this [here](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

Once you've created a cluster and associated an IAM OIDC provider to it, you can deploy Kubernetes pods which use an [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) which you'll need to create.. To leverage this IAM role in your pod, you have to patch the Kubernetes [service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) associated with the pod and add annotations that tell the pod which IAM role to use.

Pulumi's first class support for Kubernetes Helm Charts and AWS resources mean you can perform all of this in one Pulumi program. Look out for the rest of this series to see how it's done!

### Azure AKS

Azure AKS uses a different approach to assign roles to pods. [AAD Pod Identity](https://github.com/Azure/aad-pod-identity) project is an add-on which is deployed into your AKS cluster. AAD Pod Identity includes a Kubernetes [CustomResource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) which the running components of AAD Pod Identity watch for. You can then create a [Service Principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) and assign it to your pod.

Again, Pulumi has first class support for all of Azure's resource via the [Azure NextGen Provider](https://github.com/pulumi/pulumi-azure-nextgen). Watch out for the rest of the series for a real world example!

### Google Cloud GKE

Google's GKE has native support for what it calls ["Workload Identity"](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). With this solution, you create a GKE cluster with workload identity enabled, and then ensure that at least one node pool has workload identity enabled. You can then annotate the Kubernetes service account associated with your pod and point it at a created [GCP Service Account](https://cloud.google.com/iam/docs/service-accounts). Hopefully the confusion between Kubernetes service accounts and Google Cloud service accounts will become clearer in the tutorial blog post!

## Wrap up

Hopefully, I've made a compelling case for why you should reconsider using static credentials for your application, now introduced the idea for how to avoid using them in your cloud-native applications. In my next post, I'll introduce the application we're going to deploy to all of these different cloud providers, and show you how to deploy it securely on AWS EKS. Stay tuned!
