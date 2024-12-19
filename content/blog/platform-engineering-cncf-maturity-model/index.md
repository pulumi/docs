---
title: "Platform Engineering: Cloud-Native, Maturity Models, and Platforms as Products"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-07-26T17:40:17Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Discover Cloud Native Platforms, the Platform Maturity Model, how to approach Platforms as Products, the CNCF Platform Working Group, and more. Get involved!

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: platform-engineering-dominik-tech-talk-cncf.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - platform-engineering
    - community
    - pulumi-events

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
    twitter: Explore platform engineering essentials! Read the article or watch Dominik Kress's talk on Cloud Native Platforms, the Platform Maturity Model, and managing Platforms as Products.
    linkedin: Explore platform engineering essentials! Read the article or watch Dominik Kress's talk on Cloud Native Platforms, the Platform Maturity Model, and managing Platforms as Products.

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

The Platform Engineering & DevOps in-person series launched in Berlin with two great speakers. This blog article is an overview of Dominik Kress's talk, “What the Heck is the CNCF Platform Working Group? Answers from a Member!” in which he discussed Cloud-Native Platforms, The Platform Maturity Model, and approaching Platforms as Products. 

In this article, you'll learn more about [platform engineering](https://www.pulumi.com/what-is/what-is-platform-engineering/) and how to get involved with the CNCF Platform Working Group. Make sure to check our [Pulumi User Groups (PUGs)](https://www.meetup.com/pro/pugs/) to find a meetup near you.

<!--more-->

## On this platform engineering article:

