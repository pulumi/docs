---
title: Shifting Infrastructure Left at WhyLabs
description: |
    At WhyLabs, Pulumi has made a significant impact in how they build, deploy and manage their infrastructure.
meta_desc: |
    At WhyLabs, Pulumi has made a significant impact in how they build, deploy and manage their infrastructure.

customer_name: WhyLabs
customer_logo: /logos/customers/whylabs-wordmark.svg
customer_url: https://whylabs.ai/

exec_summary: |
    WhyLabs helps organizations run their AI applications with certainty by monitoring them for problems such as data drift and model degradation. Founded by alumni of AWS, the company began building their platform on AWS and used AWS-provided tools to manage their infrastructure. However, the WhyLabs team needed a platform that could handle the complexity of their modern cloud architectures and would set them up for success when they’re ready to adopt multi-cloud deployments. The team also wanted a platform that integrated with the modern development workflows used by WhyLabs’ developers, who have a software engineering-driven culture of tight collaboration and shared responsibility for infrastructure. By migrating to the Pulumi Cloud Engineering Platform, WhyLabs engineers can continuously and reliably ship new features faster than before for improved time-to-market. Pulumi enabled WhyLabs to adopt cloud engineering best practices out-of-the-box, including building infrastructure as code with general-purpose languages like TypeScript, versioning and reviewing infrastructure code through a code review process, and delivering infrastructure through its existing GitLab CI/CD pipeline using Pulumi’s integrations.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: WhyLabs
      anchor: whylabs
    - label: The WhyLabs Environment
      anchor: the-whylabs-environment
    - label: Bringing Pulumi Onboard
      anchor: bringing-pulumi-onboard
    - label: Adopting Cloud Engineering Best Practices with Pulumi
      anchor: adopting-cloud-engineering-best-practices-with-pulumi
    - label: Shifting Infrastructure Development to the Left
      anchor: shifting-infrastructure-development-to-the-left
    - label: Infrastructure CI/CD Improves Time to Market
      anchor: infrastructure-cicd-improves-time-to-market
    - label: Summary
      anchor: summary
---

## WhyLabs

WhyLabs is focused on helping companies adopt AI. The WhyLabs observability platform monitors data pipelines and machine learning applications for data-quality regressions, data drift and model performance degradation. This provides transparency for teams building and operating data and AI-enabled applications and reduces manual troubleshooting when a model no longer fits the underlying data used by an application. The platform is built on top of whylogs, an open-source, lightweight statistical logging library. WhyLabs was founded in December 2019 and is based in Seattle. It had an initial incubation period at the Allen Institute of Artificial Intelligence (AI2) and emerged from stealth in 2020, after raising a $4 million seed round.

## The WhyLabs Environment

WhyLabs is a small company and its developers are nimble and accustomed to wearing many hats. Its founding members came in with extensive experience at Amazon Machine Learning, so it’s no surprise they brought their Amazon experience with them. They follow the “two-pizza team” model made famous at Amazon, which means teams are small, collaborative and responsible for both the development and operations of the services they build.

WhyLabs uses modern cloud architectures for its AI applications running on AWS. They run containers with Amazon ECS, serverless with AWS Lambda, and Amazon EMR for large-scale data processing. They also use Amazon CloudFront as their content delivery platform.

Initially, WhyLabs tried out AWS CloudFormation and the AWS Cloud Development Kit (CDK) to manage their infrastructure. However, these tools frequently made infrastructure management more complex and inefficient for developers, which stifled WhyLabs’ ability to innovate quickly as a young startup. For example, developers had trouble using CloudFormation’s DSL, which made it difficult and time-consuming to model infrastructure. Developers found the DSL limiting since it didn’t support standard language features like conditions, loops, and constants. It also didn’t enable standard software principles such as creating modular and reusable infrastructure. Although CDK improved upon CloudFormation by adding general-purpose languages, it didn’t provide the full benefits of those languages since it didn’t support common software practices and tools such as unit testing with standard frameworks. Furthermore, it suffered many of the same limitations as CloudFormation because it was an abstraction built on CloudFormation. Last but not least, these tools only supported AWS when WhyLabs needed the flexibility to go multi-cloud.

As more developers joined WhyLabs and the company began to think about multi-cloud environments, they needed a modernized approach that would enable the company to scale its cloud infrastructure with the speed and agility required of an innovative startup. WhyLabs and its “two-pizza teams” needed a platform that would enable them to apply existing software engineering best practices to their infrastructure, and the platform needed to support any cloud.

## Bringing Pulumi Onboard

Andy Dang is a Lead Engineer and a co-founder of WhyLabs. He first heard about Pulumi from a colleague at AI2. He says, “I was blown away by the multi-language experience as well as the various innovations, such as its best-in-class support for Kubernetes. Those qualities, as well as support for multiple cloud providers made me decide to go with Pulumi.”

## Adopting Cloud Engineering Best Practices with Pulumi

Moving to Pulumi allowed WhyLabs to adopt cloud engineering best practices out-of-the-box. [Cloud engineering]({{< relref "/cloud-engineering" >}}) teams apply standard software engineering practices and tools uniformly across infrastructure management, application development, and security to tame the complexity of delivering and managing modern cloud applications. Key advantages for WhyLabs were that they could:

- Use a general-purpose, strongly-typed language to define and configure infrastructure as code while using standard software development tools.
- Shift infrastructure development left by incorporating more frequent testing during the authoring stage and before production.
- Deploy infrastructure code through their CI/CD toolchain on GitLab.

