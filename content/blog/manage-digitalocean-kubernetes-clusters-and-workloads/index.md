---
title: Manage DigitalOcean Kubernetes Clusters and Workloads
h1: "Manage DigitalOcean Kubernetes Clusters and Workloads using Infrastructure as Code"
authors: ["joe-duffy"]
tags: ["digitalocean", "kubernetes"]
meta_desc: "We've partnered with DigitalOcean to publish a new tutorial showing how to provision a Kubernetes cluster, deploy an app to it, and assign a stable domain."
date: "2019-09-30"

meta_image: "digitalocean-kubernetes.png"
---

We recently partnered with DigitalOcean to publish a new tutorial, [*How to Manage DigitalOcean and Kubernetes Infrastructure with Pulumi*](https://www.digitalocean.com/community/tutorials/how-to-manage-digitalocean-and-kubernetes-infrastructure-with-pulumi). This short tutorial walks you through provisioning a new DigitalOcean Kubernetes cluster, deploying an application to it, and then assigninging a stable domain name to your application's load balancer &mdash; all in a handful of lines of infrastructure as code.

By using infrastructure as code to provision and update your infrastructure, it's easy to create new environments, modify or scale existing ones, or automate your deployments using [continuous delivery]({{< prelref "/docs/guides/continuous-delivery" >}}). This approach also ensures that deployments are reliable and repeatable, and can even standardize how you deploy code to different cloud providers, including DigitalOcean, AWS, Azure, GCP, and others.

We regularly talk to developers who appreciate the simplicity of working with DigitalOcean. This new tutorial spins up an entire, fully functioning managed Kubernetes environment in just 6 minutes, for instance, giving you more time to focus on application logic and less on your infrastructure configuration. In addition to managing Kubernetes clusters and applications, you can also provision Droplets, LoadBalancers, and any other DigitalOcean resource type, using a similar infrastructure as code approach. For more information on doing so, read [Getting Started on DigitalOcean with Pulumi]({{< prelref "/blog/getting-started-on-digitalocean-with-pulumi" >}}).

Finally, for more detailed information on all of the DigitalOcean resources supported, please consult the [DigitalOcean API docs]({{< prelref "/docs/reference/pkg/digitalocean" >}}).

Most importantly, [have fun getting up and running with DigitalOcean Kubernetes in just a few minutes](https://www.digitalocean.com/community/tutorials/how-to-manage-digitalocean-and-kubernetes-infrastructure-with-pulumi)!
