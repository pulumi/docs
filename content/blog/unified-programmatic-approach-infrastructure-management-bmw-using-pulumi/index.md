---
title: "Unified and Programmatic Approach to Infrastructure Management at BMW Using
  Pulumi"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-10-03T09:52:10Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Explore how BMW leverages Pulumi for efficient infrastructure management,
  boosting scalability, productivity, and compliance in automotive software development

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: bmw-pulumi-deployments.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
  - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - infrastructure-as-code
  - cloud-management
  - infrastructure-lifecycle-management
  - platform-engineering
  - developer-experience-devex
  - ansible
  - containers
  - pulumi-deployments


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
    - BMW
    - infrastructure
    - infrastructure management
    - software development
    - shared modules

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

In the ever-evolving world of automotive technology, BMW has been at the forefront of innovation, seamlessly integrating software into the heart of their vehicles. As cars become increasingly complex, with a growing emphasis on connectivity, over-the-air upgrades, and brand-specific user experiences, the need for a robust and scalable software development approach has become paramount.

Enter the BMW Software Factory, a platform that aims to empower the company's developers and provide them with a superior development experience. At the core of this initiative is the adoption of Pulumi, a modern infrastructure as code (IaC) solution that has transformed the way BMW manages its software ecosystem.

<!--more-->

## On this article:

