---
title: "The Guide to Platform Engineering, Idp: 7 Steps to Get It Right"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-09-12T09:47:03Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: platform engineering guide and stuff

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston
    - josh-kKodroff

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - platform-engineering
    - developer-portals
    - policy-as-code
    - finops
    - cost-efficiency
    
# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Organizations increasingly turn to platform engineering to streamline their software delivery and operations in today's fast-paced digital landscape. As cloud adoption continues to soar, many enterprises grapple with a proliferation of uncoordinated application teams, each deploying their workloads in different ways across various cloud platforms. This siloed approach can lead to a lack of standardization, security vulnerabilities, and operational inefficiencies.

Enter platform engineering, a strategic organizational pattern that addresses these challenges head-on. This comprehensive guide will explore the critical steps to implementing a successful platform engineering strategy, from laying the groundwork to scaling your internal developer platforms for the future.

<!--more-->

## On this article:

- Platform Engineering Concepts
- Step 1: Securing Executive Buy-in

## Platform Engineering Concepts

stuff stuff stuff

## Step 1: Securing Executive Buy-in

The first and arguably most crucial step in your platform engineering journey is to secure buy-in from executive leadership. This high-level support is essential, as platform engineering often requires a top-down approach to reign in the chaos of uncoordinated application teams and establish a cohesive, organization-wide strategy.

When pitching your platform engineering initiative to leadership, be prepared to articulate the measurable outcomes and business benefits it will deliver. Leverage industry-standard metrics like the DORA metrics (deployment frequency, lead time, mean time to recovery, and change failure rate) to demonstrate how your platform will improve software delivery and operational efficiency.

Additionally, be ready to outline the resources required, including headcount, budget, and tooling. Emphasize how the platform team's efforts will ultimately enable application teams to deliver more value to the business, aligning with the organization's strategic goals.

## Step 2: Staffing the Platform Team

With executive buy-in secured, the next step is to assemble your platform engineering team. This team will be responsible for designing, building, and maintaining the organization's internal developer platform, so it's crucial to ensure the right mix of skills and expertise.

Successful platform engineering teams are characterized by a strong customer focus, empathy for the needs of application teams, and the ability to act as the "glue" that binds the organization together. Key roles and responsibilities within the platform team include:

- Customer-facing roles: Serve as the primary point of contact for application teams, understanding their needs and advocating for their requirements within the platform.
- Infrastructure expertise: Possess deep knowledge of the underlying infrastructure, whether on-premises or in the cloud, to ensure the platform is reliable and scalable.
- DevOps and automation skills: Leverage infrastructure as code (IaC) tools and techniques to automate the provisioning and management of the platform.
- Cost optimization and FinOps: Understand the organization's financial systems and processes to ensure the platform is cost-effective and aligned with budgetary constraints.
- Software development capabilities: Develop the platform's core components, including self-service interfaces and reusable infrastructure modules, using best practices in software engineering.

By assembling a team with this diverse set of skills and a customer-centric mindset, you'll be well-positioned to build a platform that truly meets the needs of your application teams.

## Step 3: Defining the Platform Mandate

With your platform team in place, the next step is to clearly define the team's mandate and responsibilities. This involves creating a comprehensive document that outlines the platform's purpose, the systems it supports, and the services it provides to application teams.

The platform mandate should serve as a central reference point for both the platform team and its customers, ensuring everyone is aligned on the team's mission and the value it delivers. Key elements to include in the platform mandate include:

- Introduction: A high-level overview of the platform team's purpose and the organizational outcomes it aims to achieve.
- Supported systems: A list of the infrastructure, services, and tools that the platform team is responsible for managing and supporting.
- Support model: Details on how application teams can access platform services, including any self-service capabilities, and the team's response times for different types of requests.
- Team structure: An overview of the platform team's members and their areas of expertise, making it easy for application teams to identify the right point of contact.

By clearly defining the platform team's mandate and making it publicly accessible, you'll establish a solid foundation for the platform's operations and ensure seamless collaboration between the platform team and its customers.

## Step 4: Implementing the Pre-Production Pipeline

With the foundational elements in place, it's time to start building out the platform's core capabilities. The first step in this process is to establish a robust pre-production pipeline, which encompasses the services and tools required to take application code from development to deployment.

Key components of the pre-production pipeline include:

