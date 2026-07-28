---
title_tag: Next Steps | Kubernetes
title: Next steps
h1: Next steps
stepper_link: "Next: Wrap up"
meta_desc: This page provides a list of tutorials that take a deeper dive into Kubernetes
           across all major cloud providers.
weight: 10
menu:
    iac:
        name: Next steps
        identifier: kubernetes-get-started.next-steps
        parent: kubernetes-get-started
        weight: 10
aliases:
    - /docs/quickstart/kubernetes/next-steps/
    - /docs/iac/get-started/kubernetes/create-component/
    - /docs/quickstart/kubernetes/create-component/
---

Congratulations! You now know how to provision and manage cloud infrastructure with Pulumi. In this guide, you learned how to:

- Create and configure a Pulumi project and stack
- Provision new cloud resources
- Update existing cloud resources
- Use the Pulumi CLI to perform common operations
- Cleanly destroy cloud resources and stacks

Below are a few good next steps to build on this foundation and keep the learning going.

## Video tutorial

Take a deeper look at Pulumi with Kubernetes with this video tutorial.

{{< get-started-next-step path="https://www.youtube.com/watch?v=2P8JLgAc5QI" label="Kubernetes in ~10 minutes" ref="gs-k8s-video" >}}

## Create reusable components

[Components](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate complexity and enable sharing and reuse. Rather than copy and paste common patterns, you can encode them as components and share them with your team with just a few lines of code. [Learn more about components](/docs/iac/concepts/resources/components/) or [follow the guide](/docs/iac/guides/building-extending/components/build-a-component/) to build your own.

{{< get-started-next-step path="/docs/iac/guides/building-extending/components/build-a-component/" label="Build a component" ref="gs-k8s-components" >}}

## Try Pulumi ESC (Environments, Secrets, and Configuration)

[Pulumi ESC](/docs/esc/) is a centralized secrets and configuration service that introduces the concept of _environments_ — managed collections of static and dynamic settings that you can use to configure any project, stack, application, or service, including with short-lived cloud credentials through OpenID Connect.

{{< get-started-next-step path="/docs/esc/get-started/" label="Learn more about Pulumi ESC" ref="gs-k8s-esc" >}}

## Launch a new project with a template

Easily deploy the most common cloud architectures, from [static websites](/templates/static-website/) to [serverless applications](/templates/serverless-application/), [virtual machines](/templates/virtual-machine/), [container services](/templates/container-service/), and [Kubernetes clusters](/templates/kubernetes/).

{{< get-started-next-step path="/templates/" label="Browse templates" ref="gs-k8s-guides" >}}

## Dive into the docs

Read more about Pulumi's architecture and foundational concepts in depth, including [projects](/docs/concepts/projects/), [stacks](/docs/concepts/stack/), [configuration](/docs/concepts/config/), [secrets](/docs/concepts/secrets/), [resources](/docs/concepts/resources/), [state](/docs/concepts/state/), and more.

{{< get-started-next-step path="/docs/concepts/" label="Read the docs" ref="gs-k8s-docs" >}}

## Check out the blog

Browse the latest posts on using Pulumi with Kubernetes, including everything from new features to technical architectures and best practices.

{{< get-started-next-step path="/blog/tag/kubernetes" label="Browse Kubernetes posts" ref="gs-k8s-blog" >}}