- [The Challenges of a Sprawling Software Landscape](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#the-challenges-of-a-sprawling-software-landscape)
- [The Evolution of BMW's Software Development Toolchain](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#the-evolution-of-bmws-software-development-toolchain)
- [Embracing Pulumi: Streamlining Infrastructure Management](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#embracing-pulumi-streamlining-infrastructure-management)
- [The Benefits of Pulumi: Accelerating Development and Improving Maintainability](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#the-benefits-of-pulumi-accelerating-development-and-improving-maintainability)
- [The Future of BMW's Software Factory: Embracing the Cloud](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#the-future-of-bmws-software-factory-embracing-the-cloud)
- [Conclusion: Unlocking the Future of Automotive Software](/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#conclusion-unlocking-the-future-of-automotive-software)

## The Challenges of a Sprawling Software Landscape

{{< youtube "HIliBBo4c-g?rel=0" >}}

[BMW's software journey](https://www.bmwgroup.com/en/news/general/2023/BMWGroupIT.html) has been a testament to the exponential growth of automotive technology. What started with simple engine controllers has evolved into a complex network of electronic control units (ECUs) scattered throughout the vehicle. As the software footprint continues to expand, BMW recognized the need for a unified and efficient approach to software development and deployment.

The company's initial efforts involved introducing a platform called "Code Craft," which provided a comprehensive stack of services to support the software development lifecycle. This stack included a GitHub Enterprise application for source code management, a Gerrit system for Android-based developments, a continuous integration (CI) pipeline, artifact stores, build caching, and various other tools and services.

However, as the demand for software-driven features grew, the complexity of managing this sprawling ecosystem became increasingly challenging. BMW found itself grappling with the need to scale its infrastructure, navigate network limitations across multiple data centers, and adapt to the ever-changing landscape of cloud computing.

## The Evolution of BMW's Software Development Toolchain

BMW's journey to streamline its software development process has been gradual and iterative. The company's initial approach involved using [Ansible](https://www.pulumi.com/docs/iac/concepts/vs/chef-puppet-etc/) for deployment and a custom-built deployment scripting solution for its OpenShift cluster.

As the complexity of the platform increased, BMW turned to Helm and Kubernetes to manage its containerized services. However, as the company ventured into the public cloud, the limitations of these tools became apparent. The team recognized the need for a more comprehensive and scalable solution to manage their infrastructure as code.

At this critical juncture, BMW discovered Pulumi. This modern IaC solution offered a unique advantage – the ability to leverage a full-fledged programming language, Python, to define and manage their infrastructure. This shift proved to be a game-changer, allowing BMW to leverage its expertise in Python and benefit from the rich ecosystem of libraries and tools available in the Python community.

## Embracing Pulumi: Streamlining Infrastructure Management

[BMW's adoption of Pulumi](https://www.pulumi.com/case-studies/bmw/) was a strategic move that aimed to address the growing complexity of its software ecosystem. By transitioning from a patchwork of tools to a unified IaC solution, the company was able to streamline its infrastructure management and improve developer productivity.

### Shared Modules: Promoting Reusability and Best Practices

One of BMW's key initiatives was developing a shared modules library, which allowed the team to abstract the complexity of various infrastructure components, such as databases, and provide a consistent and user-friendly interface for their developers.
- By leveraging [Pulumi's Python](https://www.pulumi.com/docs/iac/languages-sdks/python/) bindings, BMW was able to create reusable modules that encapsulated best practices and sensible defaults, making it easier for developers to provision and manage infrastructure resources.
BMW used Pydantic, a data validation library, to define schema-based configurations for its infrastructure. These were then integrated into its IDEs, providing developers with auto-completion and validation support.
- This approach not only accelerated the development process but also ensured that the infrastructure deployed across the organization adhered to consistent security and compliance standards.

### Transformation Features: Protecting Legacy Services

- As part of their software factory, BMW also faced the challenge of integrating legacy services that did not natively support modern authentication and authorization mechanisms, such as [OpenID Connect (OIDC)](https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/provider/).
- To address this, BMW leveraged Pulumi's transformation features to seamlessly inject an [OAuth2](https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/client/#exchanging-oidc-tokens) proxy into their deployments, providing a secure and consistent way to protect these services without requiring extensive modifications to the underlying applications.
- By encapsulating this functionality within a shared module, BMW was able to apply the OAuth2 proxy to multiple services, ensuring a consistent and secure access control layer across their software ecosystem.

### Policy Enforcement: Ensuring Compliance and Security

One key benefit of [Pulumi's IaC approach](https://www.pulumi.com/product/infrastructure-as-code/) is the ability to define and enforce policies across the organization, ensuring that infrastructure deployments adhere to security and compliance standards.
BMW has leveraged [Pulumi's policy-as-code](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/) capabilities to implement mandatory checks, such as ensuring that all S3 buckets are encrypted at rest, preventing the deployment of non-compliant resources.
- By integrating these policy checks into their deployment workflows, BMW has shifted security and compliance concerns to the left, addressing issues early in the development process and reducing the risk of costly post-deployment [remediations](https://www.pulumi.com/blog/remediation-policies/).

## The Benefits of Pulumi: Accelerating Development and Improving Maintainability

BMW's adoption of Pulumi has yielded significant benefits, transforming the way the company approaches software development and infrastructure management.

### Accelerated Development with Shared Modules

The implementation of shared modules has been a game-changer for BMW. It allows developers to leverage pre-built and tested infrastructure components without having to reinvent the wheel. This has resulted in a significant acceleration of the development process, as teams can focus on building their applications rather than grappling with the complexities of infrastructure provisioning.

### Improved Maintainability and Consistency

By centralizing infrastructure management within the shared modules, BMW has ensured that best practices and security standards are consistently applied across the organization. This has not only improved the overall maintainability of the software ecosystem but has also reduced the risk of security and compliance violations.

### Leveraging Python's Ecosystem

BMW's decision to leverage Pulumi's Python bindings has been a strategic advantage, as the company was able to tap into the rich ecosystem of Python libraries and tools. This has enabled the team to seamlessly integrate Pulumi with their existing Python-based toolchain, including dependency management, testing frameworks, and code quality tools, further enhancing the development experience.

### Streamlined Cloud Migration

As BMW continues to expand its use of public cloud services, Pulumi has played a crucial role in simplifying the [migration process](https://www.pulumi.com/migrate/). By providing a consistent IaC approach across on-premises and cloud environments, Pulumi has enabled BMW to manage its infrastructure in a unified manner, reducing the complexity and overhead associated with [multi-cloud deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/).

## The Future of BMW's Software Factory: Embracing the Cloud

Looking ahead, BMW's Software Factory is poised to take the next step in its evolution, with plans to transition away from the self-hosted backend and embrace cloud-native services. This strategic move aims to further improve [developer productivity](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/) and reduce the internal effort required to maintain the underlying infrastructure.

By leveraging the expertise and reliability of cloud service providers, BMW can focus on delivering innovative software features to their customers while the cloud providers handle the operational aspects of running the necessary services.

As BMW continues to push the boundaries of automotive software, Pulumi's role in its Software Factory will only become more crucial. By providing a scalable and flexible IaC solution, Pulumi empowers BMW's developers to innovate with confidence and be secure in the knowledge that their infrastructure is managed consistently and in alignment with the company's [security and compliance standards](https://www.pulumi.com/resources/security-automation-faster-cheaper-better/).

## Conclusion: Unlocking the Future of Automotive Software

BMW's journey with Pulumi in the Software Factory showcases the power of modern IaC solutions in navigating the complexities of the automotive software landscape. By embracing a unified and programmatic approach to infrastructure management, BMW has accelerated development, improved maintainability, and ensured compliance across its sprawling software ecosystem.

As the automotive industry continues to evolve, with cars becoming increasingly software-driven, the lessons learned by BMW can serve as a blueprint for other organizations looking to streamline their software development and deployment processes. By leveraging the capabilities of Pulumi and other cutting-edge technologies, the future of automotive software is poised to be more efficient, secure, and responsive to the ever-changing needs of both manufacturers and consumers.

To learn more about Pulumi and how it can transform your software development and infrastructure management:
- Get started with [Pulumi Tutorials](https://www.pulumi.com/tutorials/)
- Attend an [upcoming workshop](https://www.pulumi.com/resources/#upcoming)
- Try out the [Pulumi AI](https://www.pulumi.com/ai) code assistant to accelerate your infrastructure as code journey
