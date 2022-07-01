---
title: Managed Kubernetes Service
meta_desc: A type of database that does not store its data in tables.
layout: glossary/single
---

## Definition

A managed kubernetes service is a kubernetes platform where some or all of the responsibility for setup and maintenance lies with a third-party provider. The extent of services offered varies from vendor to vendor, but generally, using a managed kubernetes service shifts the responsibility for keeping the cluster online and updated from you to the vendor, as well as some or all of its maintenance.

| Feature                    | GKE                                            | EKS                                                             | AKS                      |
|----------------------------|------------------------------------------------|-----------------------------------------------------------------|--------------------------|
| Kubernetes Version Support | 14 Months                                      | 12 Months                                                       | 12 Months                |
| Container Runtime          | containerd                                     | containerd                                                      | containerd               |
| Control Plane Updates      | Automatic or Manual                            | Manual                                                          | Manual                   |
| Node OS                    | Container-Optimized OS  Ubuntu  Windows Server | Amazon Linux  Ubuntu  Windows Server                            | Ubuntu  Windows Server   |
| Node Updates               | Automatic                                      | Manual                                                          | Automatic or Manual      |
| Node Health Monitoring     | Node auto-repair                               | Not Kubernetes-aware: Autoscaling will replace node if it fails | Node auto-repair         |
| Serverless Compute         | Cloud Run for Anthos                           | AWS Fargate                                                     | Azure Container Instance |
