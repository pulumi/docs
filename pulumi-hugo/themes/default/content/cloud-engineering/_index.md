---
# TODO: update these values
title: Cloud Engineering
meta_desc: Apply software engineering practices and tools across infrastructure, development, and compliance teams to tame the complexity of modern cloud applications.

type: page
layout: cloud-engineering

overview:
    title: Software engineering practices made for the cloud
    description: |
        Apply standard software engineering practices and tools uniformly across infrastructure, development, and compliance teams to tame the
        complexity of delivering and managing modern cloud applications.

best_practices:
    title: Best practices
    description: |
        Cloud Engineering teams build, deploy, and manage modern cloud applications
        and [infrastructure as software](/what-is/what-is-infrastructure-as-software/)
        written in general purpose languages, including the application logic, cloud infrastructure,
        and cloud policies.

build:
    title: Build
    description: |
        Cloud engineers use cloud resources to build shared services platforms and reusable infrastructure components.
    items:
        - title: Standard Programming Languages
          description: |
            Define infrastructure in Node.js, Python, Go, and .NET and use standard constructs like loops and conditionals. This enables more flexibility
            and reduces complexity compared to domain-specific languages.

        - title: Broad Development Ecosystem
          description: |
            Use programming languages and modern software development tools to increase speed and quality. For example, developers can use IDEs, test frameworks,
            and package managers to build infrastructure.

        - title: Modern Application Development Experience
          description: |
            Build modern architectures (such as Kubernetes or serverless) on multiple clouds using a streamlined, more productive workflow and toolset instead of
            stitching together multiple deployment tools and Bash scripts.

        - title: Share and Reuse Best Practices
          description: |
            Build higher-level frameworks and custom platforms for cloud infrastructure that codify your best practices. Share these best practices within your company
            or with the community.

deploy:
    title: Deploy
    description: |
        Cloud engineers deliver both infrastructure and application code through a unified process that increases efficiency and quality.
    items:
        - title: Unified Infrastructure & Application CI/CD Pipeline
          description: |
            Deliver infrastructure and application code through a single CI/CD pipeline rather than separate pipelines for each. This streamlines versioning, building,
            testing, and deploying cloud applications.

        - title: Test Frameworks for Infrastructure
          description: |
            Run unit and integration tests to validate infrastructure changes before deploying them to production. This encourages a test-driven development approach that
            reduces errors and increases deployment confidence.

        - title: Advanced Deployment Automation
          description: |
            Orchestrate automated deployments by programming them within application code. This enables programmatically deploying infrastructure with APIs instead of
            using a CLI-driven workflow.

        - title: End-to-End Change History
          description: |
            All application and infrastructure changes are tracked with a complete history of who changed what and when. Maintain fine-grained diffs and set up the ability
            to easily roll back changes, if needed.

manage:
    title: Manage
    description: |
        Cloud engineers manage their cloud infrastructure and applications with Policy-as-Code, access controls, and auditing histories.
    items:
        - title: Policy-as-Code
          description: |
            Define Policy-as-Code to proactively enforce compliance across your infrastructure and correct configuration drift. You can write rules that check for security,
            cost, reliability, best practices, and more.

        - title: Auditing and Access Controls
          description: |
            Create visibility across your infrastructure using audit logs and viewing diffs for cloud resource changes, just like in Git. Set fine-grained controls on who can
            access and change infrastructure within your organization.

        - title: Team-wide Visibility
          description: |
            Ensure that your entire team (both infrastructure and developer roles) has visibility across cloud applications, including what resources exist and which changes
            have been made. This builds better collaboration for all.

benefits:
    title: Benefits of<br />Cloud Engineering
    items:
        - title: Unlock the potential of the modern cloud
          icon: lock
          icon_color: purple
          description: |
            Modern cloud architectures, such as Kubernetes, have high innovation potential but are complicated to adopt. Cloud engineering empowers teams to tame this complexity
            with software engineering practices and tools.

        - title: Increase innovation velocity and agility
          icon: lightning
          icon_color: yellow
          description: |
            Cloud engineering democratizes the cloud for developers. By using reusable infrastructure components written in programming languages, developers can more easily
            use the infrastructure they need to build applications faster.

        - title: Decrease infrastructure risks
          icon: alert
          icon_color: salmon
          description: |
            Cloud engineering “shifts risk left” through frequent testing. Every change is reviewed and tested before deployment. Policy-as-Code enforces compliance across every
            deployment, and access controls prevent unauthorized changes.

        - title: Foster closer collaboration
          icon: collab
          icon_color: blue
          description: |
            Cloud engineering breaks down silos between infrastructure, application development, and compliance teams through shared languages, tools, and processes. This
            increases collaboration and efficiency by removing process friction.

