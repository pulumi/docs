---
title: "The Guide to Platform Engineering: 7 Steps to Get It Right"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-10-22T07:47:03Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Learn platform engineering best practices in this 7-step guide, covering
  security, internal developer portals, self-service, and team-building for scalable
  success

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: platform-engineering-guide.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
  - sara-huddleston
  - josh-kodroff

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
search:
  keywords:
    - platform
    - engineering
    - infrastructure
    - platform engineering
    - infrastructure code
    - developer portals

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

In today’s fast-paced digital landscape, organizations are increasingly adopting platform engineering to optimize their software delivery and operations. Gartner predicts that by 2026, 80% of large software engineering organizations will have platform engineering teams to provide reusable services, components, and tools for application delivery. Additionally, by 2027, 80% of large enterprises will leverage platform engineering to scale DevOps initiatives in hybrid cloud environments effectively.

This shift is driven by the rise of cloud adoption, where many enterprises face the challenge of uncoordinated application teams deploying workloads in different ways across various cloud platforms. This siloed approach often results in a lack of standardization, security risks, and operational inefficiencies.

Platform engineering offers a strategic solution to these issues. This guide provides the essential steps to successfully implement platform engineering, from laying the foundation to scaling internal developer platforms (IDPs) for future growth.

<!--more-->

## On this article:

