---
title_tag: Next Steps | Kubernetes
meta_desc: This page provides a list of tutorials that take a deeper dive into Kubernetes
           across all major cloud providers.
title: Next steps
h1: "Pulumi & Kubernetes: Next steps"
weight: 8
menu:
  iac:
    name: Next steps
    identifier: kubernetes-get-started.next-steps
    parent: kubernetes-get-started
    weight: 8

aliases:
    - /docs/quickstart/kubernetes/next-steps/
    - /docs/iac/get-started/kubernetes/create-component/
    - /docs/quickstart/kubernetes/create-component/
---

Congrats! You've deployed your first project to Kubernetes with Pulumi. Here are some next steps, depending on your learning style.

## Video tutorial

Take a deeper look at Pulumi with Kubernetes with this video tutorial.

{{< get-started-next-step path="https://www.youtube.com/watch?v=2P8JLgAc5QI" label="Kubernetes in ~10 minutes" ref="gs-k8s-video" >}}

## Create reusable components

[Components](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate complexity and enable sharing and reuse. Instead of copy-pasting common patterns, you can encode them as components and stamp out entire pieces of infrastructure in just a few lines of code. Learn more about components and follow the [step-by-step guide](/docs/iac/guides/building-extending/components/build-a-component/) to build your first one.

{{< get-started-next-step path="/docs/iac/concepts/resources/components/" label="Learn about components" ref="gs-k8s-components" >}}

## Try Pulumi ESC (Environments, Secrets, and Configuration)

[Pulumi ESC](/docs/esc/) is a centralized secrets management and orchestration service. It introduces the concepts of _environments_ --- managed collections of static and dynamic settings that you can use to configure any project, stack, application, or service, including with short-lived cloud credentials through OpenID Connect.

With Pulumi ESC you can:

- **Stop secret sprawl.** Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.
- **Trust (and prove) your secrets are secure.** Every environment can be locked down with role-based access controls (RBAC) and versioned with all changes fully logged for auditing.
- **Ditch `.env` files.** No more storing secrets in plaintext on dev computers. Developers can access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.

{{< get-started-next-step path="/docs/esc/get-started" label="Learn more about Pulumi ESC" ref="gs-k8-esc" >}}

## Learn Pulumi

Dive into Learn Pulumi for a comprehensive walkthrough of key Pulumi concepts in the context of a real-life application.

{{< get-started-next-step path="/learn/pulumi-fundamentals" label="Learn Pulumi Fundamentals" ref="gs-k8s-learn" >}}

## Launch a new project with a template

Deploy the most common cloud architectures, from [static websites](/templates/static-website/) to [serverless applications](/templates/serverless-application/), [virtual machines](/templates/virtual-machine/), [container services](/templates/container-service/), and [Kubernetes clusters](/templates/kubernetes/).

{{< get-started-next-step path="/templates/" label="Browse templates" ref="gs-k8s-templates" >}}

## Dive into the docs

Read more about Pulumi's architecture and foundational concepts in depth, including [projects](/docs/concepts/projects/), [stacks](/docs/concepts/stack/), [configuration](/docs/concepts/config/), [secrets](/docs/concepts/secrets/), [resources](/docs/concepts/resources/), [state](/docs/concepts/state/), and more.

{{< get-started-next-step path="/docs/concepts/" label="Read the docs" ref="gs-k8s-docs" >}}

## Blog posts

Read through the latest blog posts about using Pulumi with Kubernetes.

{{< get-started-next-step path="/blog/tag/kubernetes" label="Read the Pulumi Blog" ref="gs-k8s-blog" >}}
