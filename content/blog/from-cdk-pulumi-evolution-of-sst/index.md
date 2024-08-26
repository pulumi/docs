---
title: "From CDK to Pulumi: The Evolution of SST"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-09-25T13:32:40Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Explore how SST evolved from AWS CDK to Pulumi, overcoming limitations to offer a flexible, provider-agnostic infrastructure management solution for developers.

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
    - cloudformation
    - aws-cdk
    - aws
    - case-studies
    - developer-experience-devex
    - infrastructure-as-code

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
    twitter: Curious about SST's evolution from CDK to Pulumi? Discover how this transition is empowering developers with a more flexible, provider-agnostic approach to infrastructure management.
    linkedin: The evolution of cloud computing has reshaped how developers interact with infrastructure. For SST, a framework built to empower application developers, the journey began with AWS CDK but soon encountered limitations, and the search for a more flexible, provider-agnostic solution led them to Pulumi. Discover how Pulumi is redefining infrastructure management and what this means for the future of SST. Dive into the full story at [link].

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---
As cloud computing continues to evolve, so do the tools and frameworks that developers rely on to manage their infrastructure. For Serverless Stack (SST), a framework built to empower application developers, the journey began with AWS's CDK. While CDK offered a way to define infrastructure using familiar programming languages, it soon became clear that more was needed to meet developers' growing needs.

Explore SST's journey from its origins with CDK to its transition to Pulumi, a modern IaC platform that addresses many of the limitations faced by application developers.

<!--more-->

## On this article:

- The Beginnings of SST
- CDK and CloudFormation Limitations
- A Provider-agnostic Solution: Discovering Pulumi
- Transitioning to Pulumi
- The Benefits of Pulumi
- The Future of SST with Pulumi

## The Beginnings of SST

As application developers, we've witnessed the rapid evolution of cloud computing and the growing need for developers to have direct access to powerful cloud resources. However, the traditional tools and approaches to Infrastructure as Code (IaC) have often been geared more toward DevOps teams, leaving application developers feeling disconnected from the infrastructure side of their projects.

This was the driving force behind the creation of SST (Serverless Stack), a framework that aims to bridge the gap between application developers and infrastructure management. In the early days, SST was built on top of AWS's Cloud Development Kit (CDK), which allowed developers to define their infrastructure using TypeScript or Python. While this was a step in the right direction, they soon realized that the limitations of CDK and the underlying AWS CloudFormation were holding them back from truly empowering application developers.

## CDK and CloudFormation Limitations

{{< youtube "LXxJ9XMXC6o?rel=0" >}}

As SST's team continued to work with CDK and CloudFormation, they encountered several challenges that led them to reevaluate their approach. One key issue was the disconnect between application developers' thinking and working and traditional IaC tools' operating methods.

With CDK and CloudFormation, the infrastructure code is essentially a code generator, producing an intermediary format (such as YAML or JSON) that is then executed to deploy the resources. This means that the actual code you write as a developer is not the same as the code running during the deployment process. This can lead to a number of problems, such as difficulty debugging, lack of visibility into the deployment process, and challenges in extending or customizing the deployment workflow.

Additionally, as SST's team expanded its focus beyond the AWS ecosystem and started exploring other cloud providers and even on-premises infrastructure, it found that the AWS-centric nature of CDK and CloudFormation was becoming a limitation. It needed a more flexible and provider-agnostic solution that would allow it to deploy and manage infrastructure across a wide range of platforms.

## A Provider-agnostic Solution: Discovering Pulumi

It was during this time that the SST team discovered Pulumi, a modern IaC platform that takes a fundamentally different approach to infrastructure management. Instead of generating an intermediary format, Pulumi treats the infrastructure code as a first-class program executed directly during deployment.

This shift in paradigm had several important implications for SST and its users:

- **Visibility and Extensibility**: With Pulumi, the infrastructure code is the same code that is running during deployment, which means there is much greater visibility into the deployment process and the ability to extend or customize it as needed.
- **Multi-Cloud Capabilities**: Pulumi's provider-agnostic approach allows SST's team to easily work with a wide range of cloud and on-premises platforms, giving their users the flexibility to deploy their infrastructure wherever it makes the most sense for their application.
- **Simplified Mental Model**: For application developers, the Pulumi model of "your code is the deployment" aligns much more closely with their existing mental models and workflows, making it easier for them to adopt and work with IaC tools.

## Transitioning to Pulumi

Transitioning SST from CDK to Pulumi was not a trivial undertaking. Still, they knew it was a necessary step to truly fulfill our mission of empowering application developers with powerful infrastructure management capabilities.

One key challenge they faced was re-implementing the higher-level components and abstractions they had built on top of CDK. These components were designed to simplify the infrastructure management experience for their users, and they wanted to ensure that they could provide a similar level of abstraction and ease of use with Pulumi.