- [Step 1: Securing Executive Buy-in](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-1-securing-executive-buy-in)
- [Step 2: Staffing the Platform Engineering Team](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-2-staffing-the-platform-engineering-team)
- [Step 3: Defining the Platform Mandate](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-3-defining-the-platform-mandate)
- [Step 4: Implementing the Pre-Production Pipeline](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-4-implementing-the-pre-production-pipeline)
- [Step 5: Embracing Infrastructure as Code](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-5-embracing-infrastructure-as-code)
- [Step 6: Implementing Policy as Code](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-6-implementing-policy-as-code)
- [Step 7: Evolving Towards Self-Service](/blog/the-guide-platform-engineering-idp-steps-best-practices#step-7-evolving-towards-self-service)
- [Frequently Asked Questions (Platform Engineering Concepts & Definitions)](/blog/the-guide-platform-engineering-idp-steps-best-practices#frequently-asked-questions)

## Step 1: Securing Executive Buy-in

{{< youtube "t4c3NOiuhXQ?rel=0" >}}

The first step in your platform engineering journey is securing executive buy-in. This high-level support is essential, as platform engineering teams must create an organization-wide strategy that integrates internal developer portals (IDPs) and self-service capabilities. Leadership needs to understand how platform engineering can address inefficiencies caused by siloed application teams and uncoordinated cloud deployments.

To do this, present a clear roadmap with measurable outcomes, such as improved delivery speed and security. Use metrics like [DORA](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (Deployment Frequency, Lead Time, Mean Time to Recovery) to demonstrate how platform engineering enhances security, standardization, and efficiency. Outline the required resources (headcount, budget, tooling) and align the project with business objectives.

## Step 2: Staffing the Platform Engineering Team

Once you have executive backing, the next step is to assemble your platform engineering team. This team will [develop and maintain your internal developer platform (IDP)](https://www.pulumi.com/blog/developer-portal-platform-teams/), ensuring it offers the organization secure, scalable, and self-service solutions.

Successful platform engineering teams are characterized by a strong customer focus, empathy for the needs of application teams, and the ability to act as the "glue" that binds the organization together. Key roles and responsibilities within the platform team include:

- **Customer-facing roles**: Serve as the primary point of contact for application teams, understanding their needs and advocating for their requirements within the platform.
- **Infrastructure expertise**: Possess deep knowledge of the underlying infrastructure, whether on-premises or in the cloud, to ensure the platform is reliable and scalable.
- **DevOps and automation skills**: Leverage infrastructure as code (IaC) tools and techniques to automate the provisioning and management of the platform.
- **[FinOps](https://www.pulumi.com/blog/finops-with-pulumi/) and cost optimization expertise**: Understand the organization's financial systems and processes to ensure the platform is cost-effective and aligned with budgetary constraints.
- **Software development capabilities**: Develop the platform's core components, including self-service interfaces and reusable infrastructure modules, using best practices in software engineering.

By assembling a team with this diverse set of skills and a customer-centric mindset, you'll be well-positioned to build a platform that truly meets the needs of your application teams.

## Step 3: Defining the Platform Mandate

Next, clearly define the platform team’s mandate to set expectations. This document should outline the platform’s purpose, the services it provides, and how it supports [internal developer portals (IDPs)](https://www.pulumi.com/blog/building-developer-portals/) and self-service capabilities.

The platform mandate should serve as a central reference point for the platform team and its customers, ensuring everyone is aligned on the team's mission and its value. Key elements to include in the platform mandate include:

- **Introduction**: A high-level overview of the platform team's purpose and the organizational outcomes it aims to achieve.
- **Supported systems**: A list of the infrastructure, services, and tools that the platform team is responsible for managing and supporting.
- **Support model**: Details on how application teams can access platform services, including any self-service capabilities and the team's response times for different types of requests.
- **Team structure**: An overview of the platform team's members and their areas of expertise, making it easy for application teams to identify the right point of contact.

A well-defined mandate aligns the team and its customers with the platform’s value and purpose.

## Step 4: Implementing the Pre-Production Pipeline

With a mandate in place, begin building the core capabilities, starting with a pre-production pipeline. This pipeline standardizes how application code moves from development to deployment, emphasizing security and consistency.

Key components of the pre-production pipeline include:

- **Version control**: Implement a centralized version control system to manage application code and infrastructure as code (IaC) configurations.
- **Continuous integration (CI)**: Automate the build and testing of application artifacts, such as container images or deployment packages.
- **Artifact management**: Provide a secure and versioned repository for storing and distributing the application artifacts produced by the CI process.
- **Static analysis**: Integrate tools that can scan application code and dependencies for security vulnerabilities and other issues.
- **Application delivery**: Automate the deployment of application artifacts to pre-production environments, such as staging or testing.

By establishing a standardized pre-production pipeline, you'll ensure that all application teams follow a consistent, secure, and efficient process for getting their code into a production-ready state.

## Step 5: Embracing Infrastructure as Code

Leveraging infrastructure as code (IaC) is crucial for managing the platform’s infrastructure. It enables consistent, scalable, and secure operations by automating the provisioning of resources, monitoring, and enforcing security policies.

Key areas where IaC can be applied within the platform include:

- **Foundational infrastructure**: Provision and manage the underlying cloud resources, such as virtual networks, storage, and compute, that form the platform's foundation.
- **Runtime platforms**: Deploy and configure the runtime environments where application workloads will be executed, such as Kubernetes clusters or serverless functions.
- **Observability and monitoring**: Set up the logging, metrics, and alerting systems that provide visibility into the platform's health and performance.
- **Security and compliance**: Implement security controls, such as [secrets management](https://www.pulumi.com/docs/esc/) and [access policies](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/get-started/), to ensure the platform meets regulatory and organizational requirements.
- **Pipelines and [automation](https://www.pulumi.com/docs/iac/packages-and-automation/automation-api/)**: Use IaC to define and version-control the platform's own deployment and management pipelines, ensuring consistency and repeatability.

With [infrastructure as code](https://www.pulumi.com/docs/pulumi-cloud/), the platform engineering team can ensure reliable, scalable, and secure infrastructure across the organization.

## Step 6: Implementing Policy as Code

Alongside your IaC efforts, it's important to set up a robust policy-as-code framework within your platform. Policy-as-code allows you to enforce security, compliance, and operational policies programmatically. This provides governance at scale, ensuring all teams follow the same rules.

Policy as code can be applied in two key ways:

- **Preventative controls**: Implement policies that proactively validate and reject non-compliant infrastructure changes before they are provisioned, providing fast feedback to application teams.
- **Detective controls**: Establish policies that continuously monitor the deployed infrastructure, triggering alerts or remediation actions when deviations from the desired state are detected.

By combining [IaC and policy as code](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/) with self-service provisioning, you maintain security and compliance while giving teams autonomy.

## Step 7: Evolving Towards Self-Service 

As your platform matures, the ultimate goal is to empower your application teams with self-service capabilities, allowing them to provision the infrastructure and resources they need quickly and autonomously. This self-service model can take various forms, from pre-defined infrastructure modules to fully automated deployment pipelines.

When implementing self-service capabilities, keep the following platform engineering best practices in mind:

- **Start small and iterate**: Don't try to boil the ocean. Begin with a few well-defined use cases, such as CI/CD pipelines or database provisioning, and gradually expand the self-service offerings as your platform team gains experience and confidence.
- **[Focus on user experience](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/)**: Ensure that the self-service interfaces, whether web-based or command-line, are intuitive and easy to use. Gather feedback from application teams and continuously refine the user experience.
- **Maintain stability and reliability**: Even with self-service, the platform team is responsible for ensuring the underlying infrastructure and services remain stable and reliable. Implement robust monitoring, alerting, and incident response processes to maintain platform health.
- **Embrace a product mindset**: Treat the [platform as a product](https://www.pulumi.com/blog/platform-engineering-cncf-maturity-model/#platforms-as-products-driving-success), with the application teams as your customers. Continuously gather feedback, measure key performance indicators, and iterate on the platform's capabilities to meet evolving needs.

By gradually transitioning towards a self-service model, you'll empower your application teams to move faster while maintaining the necessary guardrails and controls to ensure the platform's long-term success.

## Conclusion: Embracing the Platform Engineering Journey

Building a successful platform engineering strategy involves following a clear roadmap. But remember, implementing the platform engineering strategy is a journey, not a destination. By following the steps outlined in this guide, you'll be well on your way to building a robust, secure, scalable, and customer-centric internal developer platform (IDP) that empowers your organization to deliver software more efficiently and effectively.

With the right approach and mindset, your platform engineering efforts will become a strategic enabler for your organization's digital transformation.

***Build secure, scalable platforms with confidence—[register for the Platform Engineering Course](https://info.pulumi.com/platform-engineering-workshop-series)***

---

## Frequently Asked Questions

### What is Platform Engineering?

There are many definitions for platform engineering, one of which is designing, building, and maintaining internal platforms that streamline software delivery by providing reusable tools, services, and workflows for developers. It focuses on scalability, efficiency, and self-service capabilities for internal teams. 

For a more in-depth explanation of real-world use cases, see [What is platform engineering](https://www.pulumi.com/what-is/what-is-platform-engineering/).

### Who are the Platform Customers?

The platform customers are the end users, typically internal teams (e.g., application developers and DevOps engineers), who use the platform's tools and services to build, deploy, and manage software.

### What is an Internal Developer Platform (IDP)?

A centralized platform that offers developers the tools and environments they need to build, test, and deploy applications. It abstracts away the complexity of underlying infrastructure, allowing teams to focus on coding and delivery.

### What is a Platform Team?

The platform engineering team is a dedicated group of engineers responsible for managing the internal platform. They ensure the platform meets the needs of the organization, providing reliability, security, and scalability.

### What is a Self-Service Infrastructure?

A platform feature that allows development teams to provision, configure, and manage infrastructure resources on demand without relying on other teams, fostering agility.

### What is Infrastructure as Code (IaC)?

The process of managing and provisioning infrastructure through code, allowing infrastructure to be versioned, automated, and managed consistently across environments.

For a more in-depth explanation, see the [What is Infrastructure as Code? page](https://www.pulumi.com/what-is/what-is-infrastructure-as-code/).

### What is Policy as Code (PaC)?

Policy as Code (PaC) defines security, compliance, and [operational policies](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/core-concepts/) in code to automate their enforcement across infrastructure and application deployments.

### What is Developer Experience (DevEx)? 

The overall experience developers have with using the platform, tools, and workflows provided by platform engineering. Optimizing DevEx ensures that developers can work more efficiently and effectively.

For a more in-depth explanation, read [Beyond Productivity: Developer Experience is Business Critical.](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/)
