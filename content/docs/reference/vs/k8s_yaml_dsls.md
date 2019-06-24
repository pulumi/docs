---
title: Pulumi vs. Kubernetes YAML and DSLs
menu:
  reference:
    parent: vs
    name: Kubernetes YAML
    weight: 5
---

Kubernetes offers YAML configuration out of the box. This is great as an "assembly language" for configuring
Kubernetes, but is not expressive enough to capture common requirements, and leads to significant boilerplate and copy
and pasting. Due to this, there are a few DSLs (like Helm Charts and Ksonnet) that aim to help solve the issue.

Pulumi is different, in that it lets you use your favorite languages. Instead of templating, Pulumi programs use real
code. Thanks to simple things like functions and classes, we have seen 1,000s of lines of templated YAML shrink to just
100 lines of code. This approach also helps to share and enforce best practices, thanks to real package management.

Pulumi is also multi-cloud. So, you only need to learn one programming model, tool, and workflow to program Kubernetes
in addition to your cloud resources. This unlocks several interesting scenarios that today require manual orchestration
between multiple systems, including

* Creating an AWS S3 bucket and using it from your Kubernetes application
* Provisioning your AKS, EKS, or GKE cluster itself, and deploying a Kubernetes application to it
* Deploying both raw Kubernetes YAML in addition to Helm Charts, with a single CLI and CI/CD system
* Provisioning a private registry, building and pushing your container image to it, and revving your Kubernetes
    Deployment to use it

Pulumi is [open source](https://github.com/pulumi/pulumi), has a growing community around it, and is a proud member of
the Cloud Native Computing Foundation (CNCF).
