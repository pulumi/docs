---
title_tag: Next Steps | Kubernetes
meta_desc: This page provides a list of tutorials that take a deeper dive into Kubernetes
           across all major cloud providers.
title: Next steps
h1: "Pulumi & Kubernetes: Next steps"
weight: 9
menu:
  iac:
    name: Next steps
    identifier: kubernetes-get-started.next-steps
    parent: kubernetes-get-started
    weight: 9

aliases:
    - /docs/quickstart/kubernetes/next-steps/
---

Congrats! By completing this guide you have successfully:

- Created a new Pulumi project.
- Deployed an NGINX web server to Kubernetes.
- Modified and redeployed the running program.
- Refactored the deployment into a reusable component.
- Destroyed the resources you've provisioned.

Below are some recommended next steps, depending on your learning style. Also be sure to [join the Community Slack](https://slack.pulumi.com/) to meet fellow IaC practitioners.

## Try Pulumi ESC (Environments, Secrets, and Configuration)

[Pulumi ESC](/docs/esc/) is a centralized secrets management and orchestration service. It introduces the concepts of _environments_ --- managed collections of static and dynamic settings that you can use to configure any project, stack, application, or service, including with short-lived cloud credentials through OpenID Connect.

With Pulumi ESC you can:

- **Stop secret sprawl.** Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.
- **Trust (and prove) your secrets are secure.** Every environment can be locked down with role-based access controls (RBAC) and versioned with all changes fully logged for auditing.
- **Ditch `.env` files.** No more storing secrets in plaintext on dev computers. Developers can access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.

{{< get-started-next-step path="/docs/esc/get-started/" label="Learn more about Pulumi ESC" ref="gs-k8-esc" >}}

## Learn Pulumi

Dive into Learn Pulumi for a comprehensive walkthrough of key Pulumi concepts in the context of a real-life application.

{{< get-started-next-step path="/learn/pulumi-fundamentals" label="Learn Pulumi Fundamentals" ref="gs-k8s-learn" >}}

## Launch a new project with a template

Provision a managed Kubernetes cluster on [AWS](/templates/kubernetes/aws/), [Azure](/templates/kubernetes/azure/), or [Google Cloud](/templates/kubernetes/gcp/), or browse the full [Kubernetes cluster template](/templates/kubernetes/) collection.

{{< get-started-next-step path="/templates/kubernetes/" label="Browse Kubernetes templates" ref="gs-k8s-templates" >}}

## Video tutorial

Take a deeper look at Pulumi with Kubernetes with this video tutorial.

{{< get-started-next-step path="https://www.youtube.com/watch?v=2P8JLgAc5QI" label="Kubernetes in ~10 minutes" ref="gs-k8s-video" >}}

## Dive into the docs

Read more about Pulumi's architecture and foundational concepts in depth, including [projects](/docs/iac/concepts/projects/), [stacks](/docs/iac/concepts/stacks/), [configuration](/docs/iac/concepts/config/), [secrets](/docs/iac/concepts/secrets/), [resources](/docs/iac/concepts/resources/), [state](/docs/iac/concepts/state-and-backends/), and more.

{{< get-started-next-step path="/docs/iac/concepts/" label="Read the docs" ref="gs-k8s-docs" >}}

## Blog posts

Read through the latest blog posts about using Pulumi with Kubernetes.

{{< get-started-next-step path="/blog/tag/kubernetes" label="Read the Pulumi Blog" ref="gs-k8s-blog" >}}