use_cases:
    title: Use cases
    description: Learn more about the solutions that are enabled by cloud engineering.
    cta_text: See Solutions
    items:
        - Shared services platforms
        - Greenfield modern applications
        - AI and ML workloads
        - On-premises to cloud migration
        - Migrate from an existing tool

case_studies:
    title: Case studies
    items:
        - company: snowflake
          link: /case-studies/snowflake
          name: Jonas-Taha El Sesiy
          title: Senior Software Engineer
          quote: |
            Ultimately, I think what really excited us about Pulumi was that we could use
            languages that we already know for cloud infrastructure and we knew we could
            solve for future use cases that we hadn’t even thought of yet - all because
            the languages and tools are general-purpose.

        - company: mercedes-benz-rdna
          link: /case-studies/mercedes-benz
          name: Dinesh Ramamurthy
          title: Engineering Manager, Mercedes-Benz Research and Development North America
          quote: |
            I needed a solution that cut across silos and gave our developers a tool they
            could use themselves to provision infrastructure to suit their own immediate needs.
            The way Pulumi solves the multi-cloud problem is exactly what I was looking for.

        - company: credijusto
          link: case-studies/credijusto/
          name: Fernando Carlietti
          title: Lead DevOps Engineer, Credijusto
          quote: |
            Once you use a familiar programming language to tackle a problem, you see that
            you can do way more in less time. Pulumi was a natural choice based on the background
            and skills of our people in DevOps.

        - company: lemonade
          link: case-studies/lemonade/
          name: Igor Shapiro
          title: Principal Engineer at Lemonade
          quote: |
            Pulumi’s Automation API helps us to build on existing best practices and further automate
            our deployment process &mdash; eliminating manual tasks and exception handling.

        - company: hyland
          link: case-studies/learning-machine/
          name:
          title:
          quote: |
            Pulumi is the foundational technology that allowed us to transform our
            organization…Our industry moves with incredible speed and using tools like
            Pulumi are absolutely essential to providing teams with the agility that they require.

        - company: menta
          link: case-studies/menta-network/
          name: Ernesto Mendoza
          title: CTO at Menta Network
          quote: |
            At Menta Network we have a lot of experience with Ansible and Puppet but wanted
            to shift to more modern tools to manage our infrastructure. We tried Terraform but
            found that Pulumi was far easier to use given its Python support. Ultimately, Pulumi
            is just as robust as Terraform and has the added benefit of reducing the complexity
            of managing many configurations and environments.

        - company: sourcegraph
          link: case-studies/sourcegraph/
          name: Beyang Liu
          title: Sourcegraph CTO
          quote: |
            Pulumi has changed how our team works by giving us deployment superpowers. It’s great
            to run ‘pulumi up’ and not have to worry about deploying an invalid configuration.

        - company: fenergo
          link:
          name: Keith Redmond
          title:  VP of SaaS Engineering, Fenergo
          quote: |
            Pulumi improved our time-to-market by removing cloud infrastructure as a roadblock to business innovation. Our developers rely on Pulumi’s Modern Infrastructure as Code and software engineering approach to build modern cloud applications, including the underlying infrastructure, using programming languages they understand. This has resulted in faster software delivery, closer collaboration and higher-quality deployments. Every developer is now empowered to move faster and spend more time on developing things that matter to our customers, which drives a competitive advantage for Fenergo.

get_started:
    title: Get started with Cloud Engineering
    cta_text: Get Started
    description: |
        Pulumi is a cloud engineering platform that brings infrastructure, application
        development, and compliance teams together through a unified software engineering
        process to deliver and manage modern cloud applications
---
