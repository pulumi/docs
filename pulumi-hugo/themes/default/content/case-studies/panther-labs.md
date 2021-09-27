---
title: Increasing Velocity and Innovation at Panther Labs
description: |
    With Pulumi, Panther Labs was able to provide innovative solutions to their customers quickly, which is a clear advantage for a startup.
meta_desc: |
    With Pulumi, Panther Labs was able to provide innovative solutions to their customers quickly, which is a clear advantage for a startup.

customer_name: Panther Labs
customer_logo: /logos/customers/panther-labs-wordmark.svg
customer_url: https://runpanther.io/

exec_summary: |
    Panther Labs helps modern security teams build world-class detection and response pipelines using code and automation, developer-friendly workflows, and big data primitives. Its Platform Team is responsible for a large, complex serverless architecture on AWS. Because of the limitations of its legacy Infrastructure-as-Code (IaC) tool, the team was unable to manage and scale its cloud infrastructure with the speed and automation that the company needed to support its fast-growing business. After comparing different alternatives, Panther Labs decided to migrate to the Pulumi Cloud Engineering Platform. Pulumi increased the company’s deployment speeds by up to 10X, reduced the size of its infrastructure codebase by >50%, and enabled its developers to adopt cloud engineering best practices to deliver its cloud applications faster and more reliably.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About Panther Labs
      anchor: about-panther-labs
    - label: The Problem
      anchor: the-problem
    - label: Why Pulumi
      anchor: why-pulumi
    - label: Proving Pulumi’s Advantages
      anchor: proving-pulumis-advantages
    - label: Adopting Modern Cloud Engineering Practices
      anchor: adopting-modern-cloud-engineering-practices
    - label: The Conclusion
      anchor: the-conclusion
---

## About Panther Labs

Panther Labs is a security data firm based in San Francisco. It was founded in 2018 by a team of seasoned security practitioners whose goal was to build a single, modern platform that would enable small security teams to operate at a high scale. The result, called Panther, is a security analytics platform that helps teams detect and respond to breaches at cloud scale.

## The Problem

Austin Byers is a Principal Platform Engineer at Panther Labs. His team builds, deploys and manages a complex infrastructure that is on AWS and completely serverless. The developers on his team were using AWS CloudFormation and its YAML-based domain-specific language (DSL) to deploy and manage cloud infrastructure. However, the team found that CloudFormation was hitting a wall as they tried to scale their infrastructure, ultimately slowing down their velocity and ability to innovate when they needed to move faster.

CloudFormation had a number of drawbacks that impeded speed and developer productivity. Its non-standard DSL made it difficult to model infrastructure and write custom logic, which would be easy with a standard programming language. For example, programming primitives like conditions, loops, booleans, local variables, constants, and modules either weren’t possible in CloudFormation or required awkward, fragile workarounds. In addition, developers had to break the infrastructure into arbitrary chunks to avoid CloudFormation stack limits, which slowed down both the development and the deployment process. Its verbosity and inexpressiveness resulted in a bloated and unwieldy codebase, with more than 13,000 lines of templates.

It was also difficult to organize and manage the Panther Labs infrastructure into logical components with CloudFormation. The team wanted to manage different components of its infrastructure with higher-level abstractions that could be easily shared and reused consistently across teams. However, CloudFormation did not support this natively, so the team had to build a complex “hack” that accomplished the same thing. Not only did this make creating reusable infrastructure components difficult, but it also made an already unwieldy codebase even larger. Re-using the infrastructure meant auto-generating thousands of lines of new templates and injecting application code into the deploy process.

Last but not least, CloudFormation had slow deployments and teardown times, which impacted the company’s velocity. That velocity was also hampered by the lack of native support for unit and integration testing, making it difficult to test infrastructure frequently before it was deployed.

In summary, the limitations of CloudFormation actually increased the complexity of describing their infrastructure and made their jobs harder. The team needed a better solution that would enable it to increase innovation and move faster.

## Why Pulumi

Austin examined the Pulumi Cloud Engineering Platform and the AWS Cloud Development Kit (CDK), which is based on CloudFormation. After investigating the CDK, Austin rejected it because it had many of the same drawbacks as CloudFormation. For example, although CDK supported programming languages, it didn’t provide a strongly typed and structured programming environment. Developers wouldn’t be able to run standard unit and integration tests with it. It only supported AWS resources, which locked them into a single cloud vendor. Most importantly, the CDK was simply an abstraction built on CloudFormation, which meant it had many of the same limitations as CloudFormation but with slower deployment times.

