---
title: "Infrastructure Testing Best Practices of Sam Cogan, Puluminary & Azure MVP"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-09-06

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: true

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc:

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - george-huang

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - case-studies
    - kubernetes
    - cloud-native
    - azure
    - testing

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

[Sam Cogan](https://github.com/sam-cogan) is Solutions Architect at [WTW](https://www.wtwco.com/en-us), with a background in IT and experience in software development. A highly visible member of the community, he is both a Microsoft Azure MVP and Puluminary. Sam’s core duties include the development of a resilient platform that supports customer-facing applications and working with DevOps teams on standardizing deployments and using infrastructure as code. Sam's team prioritizes crafting reusable components that adhere to security and compliance standards.

<img src="sam-cogan.jpg" alt="Sam Cogan" width="250">

<!--more-->

## Challenge

Sam’s work deals with deploying and managing the infrastructure that runs sophisticated applications for risk modeling. These applications are not only computation-intensive, handling predictive modeling and random number generation, but they also require high-scale, reliable infrastructure due to their resource demands. They run on Azure, employing resources like container-based Kubernetes, Azure container apps, VMs, scale sets, and Azure Batch for grid compute. Dynamic scaling remains a core challenge; they need to efficiently scale resources according to computational demands. However, the tools they historically relied on, including ARM templates, Terraform, PowerShell, and Azure CLI, led to disjointed infrastructure management. Furthermore these tools don't natively support infrastructure testing, meaning they needed to write additional scripts or code.

## Why Pulumi

Sam likes Pulumi’s support for familiar programming languages, in particular C# which is used at WTW. This offered a simpler and more powerful way to build infrastructure. Another compelling benefit of Pulumi was that it greatly expanded developers’ ability to test and validate infrastructure code using existing test frameworks and Pulumi test frameworks, which facilitated the shift-left methodology they were adopting. Another advantage was Pulumi’s default encryption of state files, which enhances security compared to other tools.

## “Shifting left” for infrastructure

"Shift Left" isn't just a strategy for Sam, it's a philosophy. Historically, developers would handle application development, provide specifications, and hand off to operations for infrastructure deployment – a process that could introduce delays and knowledge gaps. Sam states that shifting left encourages developers to be involved in the infrastructure development process from the start, ensuring they have a comprehensive understanding of both the application and its required environment. This early involvement can preempt potential issues, resulting in more streamlined and efficient development and deployment processes.

## How Sam uses Pulumi to test infrastructure code

### Unit Testing

Unit testing validates individual software components, ensuring they function correctly. When applied to infrastructure-as-code, this testing ensures that the deployed infrastructure corresponds with the code’s design and intention. Pulumi allows developers to test infrastructure code without actual deployment through a mechanism known as 'mocking'. By creating mock outputs for deployments, Pulumi unit tests focus on validating the developer's intentions rather than the actual execution by the cloud platform. This ensures the infrastructure code will produce the expected outputs if deployed.

#### Sam’s Approach to Unit Testing with Pulumi

Pulumi's ability to enable rigorous unit testing of infrastructure has proved invaluable. By using familiar tools like XUnit, NUnit, and Visual Studio IDE, developers can seamlessly test and validate their infrastructure code, including component resources. This ensures that the real-world deployment of these components works. One example includes validating specific parameters like the number of rules in an IP allow list or checking Azure Network Security Group rules. This testing increases the integrity and compliance of their infrastructure.

### Policy Testing

Policy testing validates that infrastructure-as-code (IaC) deployments follow set standards and best practices. Pulumi's open source Crossguard framework allows developers to define, enforce, and test infrastructure policies using programming languages. This proactive approach catches policy breaches early, reducing remediation efforts and ensuring deployments adhere strictly to organizational objectives.

#### Sam’s Approach to Policy Testing with Pulumi

Sam uses Pulumi's Crossguard for policy testing. This process involves writing policies in Python that match corporate standards. Some of these policies verify configurations like enabling HTTPS encryption across all app services or ensuring VMs with public IPs aren't left exposed to the internet. Policy tests are run automatically by orchestrating Pulumi CLI commands with Azure DevOps pipelines. This integrated approach not only enhances security and compliance posture but also streamlines deployment cycles.

### Integration Testing

Integration testing evaluates individual software modules as a group, validating their interactions. For Infrastructure-as-Code, this involves verifying that deployed infrastructure runs as expected. Pulumi makes this process easy, not just for its ability to seamlessly create and teardown ephemeral infrastructure for testing, but also because it enables automation of the entire integration testing process.

#### Sam’s Approach to Integration Testing with Pulumi

Sam and his team orchestrates integration tests through an Azure DevOps Pipeline with Pulumi. When deploying component resources, such as a Kubernetes cluster which encompasses a virtual network, storage, cluster, and applications like nginx or cert manager, Pulumi is used to validate every deployment stage. The checks include confirming the Kubernetes cluster's operational status, verifying the running state of deployed pods, the ability to generate certificates, among others. After these infrastructure checks, the tests transition to the application layer. Here, they deploy the application onto the infrastructure, testing key functionalities. These tests range from ensuring the correct configuration of a storage account to complex validations, like sending an HTTP request to the app and expecting a valid 200 response. The entire procedure, streamlined by Azure DevOps and Pulumi, ensures robust infrastructure and application deployment.

## Benefits of infrastructure testing

**Faster Time-to-Market:** The integration of Pulumi and Azure DevOps pipelines speeds up the deployment lifecycle. This results in more frequent releases while increasing quality and reliability via automated integration tests.

**Shift Left:** The capacity to use familiar programming languages with Pulumi has fostered a "shift left" approach. Developers can be engaged earlier in the infrastructure development process, shortening the time from development to deployment and identifying and fixing errors much earlier on through unit testing.

**Compliance & Security:** Pulumi promotes robust security and strict compliance. Pulumi addresses this through encrypted state management and the Crossguard policy-as-code framework for policy testing.

## Try Pulumi for Infrastructure as Code

[Sign up for a free account](https://app.pulumi.com/signup) to try deploying infrastructure on any cloud, or [register for an upcoming workshop](https://www.pulumi.com/resources/#upcoming) to learn more about how Pulumi can help you ship cloud infrastructure faster and more safely.

Learn more about testing infrastructure code in the [documentation](/docs/using-pulumi/testing/).