### Adopting a Standard Language for Apps and Infrastructure

With Pulumi, WhyLabs was able to build infrastructure as code in standard programming languages like TypeScript, JavaScript, Python, Go, and C#. They decided on TypeScript based on the preferences and existing expertise of their developers.

Using a general-purpose, strongly-typed language simplified how to author and configure infrastructure code.  Andy says, “With a strongly-typed language, it’s much easier to reason about the parameters of the cloud. Each component can have hundreds of configuration parameters. Types allow you to better understand whether your configuration is correct. That makes it much easier for our devs to be confident when they work on infrastructure.”

Andy also found that using a standard programming language meant developers could start being productive much faster than if they had to learn a more limited, specialized DSL such as CloudFormation, which he believes has a high barrier to entry. With TypeScript, people could begin writing infrastructure code and contributing soon after joining the team. He says, “I wanted a lot of the ownership of the infrastructure to be shared. As you work on a service, you learn how to manage that service’s infrastructure. Each person can own some piece of it. Even if you’re not an expert, you can at least add or modify resources. For that kind of distributed responsibility, you need a general-purpose language.”

## Shifting Infrastructure Development to the Left

To cloud engineering teams, infrastructure is software meaning it is developed, deployed and managed like any other software asset. It’s frequently tested during the authoring stage and vetted through code reviews and deployed via an automated CI/CD pipeline. This enables teams to make infrastructure updates with more confidence and reliability since everything is versioned, reviewed, and tested before deployment. By doing so, teams can “shift left” - moving quality and security-focused efforts from a reactive activity to a proactive effort before bits reach production.

Pulumi made it easy for WhyLabs to adopt these practices. Pulumi’s integration with GitLab CI/CD means that WhyLabs can have a fully automated, continuous deployment pipeline for cloud infrastructure. For example, infrastructure changes are now made collaboratively through a peer review process. Rather than manually applying changes to infrastructure, all proposed changes are gated through merge requests before being deployed through the pipeline. By using merge requests, WhyLabs also has a log of all the changes and who made the changes. WhyLabs can also set access controls for the pipeline to secure who can make and approve changes.

### Review

Pulumi allows the infrastructure code review process to fit naturally within the GitLab code review process. This is particularly helpful when sensitive changes, such as those that are security related, need approval. Because infrastructure is treated like any other piece of code, Pulumi and GitLab make it easy to route proposed changes to the correct people for review. Not only does this make the review process itself easier, but it means that changes are well documented and easily audited.

### Test and Deploy

Since infrastructure is software with Pulumi, it can be tested like software through a CI/CD pipeline. WhyLabs uses Pulumi and GitLab to run automated [unit tests]({{< relref "/docs/guides/testing/unit" >}}) on infrastructure and [Policy as Code]({{< relref "/crossguard" >}}) tests that check for common human errors such as leaving an S3 bucket open to the public. The pipeline also runs [integration tests]({{< relref "/docs/guides/testing/integration" >}}) that can detect issues with the stack early in the development process by provisioning ephemeral environments. Furthermore, WhyLabs developers can use Pulumi to deploy private environments to test their logic, enabling them to iterate on complex cloud environments without causing issues to the production environment.

### Security

At WhyLabs, developers have their own stacks where they can test out deployments before they’re merged with a production stack. WhyLabs uses Pulumi to embed security controls in the pipeline to keep track of events. For example, they can track all deployments and see who triggered each deployment. Stacks are secured automatically rather than relying on manual, after-the-fact fixes. In addition, WhyLabs uses Pulumi to manage secrets with AWS Secrets Manager and to manage VPC security and network control.

## Infrastructure CI/CD Improves Time to Market

Cloud engineering is about leveraging existing software engineering best practices to increase velocity. Integrating Pulumi with GitLab’s CI/CD pipeline created an efficient, fast delivery workflow for cloud infrastructure and applications. Andy says, “Every time that we make a code change, we make a deployment. It flows through our pipeline very quickly. It allows us to demo features to our customers very effectively. We’ve had cases where features were developed in a week and we were showing them to customers on the following Monday. Pulumi definitely makes our iteration times much faster. Also, being able to replicate deployments to a separate independent environment allows us to find bugs and detect deployment issues much earlier.”

## Summary

At WhyLabs, Pulumi has made a significant impact in how they build, deploy and manage their infrastructure. Here are some of the highlights.

- Pulumi enabled WhyLabs engineers to continuously and reliably ship new features faster than before for improved time-to-market.
- Pulumi enabled WhyLabs to adopt standard programming languages (like TypeScript) to build infrastructure as code. It also allows them to use software engineering best practices like reusability and unit testing.
- Pulumi lowered the barrier to entry for developers to start working with infrastructure. A standard programming language means that every developer can quickly become involved in creating and maintaining the WhyLabs infrastructure.
- Pulumi enables WhyLabs to shift infrastructure left because testing and security controls are automated with Pulumi and GitLab integration. Peer reviews and accountability are built into the GitLab CI/CD pipeline.
- Pulumi’s integration with GitLab enables WhyLabs to deliver infrastructure through CI/CD pipelines just like with application code, which increases iteration frequency and accelerates time to market.
- Pulumi’s support for multiple cloud providers will help WhyLabs expand their platform in the future to meet customers’ needs.