Austin learned about Pulumi from a Panther customer. By using Pulumi, his team would be able to apply software engineering best practices to infrastructure with cloud engineering. A cloud engineering approach applies standard software engineering practices and tools uniformly across infrastructure, development, and security teams and tames the complexity of delivering and managing modern cloud applications. In addition, Pulumi’s fully managed service would provide his team with a centralized view of their hundreds of single-tenant deployments, allowing them to see which Panther version is running for each customer account, when versions were upgraded, and what changed after each deployment.

As part of his evaluation, Austin performed benchmarking tests on Pulumi which would help build his case for adopting it with the company.

## Proving Pulumi’s Advantages

To evaluate Pulumi’s performance, Austin ported more than 500 AWS resources to Pulumi. The results proved that Pulumi could do everything he’d hoped. His tests showed that:

- **Pulumi is fast.** Compared to CloudFormation, teardowns were twice as fast, fresh deployments were four times as fast, and simple changes were more than ten times as fast.
- **Pulumi code is compact and efficient.** Austin found that he could cut the infrastructure codebase down by more than 50%.
- **Pulumi is easy to learn.** The developers could use a programming language and existing software development practices that they already knew.

Here is the graph that contrasts deployment rates with Pulumi and CloudFormation. In all cases, Pulumi performed significantly better.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/panther-labs-deployment-rates.png" alt="Panther Labs Deployment Rates" />

This graph contrasts lines of code when using Pulumi and when using the CloudFormation DSL, which is YAML-based.

 <img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/panther-labs-lines-of-code.png" alt="Panther Labs Lines of Code" />

With Pulumi, the codebase shrank by more than 50%.

## Adopting Modern Cloud Engineering Practices

After adopting the Pulumi platform, Panther Labs can now build, deploy, and manage its cloud infrastructure and applications faster and with more confidence, using any language and any cloud. The result was faster innovation and improved time to market. This was possible because Pulumi enabled the Panther Labs team to adopt cloud engineering practices out-of-the-box.

With Pulumi, the team could build modern infrastructure as code using standard, general-purpose languages such as TypeScript, Python, .NET and Go. Developers could easily create strongly-typed, structured configurations and use standard programming constructs they’d always relied on such as loops, constants and helper functions.

Because Pulumi supports general purpose programming languages, Panther’s developers could also use standard unit testing frameworks that enable them to frequently test their infrastructure and “shift risk left.” The team could also version infrastructure code with Git and deliver their infrastructure code through the same CI/CD pipelines used for application code. Frequently testing infrastructure code and delivering it through automated pipelines increased both delivery speed and quality.

Pulumi also enabled the team to apply software reusability principles to its infrastructure. It could now create reusable infrastructure components that follow a set of common best practices, which in turn, creates predictable, reliable cloud architectures. This allowed the team to manage its complex, serverless architecture with higher-level components that can easily be shared with other developers. As an example, one type of reusable component was composed of a Lambda function along with more than a dozen other resources such as IAM roles, CloudWatch Logs, CloudWatch metrics and alarms.

Austin summed it up by saying, “Our developers needed a robust platform for managing our complex infrastructure, and it needed to be fast, modular, and testable. CloudFormation was none of these things. Although migrating from CloudFormation felt like a radical proposal, we now have more reliable releases and a significantly better developer experience as a result of adopting Pulumi. Nothing is better than having standard programming languages for building and managing infrastructure.”

## The Conclusion

Austin found that Pulumi was the way for Panther Labs to truly become a company driven by the principles of cloud engineering. With Pulumi, Panther Labs was able to provide innovative solutions to their customers quickly, which is a clear advantage for a startup. Panther Labs saw:

- Teardowns were twice as fast, fresh deployments were four times as fast, and simple changes were more than ten times as fast.
- The deployment codebase was reduced by more than 50%.
- Developers could use a programming language and existing software development practices that they already knew.
- The ability to create reusable components made it easy to replicate and share components that always followed cloud engineering best practices.
- Central visibility across hundreds of single-tenant customer deployments, including a history of when changes were made and what changed for each account.
