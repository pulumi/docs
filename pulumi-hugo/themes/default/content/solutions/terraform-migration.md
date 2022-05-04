---
title: Terraform Migration
meta_desc: Learn how Pulumi can help you manage a Terraform migration to increase velocity and reliability of deploying and managing modern cloud architectures.

type: page
layout: solutions-use-case

overview:
    title: Modernizing infrastructure management for the modern cloud
    image: /images/solutions/terraform/terraform-main-diagram.svg
    description: |
        Terraform Migration (aka IaC modernization) is the process of modernizing how your teams provision and manage infrastructure in order to adapt to the changes in technologies (containers, serverless), architectures (distributed), and software release automation associated with the cloud. Managing modern applications and infrastructure requires the coordination of many complex dependencies between services in distributed cloud architectures. There are also many common infrastructure resources that must be shared across the organization. Managing cloud infrastructure requires automation to increase complexity, testing to reduce errors, modularity to encourage sharing and reuse, and policy enforcement to manage risk. The goal of Terraform migration is to increase velocity and reliability of deploying and managing modern cloud architectures. Pulumi is purpose built to handle the scale, complexity, and delivery velocity needed for the modern cloud.

benefits:
    title: Benefits of Migrating from Terraform to Pulumi
    benefits:
      items:
        - title: Bring software development practices to infrastructure
          icon: code
          icon_color: yellow
          description: |
             With Pulumi, you can incorporate software development best practices such as code reviews, testing, policy checks into your infrastructure management process. Pulumi allows you to increase automation and velocity while reducing copy and paste as well as manual errors.

        - title: Higher order automation
          icon: eye
          icon_color: yellow
          description: |
            You can increase automation across the entire lifecycle of your cloud infrastructure. You can program logic that orchestrates complex workflows during infrastructure provisioning instead of needing to use Bash scripts or glue code. In addition to its CLI, Pulumi provides the Automation API, a programmatic interface for infrastructure as code, so you can build applications that dynamically manage infrastructure.

        - title: Shareable and reuseable infrastructure
          icon: puzzle
          icon_color: yellow
          description: |
            Pulumi allows you to create reusable infrastructure that can be shared and reused by anyone in any language. You can build and share components for commonly used architectures or shared resources with organizational best practices. With Pulumi, you can write your components once in your preferred language and make them available in all the other languages supported by Pulumi.

    help:
      items:
        - title: Fully integrated secrets management
          icon: security
          icon_color: violet
          description: |
            Pulumi provides first class support for secrets so you can confidently store values that contain sensitive data, such as database passwords or service tokens. Pulumi automatically tracks your secrets across your program’s execution and ensure that secret values are encrypted in the state file and never exposed as plain text.

        - title: Empower developers
          icon: gear
          icon_color: violet
          description: |
            Pulumi increases the accessibility and reduces the complexity of the modern cloud. Developers can just use the standard programming languages they already know like Typescript, Python, C#, Go, and Java as well as their existing tools like IDEs and test frameworks. Pulumi makes the cloud easily accessible to your developers without them having to wait on infrastructure from the operations teams. They can develop and release features faster.

        - title: Full support of the modern cloud
          icon: global
          icon_color: violet
          description: |
            Pulumi enables you to program the full surface area of the modern cloud (e.g., AWS, Azure, Google Cloud, Kubernetes). All newly-released services and features are supported the same day.

diagrams:
    title: Terraform Migration Reference Architecture
    items:
        - title: 1. Catalog all infrastructure stacks
          image: /images/solutions/terraform/terraform-diagram-one.svg
          content: |
            Identify all the Terraform stacks that are currently in production.

        - title: 2. Identify which stacks need to be modernized
          image: /images/solutions/terraform/terraform-diagram-two.svg
          content: |
            Identify all the stack that you want modernized. There are two strategies to this:  you can either pick the highest value stacks or the lowest risk stack to move and focus on first. The former allows you to get the greatest business benefit while the latter allows you to incrementally build up to the critical pieces.

        - title: 3. Convert Terraform templates to Pulumi programs
          image: /images/solutions/terraform/terraform-diagram-three.svg
          content: |
            There are two options to migrating the identified stacks. You can convert the code for each of the identified stacks or you can read the outputs from a Terraform state file and reference the existing stack from within your Pulumi program. The former allows you to fully take advantage of all the benefits of using Pulumi to manage all your infrastructure. You can either use the [tf2pulumi](/tf2pulumi/) tool to automatically translate HCL to a Pulumi program or you can translate manually. The latter allows you to use Pulumi with existing infrastructure agnostic to the choices other teams have already made.

        - title: 4. Incorporate software development best practices
          image: /images/solutions/terraform/terraform-diagram-four.svg
          content: |
            Legacy IaC tools can run in CICD, however with Pulumi, you can incorporate in all the best practice software development practices such as testing. You can design what you want to test in terms of quality issues, deployment issues, and/or code quality checks.

customer_logos:
  title: Organizations modernizing their infrastructure-as-code with Pulumi
  logos:
    - name: sans
      link: /case-studies/sans-institute
    - name: credijusto
      link: /case-studies/credijusto
    - name: lemonade
      link: /case-studies/lemonade
    - name: atlassian
      link: /case-studies/atlassian

get_started:
    title: Getting started

    get_started:
        title: Talk with customer engineering
        description: |
          Schedule some time with our customer engineering team, and we will help you migrate your Terraform to Pulumi.
        cta_text: Schedule now
---
