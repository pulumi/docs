---
title: "Integrating DevOps and Security in Platform Engineering"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-12-05T07:41:06Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Gain insights from industry leaders on integrating DevOps and security in platform engineering to build scalable, secure, and developer-friendly platforms.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - devsecops
    - platform-engineering
    - devex
    - devops
    - security


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

Platform engineering has transitioned from an emerging trend in DevOps and infrastructure to a critical function for mid-to-large organizations. By 2026, Gartner predicts that 80% of software development companies will have internal platform services and dedicated teams to streamline development processes.
One of the main goals of Platform engineering is to empower developers by providing self-service and autonomy while maintaining guardrails for security, compliance, and reliability. Achieving this balance requires integrating DevOps and security practices, referred to as DevSecOps best practices.
During PulumiUP Europe 2024, the panel of industry experts explored this integration, including:

- Jess Mink, Sr. Director of Platform Engineering at Honeycomb
- Kief Morris, Global Head of Infrastructure Engineering at ThoughtWorks
- Lindsay Jack, VP of Engineering & Security at Snyk
- Nariman Aga-Tagiyev, Application Security Architect at WiseFrog Security
- [Komal Ali](https://www.pulumi.com/blog/author/komal-ali/), Engineering Manager at Pulumi
  
This discussion centered on the core pillars of platform engineering, strategies for aligning DevOps and security, and overcoming challenges to build scalable, secure platforms.

<!--more-->

## In this article:

- [The Core Pillars of Platform Engineering](/blog/integrating-devops-and-security-for-scalable-platform-engineering/the-core-pillars-of-platform-engineering)
- [Aligning DevOps and Security for Secure Platform Engineering](blog/integrating-devops-and-security-for-scalable-platform-engineering/aligning-devops-and-security-for-secure-platform-engineering)
- [Shift Left Security](blog/integrating-devops-and-security-for-scalable-platform-engineering/shift-left-security)
- [Embrace Automation and Standardization](blog/integrating-devops-and-security-for-scalable-platform-engineering/embrace-automation-and-standardization)
- [Prioritize Observability and Monitoring](blog/integrating-devops-and-security-for-scalable-platform-engineering/prioritize-observability-and-monitoring)
- [Foster a Culture of Collaboration](blog/integrating-devops-and-security-for-scalable-platform-engineering/foster-a-culturecof-collaboration)
- [Challenges of Integrating Security in Platform Engineering](blog/integrating-devops-and-security-for-scalable-platform-engineering/challenges-of-integrating-security-in-platform-engineering)
- [Balancing Autonomy and Control](blog/integrating-devops-and-security-for-scalable-platform-engineering/balancing-autonomy-and-control)
- [Driving Adoption and Changing Mindsets](blog/integrating-devops-and-security-for-scalable-platform-engineering/driving-adoption-and-changing-mindsets)
- [Adapting to Evolving Needs and Technologies](blog/integrating-devops-and-security-for-scalable-platform-engineering/adapting-to-evolving-needs-and-technologies)
- [Measuring Success in Secure Platform Engineering](blog/integrating-devops-and-security-for-scalable-platform-engineering/measuring-success-in-secure-platform Engineering)
- [The Future of Secure Platform Engineering](blog/integrating-devops-and-security-for-scalable-platform-engineering/the-future-of-secure-platform-engineering)

## The Core Pillars of Platform Engineering

{{< youtube "WUpyqn1Jfwg?rel=0" >}}

[Platform engineering teams](https://www.pulumi.com/blog/the-guide-platform-engineering-idp-steps-best-practices/) comprise multiple professionals with many responsibilities and focus areas. According to our panel of experts, the core pillars of platform engineering include:

- **[Developer Experience (DevEx)](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/)**: Provide developers with the tools, frameworks, and abstractions they need to be productive and proactive without getting stuck in infrastructure or operational concerns.
- **[Reliability and Scalability](https://www.pulumi.com/blog/pulumi-patterns-and-practices/#an-effective-internal-developer-platform)**: Ensure that the platform and infrastructure can support the organization's needs, with the ability to scale up or down as required.
- **[Security and Compliance](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/)**: Embed robust, accessible security and compliance frameworks into the development lifecycle while making it easy for developers to adhere to these policies.
- **[Automation and Tooling](https://www.pulumi.com/docs/iac/packages-and-automation/automation-api/)**: Leverage [Infrastructure as Code (IaC)](https://www.pulumi.com/product/infrastructure-as-code/) and automation to enforce standardized processes and consistency and reduce cognitive load and manual effort.
- **[Observability and Monitoring](https://www.pulumi.com/product/pulumi-insights/)**: Provide visibility into the platform's health and performance, delivering actionable insights that allow teams to identify and resolve issues quickly.

These pillars work together to create a platform that empowers developers to innovate and deliver value to the organization and customers while maintaining the necessary controls and safeguards.

## Aligning DevOps and Security for Secure Platform Engineering

Integrating security into platform engineering ensures it becomes a proactive part of the development lifecycle and ensures that "[DevSecOps](https://www.pulumi.com/blog/devsecops-strategy-security-automation-tivity-health/)" is not an afterthought but a core consideration.

Key best practices shared by the panel include:

### Shift Left Security

One of the fundamental principles of DevSecOps is to "shift left" - that is, to integrate security earlier in the development process rather than waiting until the end. This can involve activities such as:

- Incorporating security requirements and threat modeling into the initial design phase
- Automating security scans and tests as part of the continuous integration (CI) pipeline
- Providing developers with secure coding guidelines and tools to [identify and remediate vulnerabilities](https://www.pulumi.com/blog/drift-detection/#why-pulumi-cloud-drift-detection-and-remediation)

By addressing security concerns upfront, organizations can reduce the time and cost of remediating issues later in the development lifecycle.

### Embrace Automation and Standardization

Consistency is key. Platform engineering teams should leverage automation and built-in safeguards and security processes. This may include:

- Automating the provisioning of secure infrastructure and application environments
- Implementing Infrastructure as Code (IaC) to define and manage infrastructure in a declarative, version-controlled manner
- Standardizing security controls, policies, and configurations across the platform

By automating these tasks, platform engineering teams can reduce the risk of human error, improve visibility and auditability, and free up developers to focus on building features rather than managing infrastructure.

### Prioritize Observability and Monitoring

Effective security requires visibility into the health and performance of the platform. Platform engineering teams should invest in robust observability and monitoring solutions to:

- [Detect and respond](https://www.pulumi.com/blog/drift-detection/) to security incidents and anomalies in real-time
- [Gain insights](https://www.pulumi.com/product/pulumi-insights/) into the behavior and usage patterns of the platform
- [Identify and address](https://www.pulumi.com/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/#policy-enforcement-ensuring-compliance-and-security) vulnerabilities or misconfigurations proactively

By integrating security-focused monitoring and alerting into the platform, organizations can quickly identify and mitigate threats while also providing developers with the necessary context to understand and address security-related issues.

### Foster a Culture of Collaboration

Platform engineering is often referred to as being the practical application of DevOps practices. Integrating security practices often requires a cultural shift towards collaboration and shared responsibility between all teams in development, operations, and security, thus the name DevSecOps. Platform engineering teams can facilitate this by:

- Involving security stakeholders in the design and planning of platform initiatives
- Providing security training and education to developers to empower them to make informed decisions
- Establishing communication channels and feedback loops between teams

By breaking down silos and fostering communication and a shared understanding of all the required best practices for a robust, secure, and scalable platform, organizations can support the needs of multiple users, from developers, platform engineers, infrastructure architects, and security professionals.

## Challenges of Integrating Security in Platform Engineering

While the benefits of integrating DevOps and security in platform engineering are clear, the journey has expected challenges. Our panel of experts highlighted several key obstacles that organizations may face:

### Balancing Autonomy and Control

The primary goal is to empower developers to be more productive and proactive. However, this autonomy needs to be balanced with necessary security controls and governance measures.

As Jess Mink, Director of Platform Engineering at [Honeycomb](https://www.pulumi.com/blog/observability-with-infrastructure-as-code/), explains: "*It's a delicate balance - you want to make things easy for developers, but you also need to maintain the right level of control and security. It's about finding the right abstractions and interfaces that give developers the freedom they need while still ensuring the platform remains secure and compliant.*"

### Driving Adoption and Changing Mindsets

Integrating security into the platform engineering workflow can often be met with resistance from developers accustomed to moving quickly and may view security as an obstacle to their productivity.

As Nariman, a Software Security Architect, notes: "*The challenge is not just about the tools or the technology - it's about changing the mindset and getting people to understand the importance of security. You need to find ways to motivate developers and make them feel like they're part of the solution rather than just imposing more rules and processes.*"

Effective communication, education, and a focus on the business value of security are key to driving adoption and fostering a culture of shared responsibility.

### Adapting to Evolving Needs and Technologies

As organizations grow and their technology stacks evolve, the demands on the platform engineering team can shift rapidly. Keeping up with these changes, while maintaining a secure and reliable platform, can be a significant challenge.

Lindsay Jack, VP of Engineering for the Platform Division at [Snyk](https://partners.snyk.io/English/solutions/solution/2908/pulumi), explains: "*You might have a platform team that's really good at a certain set of technologies, but then the organization starts moving in a new direction, and suddenly those skills don't match up anymore. It's about being agile and adaptable and making sure you have the right mix of skills and expertise to support the organization's evolving needs*."

Fostering internal mobility, continuous learning, and a flexible, modular platform architecture can help platform engineering teams navigate these changes more effectively.

## Measuring Success in Secure Platform Engineering

Measuring the success of a platform engineering initiative can be a complex as it involves balancing a range of technical, operational, and business-oriented metrics, but also consider human factors. According to our panel, some key metrics to include:

- **Developer Experience**: Metrics such as developer satisfaction surveys, time-to-onboard new developers, and the number of self-service platform capabilities can provide insights into the effectiveness of the platform in supporting developer productivity and autonomy.
- **Reliability and Scalability**: Monitoring service-level objectives (SLOs), incident response times, and the ability to handle increased traffic or user demands can help assess the platform's reliability and scalability.
- **Security and Compliance**: Tracking the number of security incidents, the ratio of security issues found during threat modeling versus post-deployment, and the adoption of security best practices can indicate the platform's security posture.
- **Automation and Tooling**: Metrics like the percentage of infrastructure provisioned through code, the frequency of platform updates, and the time saved through automation can demonstrate the platform's operational efficiency.
- **Observability and Monitoring**: Measuring the effectiveness of observability tools, the time to detect and resolve issues, and the quality of incident reports can [provide insights into the platform's overall health](https://www.pulumi.com/blog/insights-cloud-account-discovery/) and performance.

As Jess Mink emphasizes, it's important to not just collect these metrics, but to use them to drive meaningful action and improvement: "*We actually look at all of those [metric categories] every quarter and write summaries that go up to the executive level. This creates that visibility and shared understanding of problems, so that there's room for movement and change in the right ways.*"

## The Future of Secure Platform Engineering

Software development and infrastructure management are evolving, and the role of platform engineering will only become more critical to support it. By integrating DevOps and security practices, platform engineering teams can create scalable, secure platforms that empower developers to be more productive and innovate, delivering business value.

Learn how Pulumi customers build secure, scalable platforms and empower their development teams:

- **Tivity Health**: [DevSecOps Game-Changer: Security Automation That Delivers Business Results](https://www.pulumi.com/blog/devsecops-strategy-security-automation-tivity-health/)
- **BMW Group**: [Unified and Programmatic Approach to Infrastructure Management at BMW Using Pulumi](https://www.pulumi.com/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/)
- **Lemonade**: [How the DevOps team supports a much larger group of developers](https://www.pulumi.com/case-studies/lemonade/) using by Pulumi to standardize infrastructure components and enforce best practices.

Discover platform engineering best practices in [The Guide to Platform Engineering: 7 Steps to Get It Right](https://www.pulumi.com/blog/the-guide-platform-engineering-idp-steps-best-practices/) and learn  through hands-on workshops on how to apply them by registering to one of our upcoming [platform engineering workshops and Q&A sessions](https://www.pulumi.com/resources/#upcoming).

***Build secure, scalable platforms with confidence—get started with Pulumi today.***