- [What is a Platform?](/blog/platform-engineering-cncf-maturity-model/#what-is-a-platform)
- [Defining Cloud Native Platforms](/blog/platform-engineering-cncf-maturity-model/#defining-cloud-native-platforms)
- [The Platform Maturity Model: Charting the Path to Success](/blog/platform-engineering-cncf-maturity-model/#the-platform-maturity-model-charting-the-path-to-success)
- [Platforms as Products: Driving Success](/blog/platform-engineering-cncf-maturity-model/#platforms-as-products-driving-success)
- [Frequently Asked Questions](/blog/platform-engineering-cncf-maturity-model/#frequently-asked-questions)

## What is a Platform?

According to CNCF, a platform in cloud-native computing is an integrated collection of capabilities designed to meet users' needs. It serves as a cross-cutting layer, ensuring a consistent experience integrating and managing services and capabilities for various applications and use cases. A good platform provides consistent user experiences through portals, project templates, and self-service APIs.

[Atlassian](https://www.pulumi.com/case-studies/atlassian/) describes platform teams as creators of capabilities used by multiple product teams, reducing their overhead and cognitive load. Martin Fowler and Evan Bottcher define a digital platform as a foundation of self-service APIs, tools, services, and support arranged as an internal product. These platforms enable autonomous teams to deliver features faster with less coordination.

The specific capabilities of a platform are tailored to the needs of its stakeholders and users. While platform teams provide these capabilities, they do not always implement them directly. Managed service providers or dedicated internal teams can maintain the underlying implementations, ensuring consistency across the organization. Platforms are tailored to an enterprise’s internal users and are particularly relevant for cloud-native architectures, separating supporting capabilities from application-specific logic.

## Defining Cloud Native Platforms

{{< youtube "NUPK5CCm6XA?rel=0" >}}

The core of the discussion at the CNCF Platform Working Group is: "What exactly is a cloud-native platform, and why do organizations need one?"
A cloud-native platform is a strategic business initiative that enables organizations to deliver value more efficiently and effectively. It is characterized by:

- **Vendor-neutrality**: A cloud-native platform should be open and agnostic, allowing organizations to leverage various technologies and services without being locked into a single vendor.
**Scalability and flexibility**: The platform should be designed to accommodate the organization's growing and changing needs, with the ability to add or remove components as needed easily.
- **[Developer-centricity](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/)**: The platform should empower developers to be more productive by providing self-service capabilities, streamlined workflows, and a consistent developer experience.
- **[Operational efficiency](https://www.pulumi.com/blog/developer-portal-platform-teams/)**: The platform should simplify and automate the management and maintenance of the underlying infrastructure, allowing the organization to focus on delivering value to customers.
- **Continuous improvement**: The platform should be designed with a mindset of continuous evolution, with regular updates and enhancements to address emerging needs and technologies.
  
By aligning with these principles, organizations can achieve faster time-to-market, improved developer productivity, and reduced operational overhead.

## The Platform Maturity Model: Charting the Path to Success

{{< figure alt="Dominik Kress at the Berlin Pulumi Group meetup explaining the platform maturity model" src="./dominik-platform-engineering-berlin.png" caption="Dominik Kress at the Berlin Pulumi Group meetup explaining the platform maturity model" width=100% >}}

The Platform Working Group has developed a Platform Maturity Model. This framework can help assess the current state of a cloud native platform and identify steps to enhance its maturity. It defines five levels:

- **Ad-hoc**: At the lowest level, the platform is ad-hoc, with no dedicated team or budget and a reliance on individual efforts and workarounds.
- **Operational**: The platform has a dedicated team and budget, which focus primarily on operational tasks and maintenance rather than strategic initiatives.
- **Scalable**: The platform is now viewed as a product with a clear roadmap and a focus on delivering value to internal customers. The platform team has more autonomy and the ability to drive innovation.
- **Enabled**: The platform has become a strategic asset, with a thriving ecosystem of contributors and consumers. The platform team is empowered to make decisions and drive the platform's evolution.
- **Optimized**: The platform is continuously optimized, focusing on measuring and improving key performance indicators. The platform is deeply integrated into the organization's technology strategy and decision-making processes.

By using the CNCF's [Platform Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) as a guide, organizations can assess their current level of platform maturity, identify areas for improvement, and develop a roadmap to reach a higher level of platform success. This model has proven to be a valuable tool for many organizations, helping them to align their platform initiatives with their broader business objectives.

## Platforms as Products: Driving Success

One of the key initiatives currently underway within the Platform Working Group is the "[Platforms as Products](https://tag-app-delivery.cncf.io/blog/product-thinking-for-platforms/)" research project. This effort aims to explore the parallels between traditional product management and the management of cloud-native platforms to identify best practices and patterns that can help organizations unlock their platforms' full potential.

The core premise of the "Platforms as Products" initiative is that successful cloud-native platforms should be treated and managed like products rather than just technology projects. This means applying principles of product management, such as:

- **Defining a clear vision and roadmap**: Establishing a long-term vision for the platform and a roadmap to get there, focusing on delivering value to internal customers.
- **Measuring and optimizing for key metrics**: Identifying and tracking the right performance indicators to ensure the platform delivers the desired outcomes.
- **Fostering a thriving ecosystem**: Encouraging and enabling a community of contributors and consumers to drive the platform's evolution and adoption.
- **Continuously iterating and improving**: Embracing a continuous improvement mindset, with regular updates and enhancements to the platform based on user feedback and emerging needs.

By adopting a product management approach to their cloud native platforms, organizations can better align their platform initiatives with their broader business goals and ensure that the platform delivers tangible value to the organization.

## Conclusion

This article and Dominik Kress's talk highlighted the importance of platform engineering in cloud-native computing. Key points included defining cloud-native platforms, assessing platform maturity, and managing platforms with product management principles.

If you're interested in learning more about platform engineering and getting involved in CNCF's initiatives, there are several ways to participate:

- Register for the [Platform Engineering workshop series course](https://info.pulumi.com/platform-engineering-workshop-series).
- Join the bi-weekly [CNCF Platform Working Group meetings](https://tag-app-delivery.cncf.io/wgs/platforms/#meetings) every other Tuesday at 5 PM Berlin time (11 AM ET).
- Learn how to [build Developer Portals with Pulumi](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/). You can get off the ground faster with organization templates, a new project wizard, or leveraging the backstage plugin.

---

## Frequently Asked Questions

### What is the CNCF Platform Working Group?

Within the [CNCF](https://www.cncf.io/), the Platform Working Group is a collaborative effort focused on the critical topic of cloud native platforms. As a working group member, you can share insights and experiences from our discussions.

The Platform Working Group is part of the CNCF's App Delivery Technical Advisory Group, which includes sustainability, runtime, observability, and security initiatives. The working group is open to anyone interested in contributing to the conversation around cloud native platforms, and its members come from diverse backgrounds, including product managers, engineers, and industry experts.

### Who is Dominik Kress?

[Dominik Kress](https://www.linkedin.com/in/dominik-kress-33a540174/) is a product manager at Giant Swarm and a CNCF Platforms Working Group member.

He is on a mission to simplify developers' lives by delivering intuitive developer platforms. He has been in the IT industry for over seven years, starting his journey as a Full Stack Software Engineer, falling in love with DevOps and Product Organisations to become a Product Manager for Cloud Technology later.

Dominik is passionate about Cloud Transformation, Product Management, and helping people. He loves contributing to the community with talks, articles, or publications.

### How can I participate in the Platform As A Product research?

The "Platforms as Products" research project is currently underway, with the Platform Working Group conducting interviews and gathering insights from organizations that have successfully implemented cloud native platforms. The goal is to distill these learnings into a set of best practices and patterns that can be shared with the broader community.

To participate in this research, [sign up here](https://bit.ly/platform-research).
