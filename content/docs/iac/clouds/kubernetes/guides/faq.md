---
title_tag: Kubernetes FAQ | Crosswalk
meta_desc: A collection of common questions about Kubernetes usage with Pulumi.
title: FAQ
h1: Kubernetes FAQ
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
menu:
  iac:
    name: FAQ
    parent: kubernetes-clouds-guides
    weight: 14
aliases:
  - /docs/guides/crosswalk/kubernetes/faq/
  - /docs/clouds/kubernetes/guides/faq/
---

1. **What does Crosswalk for Kubernetes include?**

    Crosswalk for Kubernetes is a set of playbooks to configure, deploy, and manage
    Kubernetes production, along with new programmatic libraries and tools to facilitate
    understanding and working with the Kubernetes API.

    Playbook tasks are segmented by operations, and belong to one of the 6 stacks
    outlined in [Production Architecture for Teams][cw-playbooks]. The Pulumi code
    for each stack is available and linked at the top of each task, and
    references the [`pulumi/kubernetes`][pulumi-k8s] and
    [`pulumi/kubernetesx`][pulumi-kx] libraries in action.

    Together, the docs and stack code provide a reference architecture to operate
    and use Kubernetes in production across a team using industry best-practices.

    When the playbooks and frameworks are combined with querying abilities made
    available in [`pulumi/kq`][pulumi-kq], you can manage, observe, and take
    action on your Kubernetes cluster with informed, real-time data.

1. **Where is the code located?**

    You can find the Crosswalk code across various repos.

    * [Playbook reference architecture][pulumi-guides]
    * [Kubernetes Extensions][pulumi-kx]
    * [Query for Kubernetes][pulumi-kq]

1. **Where can I suggest a change or open an issue with the docs?**

    You can open an issue in [`pulumi/docs`][pulumi-docs] for any changes to the
    Crosswalk documentation.

1. **Where can I ask for assistance on Crosswalk for Kubernetes?**

    You can find us in the [community Slack][pulumi-slack] channel.

1. **Does Crosswalk support on-prem or other cloud providers?**

    Support for on-prem environments, and other clouds is an area we'd love
    to build out. Open an issue in [`pulumi/docs`][pulumi-docs] to describe your
    Crosswalk use case.

    * **Digital Ocean**: Check out [Managing DigitalOcean and Kubernetes with Pulumi][k8s-do] for more details.

## More FAQ

* [Pulumi IaC FAQ](/docs/iac/support/faq/)
* [Pulumi ESC FAQ](/docs/esc/faq/)
* [Pulumi Cloud FAQ](/docs/pulumi-cloud/faq/)
* [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
* [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
* [Pulumi CrossGuard FAQ](/docs/using-pulumi/crossguard/faq/)

<!-- markdownlint-disable url -->
[k8s-do]: https://www.digitalocean.com/community/tutorials/how-to-manage-digitalocean-and-kubernetes-infrastructure-with-pulumi
[pulumi-slack]: https://slack.pulumi.com/
[pulumi-docs]: https://github.com/pulumi/docs
[pulumi-guides]: https://github.com/pulumi/kubernetes-guides
[cw-playbooks]: /docs/clouds/kubernetes/guides/playbooks/
[pulumi-k8s]: https://github.com/pulumi/pulumi-kubernetes
[pulumi-kx]: https://github.com/pulumi/pulumi-kubernetesx
[pulumi-kq]: https://github.com/pulumi/pulumi-query
<!-- markdownlint-enable url -->
