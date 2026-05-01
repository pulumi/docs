---
title_tag: Templates for Deploying Kubernetes Applications
title: "Kubernetes Application Templates"
layout: overview
schema_type: faq
meta_desc: Deploy applications and Helm charts to your existing Kubernetes clusters with Pulumi Kubernetes Application templates.
meta_image: meta.png
weight: 99
---

## About these templates

### What does a Kubernetes Application template do?

A Kubernetes Application template scaffolds a Pulumi project that deploys a workload to an existing Kubernetes cluster. The project uses Pulumi's [Kubernetes provider](/registry/packages/kubernetes) to create a namespace and deploy resources — either a Helm chart or a Deployment plus a Service — and runs against the cluster identified by your active kubeconfig.

### What's the difference between the Helm Chart and Web Application templates?

The two templates target different starting points:

- The [Helm Chart template](/templates/kubernetes-application/helm-chart/) installs a Helm chart (the Nginx ingress controller by default) into a new namespace. Use it when you want to deploy a packaged third-party workload.
- The [Web Application template](/templates/kubernetes-application/web-application/) creates a Kubernetes Deployment and Service from primitives. Use it when you want to deploy your own container image with explicit replica and Service-type control.

### Do I need a Kubernetes cluster before I deploy an application?

Yes. Both templates assume an existing cluster reachable via your local kubeconfig. If you don't have one yet, the [Kubernetes Cluster templates](/templates/kubernetes) provision a managed cluster on AWS, Azure, or Google Cloud and export a `kubeconfig` for you to use.