Additionally, they had to carefully consider how to handle the various edge cases and complex deployment scenarios their users encountered with the CDK-based version of SST. They wanted to ensure that the Pulumi-based version would not only match the functionality of the previous version but also improve upon it and address some of the limitations they had encountered.

## The Benefits of Pulumi

As they worked through the transition to Pulumi, they realized the significant benefits that Pulumi offered to both the SST team as the framework developers and the users.

### Improved Visibility and Debugging

One of Pulumi's most immediate and tangible benefits was the improved visibility and debugging capabilities it provided. With the infrastructure code being the same as the deployment code, they could easily trace issues back to the source and understand exactly what was happening during the deployment process.

This starkly contrasted the CDK/CloudFormation approach, where the intermediary format (CloudFormation templates) often obscured the underlying logic and made it much more difficult to diagnose and resolve problems.

### Extensibility and Customization

Pulumi's design also allowed the SST team to easily extend and customize the deployment process to meet the specific needs of their users. They could leverage Pulumi's built-in extensibility features, such as custom providers and dynamic components, to integrate with a wide range of cloud and on-premises services and implement complex deployment workflows tailored to our users' requirements.

This level of customization was much more challenging with the CDK/CloudFormation approach, where they often had to resort to hacky workarounds or custom Lambda functions to achieve the desired functionality.

### Multi-Cloud Capabilities

As mentioned earlier, one key driver for their transition to Pulumi was the need to support a wider range of cloud and on-premises platforms. With Pulumi's provider-agnostic approach, the SST team was able to easily add support for new providers, allowing their users to deploy and manage infrastructure across a diverse set of environments.

This flexibility has been particularly valuable for their users, who may have workloads or requirements that span multiple cloud providers or even on-premises infrastructure. With SST built on Pulumi, they can now manage all of their infrastructure through a single, consistent interface without having to juggle multiple tools or approaches.

### Simplified Mental Model

Perhaps one of Pulumi's most significant benefits for SST users is the simplified mental model it provides. By treating the infrastructure code as a first-class program, Pulumi aligns much more closely with how application developers think and work.

Instead of having to navigate the complexities of intermediary formats, deployment pipelines, and the separation between infrastructure code and deployment code, SST users can now focus on writing their infrastructure logic in the same programming languages they use for their application code. This makes it much easier for them to understand, maintain, and extend their infrastructure as their needs evolve.

## The Future of SST with Pulumi

With Pulumi's foundation in place, they can now focus on further enhancing the developer experience and expanding the capabilities of our framework. Some of the key areas they are exploring include:

- **Deeper Integration with Application Frameworks**: By leveraging Pulumi's flexibility, they can create even tighter integrations between SST and the application frameworks and libraries that their users rely on, making managing infrastructure seamless alongside their application code.
- **Expanded Provider Support**: the SST team will continue to add support for a wide range of cloud and on-premises providers, ensuring that their users can deploy and manage their infrastructure wherever it makes the most sense for their needs.
- **Improved Deployment Workflows**: Building on Pulumi's extensibility, they can create more advanced deployment workflows that address the specific needs of application developers, such as faster deployment times, better rollback capabilities, and more granular control over the deployment process.
- **Enhanced Observability and Monitoring**: By treating the infrastructure code as a first-class program, they can provide their users with better visibility into the deployment process and more robust monitoring and observability capabilities, helping them to identify and resolve issues quickly.

As they continue to evolve SST with Pulumi at its core, the SST team is confident that they can deliver an even more powerful and user-friendly infrastructure management experience for application developers, empowering them to focus on building great applications while seamlessly managing the underlying infrastructure.

## Conclusion

If you're interested in learning more about platform engineering and getting involved in CNCF's initiatives, there are several ways to participate:

- Learn more about Pulumi Crosswalk for AWS, which supports “day one” tasks in our [AWS guide](https://www.pulumi.com/docs/clouds/aws/guides/).
- Attend a Platform Engineering & DevOps in-person meetup, [find a location near you](https://info.pulumi.com/platform-engineering-devops-series).
- Register for one of our [Platform Engineering or DevOps workshops](https://www.pulumi.com/resources/#upcoming).
  
---

## Frequently Asked Questions

### What is SST?

SST is a framework that makes building modern full-stack applications on your infrastructure easy.

### What is SST's Ion?

Ion is the code name for a new engine for deploying SST applications. The constructs (or components) are defined using Terraform providers and deployed using Pulumi instead of CDK and CloudFormation (CFN). Once Ion is stable, it will be released as SST v3.

### Does SST use mostly Terraform or Pulumi?

SST leverages Pulumi behind the scenes as the deployment engine and for provider integrations. Terraform’s providers are bridged through Pulumi.

### How does SST make money?

Although SST is open-source and free, it also offers the Console, a SaaS service that can automatically deploy your apps and monitor for issues. The Console is optional and includes a free tier.
