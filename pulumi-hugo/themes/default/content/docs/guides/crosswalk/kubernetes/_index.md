---
title: "Crosswalk for Kubernetes Guides"
meta_desc: Pulumi Crosswalk for Kubernetes is production-ready Kubernetes for teams. Work together to deliver
           Kubernetes to AWS, Azure, Google Cloud, or private.
linktitle: Crosswalk for Kubernetes
menu:
  userguides:
    identifier: crosswalk-kubernetes
    weight: 5
aliases: ["/docs/guides/k8s-the-prod-way/app", "/docs/guides/k8s-the-prod-way/architecture"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/kubernetes/crosswalk-for-k8s.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Pulumi Crosswalk for Kubernetes][cw-index] is production-ready Kubernetes
for teams. Work together to deliver Kubernetes to any cloud, AWS, Azure, Google
Cloud, or private.

If you are just getting started with Pulumi and Kubernetes, the [Get Started][k8s-get-started] guide is a better place to start.

## Playbooks for Kubernetes

Manage production-ready infrastructure leveraging hosted
Kubernetes offerings such as [Amazon Elastic Kubernetes Service (EKS)][eks], [Azure
Kubernetes Service (AKS)][aks], or [Google Kubernetes Engine (GKE)][gke].

Discover solutions to the hardest Kubernetes problems to avoid mitigating
pitfalls around infrastructure, security, governance, reliablity, and
maintainability of the cluster, it's workloads, and underlying resources.

[Get started][cw-playbooks] with the playbooks to manage Kubernetes in production with your team.

## Making Kubernetes Accessible to Everyone

Pulumi exposes 100% of the Kubernetes API in [`pulumi/kubernetes`][pulumi-k8s],
which means you use modern programming practices to reduce YAML/JSON complexity,
repetition, and encapsulate workloads effectively.

Through the new Crosswalk library extensions, the authorship experience has
improved to make the API more accessible and approachable to operators
and developers.

By reducing the Kubernetes API syntax used, including sane
defaults where possible, and maintaining idiomatic Kubernetes, it is
easier to work with the API and deploy resources. Crosswalk revamps the Kubernetes API resource
composition, but produces the exact semantic API output type. The ability to
drop into and inject a given API type's raw spec is maintained through out.

[Get started][pulumi-kx] with `pulumi/kubernetesx` to manage Kubernetes
workloads using constructs built for everyone.

## Query for Kubernetes

Maintaining and understanding Kubernetes clusters requires coordination
and delivery of continuous changes. The API surface area is complex and highly
disjointed when you want to make sense of what is taking place in the cluster, and why it is occuring.

Common choices for these assessments include a mix of `kubectl`
and [`client-go`][k8s-clientgo], and require the user to form manual joins
across resources, and perform a reactive series of queries to understand what is taking place.

To gain detailed insights, we've released a new tool called [Pulumi Query](#pulumi-query) that
helps you understand your clusters passively or in real-time.
By exposing Kubernetes through a library of streaming queries, it becomes easy
to write apps that can tail API resources, discover distinct versions of a
given Pod, or even inform you of which Services are publicly exposed to the
Internet.

[Get started][pulumi-kq] with `pulumi/query` to understand Kubernetes
clusters and workloads through a new lens.

## Pulumi Kubernetes Operator

<a href="./">
    <img src="/logos/tech/ci-cd/kubernetes.png" align="right" width="150" style="margin: 0 0 32px 16px;">
</a>

The [Pulumi Kubernetes Operator][k8s-operator] is an [extension pattern][k8s-ext-pattern] that
enables Kubernetes users to create a `Stack` as a first-class API
resource, and use the `StackController` to drive the updates of the Stack until
success.

Deploying [Pulumi Stacks][stack] in Kubernetes provides the capability to build
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alongside your Kubernetes workloads.

[Get started][k8s-operator-cicd] with the Pulumi Kubernetes Operator in your [continuous delivery][pulumi-cd] pipelines.

[k8s-operator]: https://github.com/pulumi/pulumi-kubernetes-operator
[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: /docs/intro/concepts/stack/
[k8s-operator-cicd]: /docs/guides/continuous-delivery/pulumi-kubernetes-operator/

## Join the Community

With Pulumi's unique approach to open source [infrastructure as code][gh-pulumi], you'll focus more on
code and business logic, and less on resource templates, YAML or DSL configuration languages.

Leverage Pulumi's collection of open source [tools][gh-pulumi],
Kubernetes [frameworks][pulumi-cloud-k8s], [continuous delivery integrations][pulumi-cd],
and [playbooks][cw-playbooks] to help you deliver production-ready Kubernetes.

Join the Pulumi team and thousands of practioners in our
[Community Slack][pulumi-slack] for questions and support, follow us on [Twitter][pulumi-twitter] for our latest news, and subscribe to our [YouTube channel][pulumi-yt] to access educational content.

## Frequently Asked Questions (FAQ)

See the [FAQ][crosswalk-faq] for more details.

<!-- markdownlint-disable url -->
[crosswalk-faq]: /docs/guides/crosswalk/kubernetes/faq/
[cw-index]: /docs/guides/crosswalk/kubernetes/
[cw-playbooks]: /docs/guides/crosswalk/kubernetes/playbooks/
[k8s-get-started]: /docs/get-started/kubernetes/
[eks]: https://aws.amazon.com/eks/
[aks]: https://azure.microsoft.com/en-us/services/kubernetes-service/
[gke]: https://cloud.google.com/kubernetes-engine/
[pulumi-k8s]: https://github.com/pulumi/pulumi-kubernetes
[pulumi-kx]: https://github.com/pulumi/pulumi-kubernetesx
[pulumi-kq]: https://github.com/pulumi/pulumi-query
[k8s-clientgo]: https://github.com/kubernetes/client-go
[gh-pulumi]: https://github.com/pulumi
[pulumi-cloud-k8s]: /registry/packages/kubernetes
[pulumi-cloud-k8s]: /registry/packages/kubernetes/
[pulumi-cd]: /docs/guides/continuous-delivery/
[pulumi-slack]: https://slack.pulumi.com/
[pulumi-twitter]: https://twitter.com/pulumicorp
[pulumi-yt]: https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw
<!-- markdownlint-enable url -->
