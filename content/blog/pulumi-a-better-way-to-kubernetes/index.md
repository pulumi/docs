---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
---


Kubernetes is a powerful container orchestrator that is being adopted
rapidly across the industry. At the same time, it is notoriously complex
and presents a steep learning curve for newcomers. Nobody likes
programming in YAML, and templates [make it even
harder](https://github.com/helm/charts/blob/cb3dcd7f1e0e6a152d110bcb776523856468e670/stable/cert-manager/templates/deployment.yaml).
It's difficult to understand the state of the cluster -- [Did my
deployment
succeed](../../../com/pulumi/blog/how-do-kubernetes-deployments-work-an-adversarial-perspective.html)?
Why isn't my app working? And we often need to manage hosted cloud
resources in addition to Kubernetes ones.

In this post, we will see how [Pulumi](https://pulumi.com) can help you
tame these issues and make Kubernetes more accessible, using familiar
languages and your favorite tools. It's simply a [better way to work
with Kubernetes](https://pulumi.io/quickstart/kubernetes/index.html)!

Clusters as code
---------------------------------------

Pulumi can seamlessly manage multiple layers of your stack, from the raw
infrastructure to Kubernetes resources, and all the way up to
[serverless
app](../../../com/pulumi/blog/simple-serverless-programming-with-google-cloud-functions-and-pulumi.html)
code. Rather than gluing together yet another set of tools, you can
[create managed Kubernetes
clusters](../../../com/pulumi/blog/program-kubernetes-with-11-cloud-native-pulumi-pearls.html)
with [GKE](https://github.com/pulumi/examples/tree/master/gcp-ts-gke),
[EKS](../../../com/pulumi/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi.html),
or
[AKS](../../../com/pulumi/blog/create-aks-clusters-with-monitoring-and-logging-with-pulumi-azure-open-source-sdks.html),
and then reference them directly in your Pulumi code!

![Create an EKS
cluster](https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=1600&name=cluster.png){width="1600"
sizes="(max-width: 1600px) 100vw, 1600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=800&name=cluster.png 800w, https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=1600&name=cluster.png 1600w, https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=2400&name=cluster.png 2400w, https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=3200&name=cluster.png 3200w, https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=4000&name=cluster.png 4000w, https://blog.pulumi.com/hs-fs/hubfs/cluster.png?width=4800&name=cluster.png 4800w"}

Apps as code (not YAML!)
-----------------------------------------------------

Pulumi exposes the full API surface of Kubernetes as classes in your
SDK, so you can manage any k8s resource (including CRDs and related
CustomResources) in your Pulumi code. Stop [trying to work
around](https://ksonnet.io/) the [limitations of
YAML](https://arp242.net/yaml-config.html) with
[templates](https://helm.sh/docs/chart_template_guide/#the-chart-template-developer-s-guide),
and reap the benefits of real software development practices:
[abstraction](../../../com/pulumi/blog/pulumi-and-docker-development-to-production.html),
conditionals, looping, library support,
[packaging](../../../com/pulumi/blog/creating-and-reusing-cloud-components-using-package-managers.html),
[testing](../../../com/pulumi/blog/testing-your-infrastructure-as-code-with-pulumi.html),
debugging, and more! From the obvious ([use variables to manage resource
metadata](../../../com/pulumi/blog/program-kubernetes-with-11-cloud-native-pulumi-pearls.html)),
to the more esoteric ([gate a canary deployment with
Prometheus](../../../com/pulumi/blog/program-kubernetes-with-11-cloud-native-pulumi-pearls.html)),
Pulumi keeps the simple things simple, and makes the hard things
possible.

![Write real code to deploy a guestbook
app](https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=1138&name=guestbook.png){width="1138"
sizes="(max-width: 1138px) 100vw, 1138px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=569&name=guestbook.png 569w, https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=1138&name=guestbook.png 1138w, https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=1707&name=guestbook.png 1707w, https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=2276&name=guestbook.png 2276w, https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=2845&name=guestbook.png 2845w, https://blog.pulumi.com/hs-fs/hubfs/guestbook.png?width=3414&name=guestbook.png 3414w"}

![Deploy the app to Kubernetes using Pulumi](https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=825&name=app-cli.png){width="825" sizes="(max-width: 825px) 100vw, 825px" srcset="https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=413&name=app-cli.png 413w, https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=825&name=app-cli.png 825w, https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=1238&name=app-cli.png 1238w, https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=1650&name=app-cli.png 1650w, https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=2063&name=app-cli.png 2063w, https://blog.pulumi.com/hs-fs/hubfs/app-cli.png?width=2475&name=app-cli.png 2475w"}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Integrate with existing Helm charts or manifests
--------------------------------------------------------------------------------------------------------

Most projects aren't greenfield apps, and we know it's critical to
support an incremental transition when you switch tools. Our SDKs allow
you to import [Helm
charts](../../../com/pulumi/blog/using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code.html)
and [YAML
manifests](../../../com/pulumi/blog/program-kubernetes-with-11-cloud-native-pulumi-pearls.html),
and then mix and match these resources within your Pulumi program. While
you can keep it simple and just import the resources, you have the full
power of a programming language at your disposal. Why fight with a
[complicated YAML templating
scheme](https://helm.sh/docs/chart_template_guide/#the-chart-template-developer-s-guide)
when you can accomplish the same thing (and much more) with a real
programming language? Take advantage of 60 years of software engineering
know-how to [make your deployments more
reproducible](../../../com/pulumi/blog/simple-reproducible-kubernetes-deployments.html)
and maintainable.

![Deploying a Helm chart with Pulumi](https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=1600&name=helm-pulumi-deploy.gif){width="1600" sizes="(max-width: 1600px) 100vw, 1600px" srcset="https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=800&name=helm-pulumi-deploy.gif 800w, https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=1600&name=helm-pulumi-deploy.gif 1600w, https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=2400&name=helm-pulumi-deploy.gif 2400w, https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=3200&name=helm-pulumi-deploy.gif 3200w, https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=4000&name=helm-pulumi-deploy.gif 4000w, https://blog.pulumi.com/hs-fs/hubfs/helm-pulumi-deploy.gif?width=4800&name=helm-pulumi-deploy.gif 4800w"}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Make full use of your cloud
--------------------------------------------------------------

While you can run stateful workloads on Kubernetes using StatefulSets,
it's often better to use a managed service from your cloud provider.
Since Pulumi can [manage cloud resources as well as k8s
resources](../../../com/pulumi/blog/pulumi-heart-google-cloud-platform.html),
it's easy to bridge that gap! Try adding in a [managed
database](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean),
[message
queue](../../../com/pulumi/blog/pulumi-and-epsagon-define-deploy-and-monitor-serverless-applications.html),
or [object
store](https://github.com/pulumi/examples/tree/master/kubernetes-ts-s3-rollout),
and see how much simpler your k8s app can be. When your app is already
running in the cloud, think outside of k8s, and use the power of the
cloud! It's far easier to maintain an app at scale if you strategically
mix in managed cloud resources.

![Use a managed database in a Kubernetes app](https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=828&name=cosmos.png){width="828" sizes="(max-width: 828px) 100vw, 828px" srcset="https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=414&name=cosmos.png 414w, https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=828&name=cosmos.png 828w, https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=1242&name=cosmos.png 1242w, https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=1656&name=cosmos.png 1656w, https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=2070&name=cosmos.png 2070w, https://blog.pulumi.com/hs-fs/hubfs/cosmos.png?width=2484&name=cosmos.png 2484w"}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Debugging failures
--------------------------------------------

It can be daunting to troubleshoot failures in Kubernetes, especially
for new users. What happens after I run `kubectl apply`? [Why is my app
not
working](../../../com/pulumi/blog/how-do-kubernetes-deployments-work-an-adversarial-perspective.html)?
Even with a detailed guide to follow, it can feel like playing 20
questions with `kubectl` to get the answers you need. Pulumi's
Kubernetes provider includes [sophisticated
logic](../../../com/pulumi/blog/improving-kubernetes-management-with-pulumis-await-logic.html)
to [check resource
readiness](../../../com/pulumi/blog/program-kubernetes-with-11-cloud-native-pulumi-pearls.html),
and proactively surfaces errors during updates. With Pulumi, it's far
easier to understand the state of your k8s resources, and [get the
information you
need](../../../com/pulumi/blog/unified-logs-with-pulumi-logs.html) to
make changes when something goes wrong.

![See detailed status during deployments with
Pulumi](https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=865&name=deployment-zoom.gif){width="865"
sizes="(max-width: 865px) 100vw, 865px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=433&name=deployment-zoom.gif 433w, https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=865&name=deployment-zoom.gif 865w, https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=1298&name=deployment-zoom.gif 1298w, https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=1730&name=deployment-zoom.gif 1730w, https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=2163&name=deployment-zoom.gif 2163w, https://blog.pulumi.com/hs-fs/hubfs/deployment-zoom.gif?width=2595&name=deployment-zoom.gif 2595w"}

Integrating with CI/CD
---------------------------------------------------

Kubernetes uses an eventual consistency model that can be difficult to
integrate with CI/CD systems. How do you know when your application is
ready? Common workflows involve [scripting kubectl
calls](https://kubernetes.io/docs/reference/kubectl/conventions/#using-kubectl-in-reusable-scripts)
and parsing JSON output in Bash. This approach is brittle, and the
process is a little different for every Kubernetes resource type.
Pulumi's [state reconciliation
model](https://pulumi.io/reference/how.html) is a [natural fit for CI/CD
systems](https://pulumi.io/reference/cd.html): review changes with a
preview, and then proceed with confidence once an update succeeds. This
is great for GitOps and
[ChatOps](../../../com/pulumi/blog/getting-to-chatops-with-pulumi-webhooks.html)
workflows. You don't have to be an expert on the inner workings of
Kubernetes to be productive with Pulumi.

Since you can [manage a full infrastructure
stack](../../../com/pulumi/blog/using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code.html)
with Pulumi, you can [create infrastructure on
demand](../../../com/pulumi/blog/data-science-on-demand-spinning-up-a-wallaroo-cluster-is-easy-with-pulumi.html)
(k8s cluster, databases, networking, object storage, etc.), spin up your
application, run tests, and then tear the whole stack back down! This
saves you money and builds confidence that you can recover from disaster
scenarios.

![It's real code, so write tests for infrastructure and
apps](https://blog.pulumi.com/hs-fs/hubfs/test.png?width=800&name=test.png){width="800"
sizes="(max-width: 800px) 100vw, 800px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/test.png?width=400&name=test.png 400w, https://blog.pulumi.com/hs-fs/hubfs/test.png?width=800&name=test.png 800w, https://blog.pulumi.com/hs-fs/hubfs/test.png?width=1200&name=test.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/test.png?width=1600&name=test.png 1600w, https://blog.pulumi.com/hs-fs/hubfs/test.png?width=2000&name=test.png 2000w, https://blog.pulumi.com/hs-fs/hubfs/test.png?width=2400&name=test.png 2400w"}

Learn more
----------------------------

If you'd like to learn about Pulumi and how to manage your
infrastructure and Kubernetes through code, [click here to get started
today](https://pulumi.io/quickstart). Pulumi is open source and free to
use.

As always, you can check out our code on
[GitHub](https://github.com/pulumi), follow us on
[Twitter](https://twitter.com/pulumicorp), subscribe to our [YouTube
channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), or
join our [Community Slack](https://slack.pulumi.io/) channel if you have
any questions, need support, or just want to say hello.

If you'd like to chat with our team, or get hands-on assistance with
migrating your existing configuration code (including ksonnet programs)
to Pulumi, [please don't hesitate to drop us a
line](https://www.pulumi.com/contact/).

 

