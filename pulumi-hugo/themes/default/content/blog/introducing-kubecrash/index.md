---
title: "Introducing KubeCrash: Cloud Native Crash Courses"
date: 2022-04-08
draft: false
meta_desc: Explore cloud native tech via the KubeCrash courses and content
meta_image: meta.png
authors:
    - kat-cosgrove
tags:
    - cloud-native
    - pulumi-news
---

Can’t make it to Valencia for KubeCon this year? Timezone doesn’t work for the virtual conference either? We can’t fix time, but if you’re feeling left out and still want some of that sweet cloud native content, you can still join us for [KubeCrash](https://kubecrash.io/), a new event hosting live crash courses and sessions on cloud native tech. Come hang out and learn directly from the maintainers of cloud native open source projects!

## About KubeCrash

Five open source companies have teamed up to bring you top-notch, KubeCon-grade crash courses on cloud native tech. No vendor pitches, just awesome open source content on projects such as Linkerd, cert-manager, CockroachDB, Pulumi, Polaris, and Goldilocks.

With Kubernetes becoming the new standard for cloud-hosted application development, DevOps teams are driving the technology choices for enterprise-grade cloud native tooling. Freely available open source solutions are often the primary source for these tooling decisions.

KubeCrash provides a half-day knowledge sharing and virtual learning environment for developers, reliability engineers, cloud security specialists, and platform engineers. Learn directly from the maintainers of some of the most popular open source projects in this series of focused talks and workshops.

## The KubeCrash program

Come prepared for a schedule packed with great content and actionable insights directly from the teams that maintain some of the ecosystem's most popular open source projects. The program will cover the latest learnings on implementing scalable zero-trust, scanning workloads for improved cloud native security, using service mesh to ensure high availability across multi-cluster infrastructure, and delivering "serverless" for multi-cloud deployments.

### Program overview

**Using cert-manager to enable zero-trust identities for intra-pod communication --- _Jake Sanders, cert-manager maintainer_**

Modern cloud native architectures require the network to be considered untrustworthy and this is why internal workloads are rapidly driving the use of mTLS and private PKI. This workshop from Jetstack will demonstrate how to use cert-manager to issue, manage and rotate mTLS certs, allowing users to have strongly attested and verified Machine Identities between Kubernetes pods. All without the workload private keys leaving node memory! Think of this session as a precursor to implementing a service mesh solution, using cert-manager to establish zero trust environments, perhaps defined by trust domains, and enforce security for pod to pod traffic.

**Multi-cluster failover using Linkerd --- _Eliza Weisman, Linkerd maintainer_**

Failover across clusters is a great way to improve the overall uptime and reliability of Kubernetes applications. While whole-cluster failover can be accomplished at the global ingress layer, failing over individual services is a little more difficult. During this session, Linkerd maintainer Eliza Weisman will walk you through how to use Linkerd, the CNCF graduated service mesh, to enable traffic failover for individual services across clusters. Attendees will learn how to combine service mesh metrics, traffic shifting, and cross-cluster communication in a cohesive and automated way using pure open source, while preserving fundamental security guarantees such as mutual TLS.

**Optimizing and Securing Kubernetes Workloads with Polaris and Goldilocks --- _Rachel Sweeney, Fairwinds and Andy Suderman, Polaris and Goldilocks maintainer_**

Learn how to scan your Kubernetes workloads to improve your resource utilization and security using open source tools Polaris and Goldilocks. You will watch Andy Suderman, Director of R&D and Technology, and Rachel Sweeney, SRE at Fairwinds, as they show how to correctly configure your clusters based on Kubernetes' best practices for security and efficiency.

**Using Kubernetes to deliver a “serverless” service --- _Lisa-Marie Namphy and Jim Walker, Cockroach Labs_**

In this talk, Cockroach Labs team members will share how they leverage Kubernetes to deliver a "serverless" experience. Serverless promises to change the way we consume software. It allows us to potentially pay for what we use only and help drive down operational costs by minimizing resource consumption. Architecting for serverless requires a unique look at app logic and how it is deployed---a combination of the logical and physical worlds. An architectural pattern has emerged where we can scale ephemeral compute separate from services that need to persist.

**Multi-cloud, single deploy: cloud engineering with Kubernetes and Pulumi --- _Aaron Friel and Guinevere Saenger, Pulumi_**

Business constraints and customer requests often require to stand up new Kubernetes environments across multiple cloud providers. This growing complexity in computing infrastructure will incur greater operational costs for organizations when coordinating across multiple teams. Pulumi engineers Aaron Friel and Guinevere Saenger will demonstrate standing up Kubernetes clusters, deploying applications, and automating ops tasks by building a CLI using the Pulumi Automation API. These tools empower every engineer---from application developers to site reliability engineers---to be a cloud engineer.

## Join us on May 17

If you're staying in the Americas (or are up for a late-night session) this KubeCon, join us on Tuesday, May 17th starting at 9 am PST/10 am CST/12 pm EST. Enjoy a specifically curated set of sessions, each led by a project maintainer from projects covering modern cloud native security to improving the developer experience. [Register today](https://www.kubecrash.io/)!
