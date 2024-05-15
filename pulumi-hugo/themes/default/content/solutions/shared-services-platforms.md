---
title: Shared Services Platforms
meta_desc: Learn how Pulumi can help you build and manage a Shard Services Platform that allows application developers to self-service their infrastructure environments.

type: page
layout: solutions-use-case

overview:
    title: Building self-service infrastructure environments
    image: /images/solutions/shared-services-platform/ssp-main-diagram.svg
    description: |
        A Shared Services Platform (aka Internal Developer Portal or Infrastructure Platform) is an internal company service that allows application developers to self-service infrastructure environments. SSPs are an extremely common amongst companies that have reached a certain size where they want to share common infrastructure and automate the provisioning of infrastructure for the development teams. Kubernetes (K8s) is becoming the de facto control plane for modern clouds, and it is frequently employed to power these internal platforms. The goal of a SSP is to increase developer velocity while maintaining centralized control over security, networking, compliance, and costs. Pulumi makes it easy to model and provision the SSP control plane as well as automate the provisioning of the data plane stacks.

benefits:
    title: Why Shared Services Platforms?
    benefits:
      title: Benefits
      items:
        - title: Centralized control
          icon: code
          icon_color: yellow
          description: |
            Companies maintain centralized control over security, networking, compliance, and costs.

        - title: Direct infrastructure access
          icon: global
          icon_color: yellow
          description: |
            Developers can directly access and deploy to infrastructure (e.g., K8s clusters or cloud resources) without contacting operations/cluster managers.

        - title: Start easily
          icon: puzzle
          icon_color: yellow
          description: |
            Developers can get started easily and do not have to adapt their workflows.

    help:
      title: How Pulumi helps
      items:
        - title: Languages you love
          icon: rocketship
          icon_color: salmon
          description: |
            Pulumi allows infrastructure or platform engineering teams to use the programming languages they already use for modeling their infrastructure. They can take advantage of all the existing testing tools, IDE plugins that are standard to their programming languages.

        - title: Build on any cloud
          icon: gear
          icon_color: salmon
          description: |
            Pulumi can provision any resource available in the K8s API. Pulumi supports all new resources and features in the K8s API on the same day as the release. Pulumi allows K8s users novel forms of cluster management and app workload deployments.

        - title: Programmable guardrails
          icon: eye
          icon_color: salmon
          description: |
            Pulumi also enables “policy as code”, which allows the platform team to enforce cost, security, and best practices across all infrastructure.

        - title: Reusable components
          icon: team
          icon_color: salmon
          description: |
            Pulumi makes creating reusable and modular components easy which allows repeatable infrastructure building blocks to be templatized and easily reused.

diagrams:
    title: Kubernetes Platform Reference Architecture

    items:
        - title: 1. Define your goals
          image: /images/solutions/shared-services-platform/diagram-one.svg
          content: |
            Define your business goals you want to achieve by building a K8s platform. Your goals will determine what features to include or not include in your platform.

        - title: 2. Define the platform
          image: /images/solutions/shared-services-platform/diagram-two.svg
          content: |
            A good starting point for your internal Kubernetes platform is to use just a single environment that reflects the environment of your production system best. You want to first define the common infrastructure components/resources that will be shared across the platform and by all the developers (end users). Then you want to define the infrastructure components/resources that are configured and managed by the developer. Finally define the boundary between the platform space and end user space, which is how the developer will access the shared resources (e.g., via StackReference).

        - title: 3. Define how developers consume the platform
          image: /images/solutions/shared-services-platform/diagram-three.svg
          content: |
            Define how developers will interact with the platform. You may want to give them a self-service portal where they can pick and choose their infrastructure, a GitOps workflow, or developers just interact with a CI/CD pipeline directly.

        - title: 4. Build the components, blueprints, & pipelines
          image: /images/solutions/shared-services-platform/diagram-four.svg
          content: |
            Write code for the shared platform components first. Then write code for the application components that can be selected and used by developers. These application components will have the logic to retrieve credentials or connect to the shared resources in the platform.

        - title: 5. Define the guardrails & policies
          image: /images/solutions/shared-services-platform/diagram-five.svg
          content: |
            Use Pulumi CrossGuard to define cost guardrails and security policies. CrossGuard can also be used to enforce general best practices (e.g., closing ports) or best practices specific to your business (e.g., regional locality requirements).

customer_logos:
  title: Organizations building shared services platforms with Pulumi
  logos:
    - name: mercedes-benz
      link: /case-studies/mercedes-benz
    - name: snowflake
      link: /case-studies/snowflake
    - name: lemonade
      link: /case-studies/lemonade

get_started:
    title: Getting started

    get_started:
        title: Talk with customer engineering
        description: |
          Schedule some time with our customer engineering team, and we will help you plan and build your shared services platform.
        cta_text: Schedule now
---
