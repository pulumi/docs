---
title: Elastic Kubernetes Service
meta_desc: A managed Kubernetes service on AWS, allowing you to run your containerized workloads on Kubernetes without the overhead of managing it yourself.
layout: glossary/single
---

## Description

[AWS Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS) is a managed Kubernetes service, allowing you to run your containerized workloads on Kubernetes without the overhead of managing it yourself. When using EKS, the control plane nodes responsible for the scheduling and scaling of your application containers are managed automatically by AWS. The native role-based access control (RBAC) built into Kubernetes integrates directly with AWS IAM. Like Amazon ECS, deployment can be via [Fargate](/learn/glossary/aws-fargate) or EC2.

### Use Cases

EKS is an ideal choice for when you know you need the flexibility and scalability of Kubernetes, but do not want to be responsible for defining and managing your own cluster on-prem or on the cloud. Applications that need to be resilient and automatically scalable, such as web apps or machine learning workloads, are commonly deployed using Kubernetes.
