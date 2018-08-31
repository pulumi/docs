---
title: Kubernetes YAML and DSLs
---

Kubernetes offers YAML configuration out of the box. This is great as an "assembly language" for configuring
Kubernetes, but is not expressive enough to capture common requirements, and leads to a lot of boilerplate. Due
to this, the community has conceived of several DSLs (like Helm Charts and Ksonnet) to help solve the issue.

Helm Charts use Go templates for YAML, but this feels bolted on. Because YAML is whitespace sensitive, you end up
spending as much time making sure you've injected enough spaces into the resulting file, than spending on the core
architecture itself. The model for reuse here is also quite primitive.

Ksonnet uses the Jsonnet templating language to generate YAML. This language can feel foreign to programmers
who understand existing languages. And its model for reuse is template injection, instead of real package management.

Pulumi is different: it lets you use your favorite languages. Instead of bespoke templating solutions, often tacked on
to a markup in an awkward and hard-to-learn and -remember way, Pulumi programs use real code. Thanks to simple things
like functions and classes, we have seen 1,000s of lines of templated YAML shrink to just 100 lines of code.
This approach also leads to far less copy and pasting between projects, because you can share packages.

Pulumi is also multi-cloud. So, you only need to learn one programming model, tool, and workflow to program Kubernetes
in addition to your cloud resources. This addresses cases that would otherwise require manual orchestration between
multiple systems. This includes

* Creating an AWS S3 bucket and using it from your Kubernetes application
* Provisioning your AKS, EKS, or GKE cluster itself, and deploying a Kubernetes application to it
* Deploying both raw Kubernetes YAML in addition to Helm Charts, with a single CLI and CI/CD system
* Provisioning a private registry, building and pushing your container image to it, and revving your Kubernetes
    Deployment to use it
