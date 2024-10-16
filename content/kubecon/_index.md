---
title: KubeCon 2024
meta_desc: Discover Pulumi's game-changing Kubernetes solutions at KubeCon booth R1.
meta_image: /images/kubecon/kubecon-meta-24.png
type: page
layout: kubecon

kubernetes_overview:
    title: Ready to streamline your Kubernetes setup?
    description: |
      **Fly to Pulumi booth R1 at KubeCon** and discover how to tame your infrastructure with actual code! We're not just talking YAML alternatives – we're talking a full-blown IaC powerhouse with first-class K8s support across all Pulumi products.

      Don't just manage your infrastructure – engineer it. With Pulumi, you'll bring software development practices to your DevOps, boosting efficiency and reducing errors. Stop by booth R1 and see how Pulumi can transform your Kubernetes workflow!

      Here's why Pulumi is turning heads:

superpowers:
    - title: Powerful Native Kubernetes Provider
      icon_type: provisioning
      description: |
        - Pulumi IaC offers a native Kubernetes provider more powerful and flexible than any Terraform alternative
        - Full support for CustomResourceDefinitions, ConfigGroups, and ConfigFiles, enabling complex K8s setups

    - title: Faster Updates and Deployment
      icon_type: delivery
      description: |
        - Aims for same-day support of new Kubernetes releases, keeping you on the cutting edge
        - Server-Side Apply (SSA) by default, allowing for more efficient and conflict-free updates

    - title: Enhanced Security and Ease of Use
      icon_type: policy
      description: |
        - Pulumi ESC auto-generates kubeconfig files and enables easy authentication with cloud providers using just-in-time, short-lived credentials
        - Seamlessly integrate kubeconfig from cloud-provisioned clusters, simplifying multi-cloud setups

    - title: Comprehensive Insights and Management
      icon_type: cloud
      description: |
        - Pulumi Insights offers full support for searching, filtering, and importing resources across Kubernetes clusters
        - Brings Kubernetes support to the same level as major cloud providers, enabling unified management and visibility

detail_sections:
    - title: Pulumi at KubeCon North America
      description: |
        Pulumi streamlines Kubernetes cluster configuration, management, and app workload deployments to your clusters.
      items:
          - title: RSVP to “Down the Rabbit Hole” 
            icon: security
            icon_color: violet
            description: with Pulumi, Oso and Apollo GraphGL for an evening of mountain magic Wednesday, November 13, 8-10pm MT at Lake Effect, 155 W 200 S, Salt Lake City
            link: https://lu.ma/qzgd18gp
            cta: RSVP to Happy Hour

          - title: Request a 1:1 demo
            icon: pen
            icon_color: yellow
            description: See how Pulumi can help you ship infrastructure faster and manage your AWS resources at scale.  Reserve your time today.
            link: https://info.pulumi.com/kubecon-na?hs_preview=KRDQSZjg-181026154277
            cta: Schedule a Meeting

          - title: "Pulumi and Kubernetes:  Better Together"
            icon: team
            icon_color: salmon
            description: |
              Nov 18, 2024 9 am PT/Noon ET

              Presented by:  Josh Kodroff

              Learn how to use Pulumi's integrations with Kubernetes to ensure that your clusters and containerized workloads are managed with maximum ease and efficiency!
            link:
            cta: RSVP for Kubernetes Workshop


contact_us_form:
    section_id: contact
    hubspot_form_id: 30017141-1093-4b94-b0eb-20aabc08447b
    headline: Want a demo?
    quote:
        title: See why the world’s best engineering teams use Pulumi + Kubernetes to enable true collaboration between developers and operators.
        name: Fernando Carletti
        name_title: Head of DevOps, Credijusto
        content: |
            Pulumi enables our teams to deploy, scale and manage Kubernetes clusters in a fraction of the time that it took them previously, by giving them the ability to work with the languages they already know, bypassing YAML and unwieldy DSLs. It helps bring together application and infrastructure developers by eliminating silos and reducing friction in their workflows and interactions. We're excited that Pulumi Crosswalk for Kubernetes will simplify our infrastructure provisioning even further, advancing application lifecycle management throughout our organization.

