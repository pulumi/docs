---
title: Infrastructure CI/CD
meta_desc: Learn how Pulumi can help you automate the testing, provisioning, and management of infrastructure through a software delivery pipeline.

type: page
layout: solutions-use-case

overview:
    title: Shifting left infrastructure
    image: /images/solutions/git-ops/git-ops-main-diagram.svg
    description: |
        Infrastructure CI/CD (aka Infrastructure Shift Left, GitOps) is the process of automating the testing, provisioning, and management of infrastructure through a software delivery pipeline. This starts with Infrastructure as Code (IaC), which is provisioning and managing infrastructure through definition files (e.g., templates or code) and stored in version control systems. IaC provides automation to provision infrastructure and increases delivery velocity by removing the risk of human errors. Infrastructure CI/CD further automates infrastructure provisioning and management by building the entire IaC process into a CI/CD pipeline. All infrastructure updates run through a standard set of unit and integration tests, allowing reduced errors, greater security, and increased delivery velocity.

benefits:
    title: Why Infrastructure CI/CD?
    benefits:
      title: Benefits
      items:
        - title: Increase release velocity
          icon: code
          icon_color: yellow
          description: |
            Application changes with their corresponding infrastructure changes can all share one automated pipeline, reducing complexity and increasing release velocity.

        - title: Increase reliability
          icon: global
          icon_color: yellow
          description: |
            Every infrastructure update is run through a standard set of unit and integration tests, identifying and addressing bugs earlier and increasing reliability.

        - title: Reduce mean time to resolution
          icon: puzzle
          icon_color: yellow
          description: |
            Small code changes are encouraged which reduces the scale of infrastructure changes and isolates faults, which reduces the mean time to resolution.

    help:
      title: How Pulumi helps
      items:
        - title: Unified delivery pipeline
          icon: rocketship
          icon_color: salmon
          description: |
            Pulumi allows the the same programming languages used for application code to be used for infrastructure. This allows teams to leverage the same testing frameworks and same delivery process for both.

        - title: Shareable infrastructure components
          icon: gear
          icon_color: salmon
          description: |
            Pulumi provides a shared way for teams to collaborate with each other on infrastructure through modular and reusable components that can easily be built and shared across the entire organization.

        - title: Higher order automation
          icon: eye
          icon_color: salmon
          description: |
            You can increase automation across the entire lifecycle of your cloud infrastructure. You can program logic that orchestrates complex workflows during infrastructure provisioning instead of needing to use Bash scripts or glue code. In addition to its CLI, Pulumi provides the Automation API, a programmatic interface for infrastructure as code, so you can build applications that dynamically manage infrastructure.

diagrams:
    title: GitOps Workflow Reference Architecture

    items:
        - title: 1. Pick an execution platform
          image: /images/solutions/git-ops/git-ops-diagram-one.svg
          content: |
            There are many methods by which you can execute a Pulumi program. You need to pick a platform from which Pulumi programs will execute.

        - title: 2. Define the environment/branching strategy
          image: /images/solutions/git-ops/git-ops-diagram-two.svg
          content: |
            Define whether you want one git repo to represent your entire infrastructure or whether you want a stack per branch. The advantage of the former is simplicity while the advantage of the latter is more granularity in control over stack deployments.

        - title: 3. Build the pipelines
          image: /images/solutions/git-ops/git-ops-diagram-three.svg
          content: |
            Based on the branching strategy you chose, you can configure a pipeline per stack or a single pipeline that chooses stacks based on deployment flags.

        - title: 4. Incorporate software development best practices
          image: /images/solutions/git-ops/git-ops-diagram-four.svg
          content: |
            Legacy IaC tools can run in CICD, however with Pulumi, you can incorporate in all the best practice software development practices such as testing. You can design what you want to test in terms of quality issues, deployment issues, and/or code quality checks.

        - title: 5. Define higher-level workflows
          image: /images/solutions/git-ops/git-ops-diagram-five.svg
          content: |
            With Automation API, you can build higher-order orchestration type workflows across all your infrastructure deployments. You can build in serial or branching dependencies that are connected together via StackReferences.

customer_logos:
  title: Organizations practicing infrastructure CI/CD with Pulumi
  logos:
    - name: sans
      link: /case-studies/sans-institute
    - name: skai
      link: /blog/kenshoo-migrates-to-aws-with-pulumi
    - name: atlassian
      link: /case-studies/atlassian
    - name: panther-labs
      link: /case-studies/panther-labs
    - name: whylabs
      link: /case-studies/whylabs

get_started:
    title: Getting started

    get_started:
        title: Talk with customer engineering
        description: |
          Schedule some time with our customer engineering team, and we will help you automate your entire infrastructure provisioning and management through a CI/CD pipeline.
        cta_text: Schedule now
---
