---
title: Fenergo

description: |
    Fenergo chose Pulumi so that it could more easily adopt modern cloud architectures
    on AWS, deliver a new SaaS platform, and improve time-to-market.
meta_desc: |
    Fenergo chose Pulumi so that it could more easily adopt modern cloud architectures
    on AWS, deliver a new SaaS platform, and improve time-to-market.

customer_name: Fenergo
customer_logo: /logos/customers/fenergo-wordmark.svg
customer_url: https://www.fenergo.com/

exec_summary: |
    Fenergo delivers cutting edge client lifecycle management technology for financial institutions. The advent of COVID meant that Fenergo had to dramatically change the services they delivered, so Fenergo shifted its focus to creating SaaS applications built on modern cloud architectures. Fenergo’s lean, full-stack engineering teams sought an agile culture and cloud engineering best practices in order to deliver cloud applications rapidly and safely, but they needed a platform that would enable them to adopt cloud engineering best practices out-of-the-box. By selecting the Pulumi Cloud Engineering Platform, Fenergo improved its time-to-market by removing cloud infrastructure as a road back to business innovation. Its engineers can now build, deploy, and manage both cloud infrastructure and applications faster and with more confidence, using programming languages and software tools they already know. This has resulted in faster software delivery, closer collaboration and higher-quality deployments. Every developer is now empowered to move faster and spend more time on developing things that matter to customers, which drives a competitive advantage for Fenergo.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About Fenergo
      anchor: about-fenergo
    - label: The Move to Modern Cloud Architectures
      anchor: the-move-to-modern-cloud-architectures
    - label: Why Pulumi
      anchor: why-pulumi
    - label: How Pulumi Benefits Fenergo
      anchor: how-pulumi-benefits-fenergo
    - label: The Future
      anchor: the-future
---

## About Fenergo

Fenergo is the leading provider of client lifecycle management, anti-money laundering and Know Your Customer (KYC) compliance solutions for the financial services industry. Founded in 2008, Fenergo serves more than 80 of the world’s top financial institutions and 32 of the top 50 banks in the world use the Fenergo platform. Fenergo’s goal is to digitize the fight against financial crime. Fenergo creates frictionless onboarding and compliance journeys for its customers and for their customers.

## The Move to Modern Cloud Architectures

Keith Redmond is the VP of SaaS Engineering at Fenergo. With the advent of COVID, he realized that Ferengo needed to move away from its focus on on-premise software to modern cloud architectures and software-as-a-service products. He says, “We’ve all been forced into working remotely and that change has dramatically affected the financial services industry. Traditionally it’s an industry based on face-to-face communications. With COVID, physical bank branches and financial offices became inaccessible. That meant we had to become much more focused on cloud-based products.” So, in early 2020, Fenergo decided to build out its modern cloud architecture product stack.

To support its move to the modern cloud, Fenergo would have to build out its engineering teams and use a new approach to developing software. Keith’s goal was to create a culture that emphasized ownership, agility and frequent deployments. In strategy sessions, his teams would often use the phrase ‘You build it, you run it.’ He wanted to avoid creating teams where responsibilities were handed off to groups that were dedicated to specific functions, such as dedicated DevOps teams.

With a limited budget for building a team, Keith wanted to invest in full-stack engineering teams rather than specialists to achieve his goals. These teams would use a software engineering approach to tackle both the cloud infrastructure and application development. But they needed a platform that would enable them to use software engineering best practices with both cloud infrastructure and applications—otherwise known as [cloud engineering]({{< relref "/cloud-engineering" >}}).

“I was determined to find a cloud engineering platform that would both support our continuous deployment goals while also making it easy for our development teams to ramp up and become true cloud engineers,” says Keith.

### Finding the Right Framework

Keith and his group began their journey to a modern cloud architecture in early 2020 and evaluated a number of tools, including the Pulumi Cloud Engineering Platform. Pulumi would support their goals by enabling them to adopt cloud engineering practices out-of-the-box. Cloud engineering applies standard software engineering practices and tools uniformly across infrastructure, developer, and security teams to tame the complexity of delivering and managing modern cloud applications.

Each tool would be evaluated through a proof of concept to see if it would enable the engineers to apply cloud engineering principles to their projects and build the cross-cutting culture Keith wanted.

Their first project, running on AWS, used some simple AWS Lambda functions behind an API Gateway that connected to a document database. The project itself wasn’t complicated but it allowed the engineers to focus on what the tools could do.

## Why Pulumi