links:
    items:
        - heading: "RSVP to Meetup: Development & Data Productivity in the Age of AI"
          description: Join Docker, Pulumi, Tailscale, and New Relic for drinks, snacks, and casual conversations.<br/><b>Limited Spots Remaining</b><br/>Thursday, March 21 - 6:00 PM at Tonton Becton
          action: Reserve your spot
          link: https://www.eventbrite.com/e/docker-meetup-at-kubecon-development-data-productivity-in-the-age-of-ai-tickets-850415043287
        - heading: Request a Demo
          description: See how Pulumi can help you ship infrastructure faster, and manage Kubernetes clusters at scale on all major cloud providers. Ready for a change?
          action: Talk with an engineer
          link: https://info.pulumi.com/kubecon-europe/

workshops:
    items:
      - title: Getting Started with Kubernetes on AWS
        location: virtual
        datetime: 2024-03-25T09:00:00.000-07:00
        description: In this workshop, you will learn the fundamentals of setting up EKS clusters on AWS through guided exercises using Pulumi.
        link: /resources/getting-started-with-kubernetes-aws/
        action: Register Now
      - title: Getting started with Kubernetes on AKS with Pulumi
        location: virtual
        datetime: 2024-03-26T09:00:00.000-07:00
        description: Learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi's IaC platform and deployment on Azure.
        link: /resources/getting-started-with-kubernetes-aks/
        action: Register Now
      - title: Streamlining AI/ML Workflows on GKE with Pulumi
        location: virtual
        datetime: 2024-03-28T09:00:00.000-07:00
        description: Learn to harness the capabilities of GPUs and TPUs effortlessly, empowering data scientists to focus on model development rather than infrastructure management.
        link: /resources/streamlining-ai-ml-gke-pulumi/
        action: Register Now
      - title: From Zero to Production in Kubernetes
        location: on-demand
        description: Explore how to leverage the power of Python with Pulumi, an infrastructure as code platform to define and manage your Kubernetes deployments.
        link: /resources/from-zero-to-production-in-kubernetes/
        action: Watch

templates:
    items:
        - heading: Kubernetes Cluster Templates
          description: Deploy Kubernetes clusters and their associated infrastructure on AWS, Azure, or Google Cloud Platform.
          image: /images/kubecon/templates-kubernetes-cluster.png
          action: Try it
          link: /templates/kubernetes
        - heading: Kubernetes Application Templates
          description: Build and deploy applications with programming languages and deploying them to your Kubernetes clusters.
          image: /images/kubecon/templates-kubernetes-application.png
          action: Try it
          link: /templates/kubernetes-application
        - heading: Container Service Templates
          description: Pulumi program templates are the fastest way to deploy container services on AWS, Azure, or Google Cloud Platform.
          image: /images/kubecon/templates-container-service.png
          action: Try it
          link: /templates/container-service

knowledge:
    items:
        - link: /resources/infrastructure-as-software-best-practices/
          image: /images/video-thumbnails/infrastructure-as-software-best-practices-thumbnail.png
        - link: /resources/ci-cd-pipelines-for-kubernetes-apps-with-codefresh/
          image: /images/video-thumbnails/gitops-with-pulumi-codefresh-thumbnail.png

customer_logos:
  title: Trusted by your peers
  logos:
    - name: mercedes-benz
      link: /case-studies/mercedes-benz
    - name: snowflake
      link: /case-studies/snowflake
    - name: lemonade
      link: /case-studies/lemonade
    - name: cockroach-labs
    - name: meta
    - name: webflow
    - name: bluenile
    - name: dutchie
      link: https://youtu.be/X1qetq7PjjY
    - name: panther-labs
      link: /case-studies/panther-labs
    - name: univision
    - name: washington-trust
      link: https://youtu.be/Q63ZaX340M4
    - name: nubank
    - name: docker

---
