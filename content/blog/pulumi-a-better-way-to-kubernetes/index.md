---
title: "Pulumi: A Better Way to Kubernetes"
authors: ["levi-blackstone"]
tags: ["Kubernetes"]
date: "2019-05-21"

meta_image: "helm-deploy-using-pulumi.gif"
---

Kubernetes is a powerful container orchestrator that is being adopted
rapidly across the industry. At the same time, it is notoriously complex
and presents a steep learning curve for newcomers. Nobody likes
programming in YAML, and templates [make it even harder](https://github.com/helm/charts/blob/cb3dcd7f1e0e6a152d110bcb776523856468e670/stable/cert-manager/templates/deployment.yaml).
It's difficult to understand the state of the cluster --
[Did my deployment succeed]({{< relref "how-do-kubernetes-deployments-work-an-adversarial-perspective" >}})?
Why isn't my app working? And we often need to manage hosted cloud
resources in addition to Kubernetes ones.

In this post, we will see how [Pulumi](/) can help you
tame these issues and make Kubernetes more accessible, using familiar
languages and your favorite tools. It's simply
[Kubernetes made easy]({{< relref "/kubernetes" >}})!
<!--more-->

## Clusters as code

Pulumi can seamlessly manage multiple layers of your stack, from the raw
infrastructure to Kubernetes resources, and all the way up to
[serverless app]({{< relref "simple-serverless-programming-with-google-cloud-functions-and-pulumi" >}})
code. Rather than gluing together yet another set of tools, you can
[create managed Kubernetes clusters]({{< relref "program-kubernetes-with-11-cloud-native-pulumi-pearls" >}})
with [GKE](https://github.com/pulumi/examples/tree/master/gcp-ts-gke),
[EKS]({{< relref "easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}) or
[AKS]({{< relref "create-aks-clusters-with-monitoring-and-logging-with-pulumi-azure-open-source-sdks" >}})
and then reference them directly in your Pulumi code!

![Create an EKS cluster](./creating-an-eks-cluster.png)

## Apps as code (not YAML!)

Pulumi exposes the full API surface of Kubernetes as classes in your
SDK, so you can manage any k8s resource (including CRDs and related
CustomResources) in your Pulumi code. Stop [trying to work
around](https://ksonnet.io/) the [limitations of YAML](https://arp242.net/yaml-config.html) with
[templates](https://helm.sh/docs/chart_template_guide/#the-chart-template-developer-s-guide),
and reap the benefits of real software development practices:
[abstraction]({{< relref "pulumi-and-docker-development-to-production" >}}),
conditionals, looping, library support,
[packaging]({{< relref "creating-and-reusing-cloud-components-using-package-managers" >}}),
[testing]({{< relref "testing-your-infrastructure-as-code-with-pulumi" >}}),
debugging, and more! From the obvious
([use variables to manage resource metadata]({{< relref "program-kubernetes-with-11-cloud-native-pulumi-pearls" >}})),
to the more esoteric
([gate a canary deployment with Prometheus]({{< relref "program-kubernetes-with-11-cloud-native-pulumi-pearls" >}}),
Pulumi keeps the simple things simple, and makes the hard things possible.

![Write real code to deploy a guestbook app](./guestbook.png)

![Deploy the app to Kubernetes using Pulumi](./app-cli.png)

## Integrate with existing Helm charts or manifests

Most projects aren't greenfield apps, and we know it's critical to
support an incremental transition when you switch tools. Our SDKs allow
you to import [Helm charts]({{< relref "using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code" >}})
and [YAML manifests]({{< relref "program-kubernetes-with-11-cloud-native-pulumi-pearls" >}})
and then mix and match these resources within your Pulumi program. While
you can keep it simple and just import the resources, you have the full
power of a programming language at your disposal. Why fight with a
[complicated YAML templating scheme](https://helm.sh/docs/chart_template_guide/#the-chart-template-developer-s-guide)
when you can accomplish the same thing (and much more) with a real
programming language? Take advantage of 60 years of software engineering
know-how to
[make your deployments more reproducible]({{< relref "simple-reproducible-kubernetes-deployments" >}})
and maintainable.

![Deploying a Helm chart with Pulumi](./helm-deploy-using-pulumi.gif)

## Make full use of your cloud

While you can run stateful workloads on Kubernetes using StatefulSets,
it's often better to use a managed service from your cloud provider.
Since Pulumi can [manage cloud resources as well as k8s resources]({{< relref "pulumi-heart-google-cloud-platform" >}})
it's easy to bridge that gap! Try adding in a [managed database](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean),
[message queue]({{< relref "pulumi-and-epsagon-define-deploy-and-monitor-serverless-applications" >}})
or [object store](https://github.com/pulumi/examples/tree/master/kubernetes-ts-s3-rollout),
and see how much simpler your k8s app can be. When your app is already
running in the cloud, think outside of k8s, and use the power of the
cloud! It's far easier to maintain an app at scale if you strategically
mix in managed cloud resources.

![Use a managed database in a Kubernetes app](./cosmos.png)

## Debugging failures

It can be daunting to troubleshoot failures in Kubernetes, especially
for new users. What happens after I run `kubectl apply`?
[Why is my app not working]({{< relref "how-do-kubernetes-deployments-work-an-adversarial-perspective" >}})?
Even with a detailed guide to follow, it can feel like playing 20
questions with `kubectl` to get the answers you need. Pulumi's
Kubernetes provider includes [sophisticated logic]({{< relref "improving-kubernetes-management-with-pulumis-await-logic" >}})
to [check resource readiness]({{< relref "program-kubernetes-with-11-cloud-native-pulumi-pearls" >}}),
and proactively surfaces errors during updates. With Pulumi, it's far
easier to understand the state of your k8s resources, and
[get the information you need]({{< relref "unified-logs-with-pulumi-logs" >}}) to
make changes when something goes wrong.

![See detailed status during deployments with Pulumi](./deployment-zoom.gif)

## Integrating with CI/CD

Kubernetes uses an eventual consistency model that can be difficult to
integrate with CI/CD systems. How do you know when your application is
ready? Common workflows involve [scripting kubectl calls](https://kubernetes.io/docs/reference/kubectl/conventions/#using-kubectl-in-reusable-scripts)
and parsing JSON output in Bash. This approach is brittle, and the
process is a little different for every Kubernetes resource type.
Pulumi's [state reconciliation model]({{< ref "/docs/reference/how" >}}) is a
[natural fit for CI/CD systems]({{< ref "/docs/reference/cd" >}}): review changes with a
preview, and then proceed with confidence once an update succeeds. This
is great for GitOps and [ChatOps]({{< relref "getting-to-chatops-with-pulumi-webhooks" >}})
workflows. You don't have to be an expert on the inner workings of
Kubernetes to be productive with Pulumi.

Since you can [manage a full infrastructure stack]({{< relref "using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code" >}})
with Pulumi, you can
[create infrastructure on demand]{{< relref "data-science-on-demand-spinning-up-a-wallaroo-cluster-is-easy-with-pulumi" >}})
(k8s cluster, databases, networking, object storage, etc.), spin up your
application, run tests, and then tear the whole stack back down! This
saves you money and builds confidence that you can recover from disaster
scenarios.

![It's real code, so write tests for infrastructure and apps](./test.png)

## Learn more

If you'd like to learn about Pulumi and how to manage your
infrastructure and Kubernetes through code,
[click here to get started today]({{< ref "/docs/quickstart" >}}). Pulumi is open source and free to
use.

As always, you can check out our code on
[GitHub](https://github.com/pulumi), follow us on
[Twitter](https://twitter.com/pulumicorp), subscribe to our
[YouTube channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), or
join our [Community Slack](https://slack.pulumi.io/) channel if you have
any questions, need support, or just want to say hello.

If you'd like to chat with our team, or get hands-on assistance with
migrating your existing configuration code (including ksonnet programs)
to Pulumi, [please don't hesitate to drop us a line]({{< ref "/contact" >}}).