When evaluating Pulumi, the teams were impressed that they could now build infrastructure as code using general-purpose languages such as TypeScript, Python, Go and .NET. These languages have quite a few advantages over special-purpose domain-specific languages (DSLs) used by legacy infrastructure tools. For instance, they allow developers to easily create strongly-typed, structured configurations. In addition, DSLs lack many basic programming constructs. With Pulumi, the developers could use features they’d always relied on such as loops, constants and helper functions. Using programming languages meant that they could also use IDEs they already knew as well as familiar testing frameworks so they could easily test the infrastructure.

Pulumi made it easier for Fenergo’s full-stack engineers to learn how to develop for the cloud because it tames the cloud’s complexities. Keith says, “Because Pulumi  provided a familiar development experience for cloud infrastructure through support for common programming languages and developer tools, our teams were able to see results quickly. But one of the things that made Pulumi really stand out for us was its ability to help our people learn the cloud.

“At the time, we had limited knowledge of some of the AWS stack. Even something as simple as Pulumi’s built-in Intellisense, which works with any IDE, helped us drive quality and make sure our infrastructure as code was complete.”

Another way that Pulumi helps developers become proficient at building for the cloud is by providing best practices out-of-the-box. Pulumi provides a [collection of libraries]({{< relref "/docs/guides/crosswalk/aws" >}}) that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure. Using these best practices, Fenergo developers could rapidly build and deploy cloud infrastructure without needing expertise in cloud architecture.

The Fenergo teams also found that Pulumi enabled them to easily create and share reusable infrastructure components that had custom best practices baked in. This cloud engineering practice, called reusability, meant that Fenergo engineers could easily share a set of common best practices across teams so that everyone could build and deploy uniform, predictable cloud architectures.

Summing up his experiences with Pulumi, Keith says, "I've had 50 cloud developers
working with Pulumi in the last year and maybe two or three of them had cloud experience. But I can count the number of misconfigurations in production on one hand because Pulumi breaks the build when they occur. It's not letting us make those mistakes."

### Success at Fenergo

Keith and his teams never looked back after their initial success with Pulumi. One year after that first simple project, Fenergo now has 12 teams actively building the production cloud infrastructure with TypeScript. They are all using Pulumi to build, deploy, and manage everything from Lambda functions to configurations of EC2 instances that are deeply integrated into the company’s SIEM (Security information and event management) tools and Infosec layer. They now make changes to infrastructure safely and confidently by using cloud engineering deployment practices. For example, they commit infrastructure changes to Git through pull requests, which trigger automated pipelines that test and deploy updates.

Keith says, “We’re doing everything from automated build and release pipelines where Pulumi is a gated step that ensures we’re maintaining the integrity and the quality of all of our cloud resources. That’s vital to us as a company that’s in such a highly regulated industry.”

## How Pulumi Benefits Fenergo

Pulumi enabled Fenergo to adopt cloud engineering best practices across every team, which increased their agility and innovation velocity. Here’s a summary of how Pulumi benefits Fenergo.

- With Pulumi, Fenergo was able to invest its entire headcount in teams of full-stack engineers who own both the infrastructure and applications instead of needing to hire DevOps engineers.
- Improved time-to-market because,  now that the cloud infrastructure is easy to manage, engineers can spend more time building new features.
- With Pulumi, Fenergo can set cloud infrastructure best practices that the teams implement consistently.
- The quality and integrity of the Fenergo infrastructure is always improving because Pulumi helps the engineers use cloud engineering best practices that reduce errors.

"Pulumi improved our time-to-market by removing cloud infrastructure as a roadblock to business innovation," said Keith. "Our developers rely on Pulumi’s Modern Infrastructure as Code and software engineering approach to build modern cloud applications, including the underlying infrastructure, using programming languages they understand. This has resulted in faster software delivery, closer collaboration and higher-quality deployments. Every developer is now empowered to move faster and spend more time on developing things that matter to our customers, which drives a competitive advantage for Fenergo."

## The Future

Keith has a number of plans for using Pulumi in the future. His company is starting to evaluate using multiple cloud providers and he thinks that Pulumi will help them take advantage of what each provider has to offer.

He also wants to use [Pulumi’s “policy as code”]({{< relref "/docs/guides/crossguard" >}}) features to help Fenergo implement stronger governance and oversight for their engineering projects. Automating compliance will be very important as Fenergo scales out its footprint.

Finally, Keith is particularly excited by the [Pulumi Automation API]({{< relref "/docs/guides/automation-api" >}}), which exposes the full power of infrastructure as code through a programmatic interface, instead of through CLI commands.

Keith says, “Using the Automation API, I think we can move away from configuration-based build pipelines and the challenges they bring and instead move toward full end-to-end solutions where build, test, run and deploy are all written in first-class languages using tooling we’re all familiar with.”