- Version control: Implement a centralized version control system to manage application code and infrastructure as code (IaC) configurations.
- Continuous integration (CI): Automate the build and testing of application artifacts, such as container images or deployment packages.
- Artifact management: Provide a secure and versioned repository for storing and distributing the application artifacts produced by the CI process.
- Static analysis: Integrate tools that can scan application code and dependencies for security vulnerabilities and other issues.
- Application delivery: Automate the deployment of application artifacts to pre-production environments, such as staging or testing.

By establishing a standardized pre-production pipeline, you'll ensure that all application teams follow a consistent, secure, and efficient process for getting their code into a production-ready state.

## Step 5: Embracing Infrastructure as Code

With the pre-production pipeline in place, the next step is to leverage infrastructure as code (IaC) to manage the platform's post-production components. IaC allows you to define your infrastructure in a declarative, version-controlled manner, enabling greater consistency, scalability, and maintainability.

Key areas where IaC can be applied within the platform include:

- Foundational infrastructure: Provision and manage the underlying cloud resources, such as virtual networks, storage, and compute, that form the platform's foundation.
- Runtime platforms: Deploy and configure the runtime environments where application workloads will be executed, such as Kubernetes clusters or serverless functions.
- Observability and monitoring: Set up the logging, metrics, and alerting systems that provide visibility into the platform's health and performance.
- Security and compliance: Implement security controls, such as secrets management and access policies, to ensure the platform meets regulatory and organizational requirements.
- Pipelines and automation: Use IaC to define and version-control the platform's own deployment and management pipelines, ensuring consistency and repeatability.

By embracing IaC, you'll empower your platform team to manage the platform's infrastructure with the same rigor and automation they apply to application deployments, leading to increased reliability, scalability, and cost optimization.

## Step 6: Implementing Policy as Code

Alongside your IaC efforts, it's crucial to establish a robust policy as code framework within your platform. Policy as code allows you to define and enforce organizational policies and guardrails programmatically, ensuring consistent compliance across all application deployments.

Policy as code can be applied in two key ways:

- Preventative controls: Implement policies that proactively validate and reject non-compliant infrastructure changes before they are provisioned, providing fast feedback to application teams.
- Detective controls: Establish policies that continuously monitor the deployed infrastructure, triggering alerts or remediation actions when deviations from the desired state are detected.

By combining IaC and policy as code, you'll create a platform that not only enables self-service infrastructure provisioning but also ensures that it aligns with your organization's security, compliance, and cost optimization requirements.

## Step 7: Evolving Towards Self-Service 

As your platform matures, the ultimate goal is to empower your application teams with self-service capabilities, allowing them to provision the infrastructure and resources they need quickly and autonomously. This self-service model can take various forms, from pre-defined infrastructure modules to fully automated deployment pipelines.

When implementing self-service capabilities, keep the following best practices in mind:

- Start small and iterate: Don't try to boil the ocean. Begin with a few well-defined use cases, such as CI/CD pipelines or database provisioning, and gradually expand the self-service offerings as your platform team gains experience and confidence.
- Focus on user experience: Ensure that the self-service interfaces, whether web-based or command-line, are intuitive and easy to use. Gather feedback from application teams and continuously refine the user experience.
- Maintain stability and reliability: Even with self-service, the platform team is responsible for ensuring the underlying infrastructure and services remain stable and reliable. Implement robust monitoring, alerting, and incident response processes to maintain platform health.
- Embrace a product mindset: Treat the platform as a product, with the application teams as your customers. Continuously gather feedback, measure key performance indicators, and iterate on the platform's capabilities to meet evolving needs.

By gradually transitioning towards a self-service model, you'll empower your application teams to move faster while maintaining the necessary guardrails and controls to ensure the platform's long-term success.

## Conclusion: Embracing the Platform Engineering Journey

Implementing a successful platform engineering strategy is a journey, not a destination. By following the steps outlined in this guide, you'll be well on your way to building a robust, scalable, and customer-centric internal developer platform that empowers your organization to deliver software more efficiently and effectively.

Remember, the key to success lies in maintaining a relentless focus on your application teams' needs, continuously iterating on the platform's capabilities, and fostering a culture of collaboration and shared ownership. With the right approach and mindset, your platform engineering efforts will become a strategic enabler for your organization's digital transformation.

To learn more about getting started with platform engineering, be sure to check out the upcoming workshops and resources from Pulumi. And if you're ready to dive in, explore the Pulumi documentation for AWS to kickstart your platform engineering journey.
