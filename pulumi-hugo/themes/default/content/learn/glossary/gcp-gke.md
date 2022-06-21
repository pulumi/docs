---
title: Google Kubernetes Engine
meta_desc: A managed container orchestration tool on Google Cloud Platform (GCP), allowing for the deployment and automated management of containerized applications.
layout: glossary/single
---

## Description

[Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE) is a managed container orchestration tool. Applications are deployed within containers by defining a cluster and node pool, then giving the cluster a kubeconfig, deployment definition, and service definition, as with any other application deployed on a Kubernetes cluster. GKE also provides some additional services, such as auto-repair for unhealthy nodes and auto-scaling. Serverless functionality is available via [Cloud Run](https://cloud.google.com/run) for Anthos.

### Use Cases

As the longest-running managed Kubernetes service on the market, it benefits from a larger featureset. In particular, GKE provides quite a lot of automation, including automated updating of cluster versions and node pools as well as selected Kubernetes patches and CVE fixes. GKE also tends to support more Kubernetes versions than other services.
