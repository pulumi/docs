---
title: What is Platform Engineering?
allow_long_title: true
meta_desc: |
    Understand what platform engineering is, along with the main benefits and importance for modern application development.
type: what-is
page_title: What is Platform Engineering?
---

Platform engineering is a set of modern engineering practices that take a holistic approach to managing the entire software development lifecycle, encompassing infrastructure, tools, and processes. The aim of platform engineering is to provide a scalable and secure platform that supports the development, deployment, and operation of software applications in a standardized and efficient way.

## What is platform engineering?

In a platform engineering approach, one or more teams---often referred to as the platform engineering team or the platform team---build a comprehensive set of shared tools and services (aka "the platform") to help development teams develop, deploy, and operate cloud infrastructure on a self-service basis. This includes cloud infrastructure, container orchestration platforms, databases, networking, monitoring, code repositories, and deployment pipelines.

Platform teams use a customer-driven mindset where they treat the application developers that they serve as customers that must be understood and won over through products that solve their problems. The products these teams offer are infrastructure tools and building blocks that development teams use to provision and manage standardized infrastructure for their applications and services. Typically, these tools have built-in guardrails that enforce best practices and security standards without impeding developers' agility and workflow. This is all done in service of increasing the speed of delivery for the company's products.

## What are some of the requirements for platform engineering?

Regardless of implementation details or specific methods, there are some simple requirements that many platform engineering teams follow. All of these requirements are driving toward maximizing the use of the cloud at scale across an organization while being secure and compliant and enabling developers and develpoment teams to ship faster.

* **Simple and powerful user experience**: Build curated experiences that empower developers by meeting them at their level of expertise. Use a variety of approaches to provide an ideal user/developer experience, including infrastructure code libraries (reusable pieces of code), infrastructure CLIs, internal developer portals (IDPs), or shared IaC templates.
* **Automation as default**: Automation reduces devastating errors. Don't leave anything to ClickOps. Every change to infrastructure must be run through tests before rolling into production. No change should be untraceable. All infrastructure from resources, configurations, environments, and secrets are tracked in version control. Everything from infrastructure provisioning to control plane orchestrations needs to be programmable.
* **Full visibility on everything**: Log, monitor, and observe all infrastructure for greater operational control. Optimize against unnecessary costs.
* **Security as a foundation**: Security and compliance guardrails need to exist for everything. Fine-grained access controls should exist for every piece of infrastructure. Prefer dynamic, short-lived credentials over long-lived, static credentials with seamless integration into development workflows.
* **Well architected by design**: Decouple the application complexity from the infrastructure complexity, reducing the blast radius of incidents while increasing resiliency. Construct shareable infrastructure components that are built for high availability and low operational maintenance. Operate seamlessly across heterogeneous environments while implementing best-in-class infrastructure.

## What is a platform engineer?

_Platform engineer_ is a term used to describe the engineers that make up a platform team or a platform engineering team. Typically, these engineers have the multi-disciplinary skills, experience, and empathy needed to build a great product, serve developers' needs, and "go to market" within their company. Often, they have experience with multiple engineering disciplines like infrastructure or DevOps and software engineering. The reality is that many engineers who perform platform engineering responsibilities do not have the title "platform engineer." In practice they have varying job titles like software engineer, DevOps engineer, SRE, cloud architect, cloud engineer, and more. By providing developers with infrastructure and tooling to deploy and operate their applications efficiently, platform engineers enable developers to focus on building great software.

Practitioners working in platform engineering roles usually have a software engineering mindset, as opposed to a DevOps/sysadmin/scripting mindset.

## Why is platform engineering important?

Developers need infrastructure to run their applications and services. Traditionally, companies have used central infrastructure teams that provision and manage infrastructure on behalf of developers, but this model is prone to bottlenecks as developer requests for infrastructure overwhelm central teams. As modern development teams have taken responsibility over owning and operating their own infrastructure, they also need simple and fast ways of provisioning it while adhering to best practices.

Platform teams solve these challenges:

* The cloud is too complex and unwieldy for most developers to use without abstractions and tooling
* Developers need to know which infrastructure resources to provision
* Developers need an easy way to provision, configure, and manage infrastructure
* Infrastructure provisioned by developers needs to adhere to company best practices

Platform engineering can increase development velocity, improve security, increase infrastructure's adherence to best practices, and reduce operational costs through automation. It helps organizations increase the ROI on cloud investments and improves the software delivery lifecycle so that developers can ship new features faster.

Many companies have already started to create dedicated teams for platform engineering. According to Gartner, by 2026, 80% of software engineering organizations will establish platform teams as internal providers of reusable services, infrastructure components, and tools for application delivery.

## Case studies

### Elkjøp Nordic

<iframe width="560" height="315" src="https://www.youtube.com/embed/aoa_O-rh5KE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Elkjøp Nordic is the leading consumer electronics retailer in the Nordics. The company had a modernization strategy to increase agility of development teams by giving them ownership over their services and the infrastructure that runs them. At the same time, they wanted to create security and compliance guardrails that prevent issues while maintaining developers’ freedom. They accomplished this by building an infrastructure platform application that enabled developers to provision infrastructure running on Kubernetes in Azure. Learn more in the [blog post](/blog/how-elkjop-nordic-enables-developers-to-self-serve-infrastructure/).

### Washington Trust Bank

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q63ZaX340M4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Washington Trust Bank modernized its software development and infrastructure practices since migrating to Azure and adopting infrastructure as code. It enables developers with self-service infrastructure components, prevents developers from deploying forbidden resources with CrossGuard policies, and uses automation to save time and effort.

## Conclusion

Given platform engineering's strong focus on infrastructure management, automation, and standardization, platform engineering teams need a solution that enables them to adhere to the principles of platform engineering while empowering their developers and development teams to leverage the cloud in a secure, scalable, reliable, and consistent way.

![Pulumi's solution for platform teams](/images/product/platform-teams-diagram.png)

Pulumi's solution for platform teams encompasses all of the key requirements described earlier in this article:

1. The _developer control plane_ enables the simple and powerful user experience, allowing platform teams to meet the varying needs of different developers and development teams. The core infrastructure as code tool supports the languages that teams are already familiar with (including TypeScript, Python, Go, C#, Java, and YAML), and leverages the powerful ecosystems surrounding these languages (IDE support, linters, and test frameworks, for example). There's also support for internal developer portals like [AWS Proton](https://aws.amazon.com/proton/) and [Backstage](https://backstage.io).
2. _Integration and delivery_ is key to supporting automation as the default. This includes extensive integration with numerous CI/CD systems as well as Pulumi's own CI/CD offering, called [Pulumi Deployments](/product/pulumi-deployments/). The [Automation API](/automation/) makes it possible to embed IaC into application software, empowering teams to create reusable infrastructure workflows.
3. _Monitoring and logging_ provides the "full visibility on everything" that is a requirement for platform engineering, through support for and integration with leading monitoring, logging, and metric solutions. [Pulumi Insights](/product/pulumi-insights/) provides advanced search (including natural language search), analytics, and artificial intelligence (AI) into [Pulumi Cloud](/product/pulumi-cloud/) to provide actionable knowledge on cloud usage and cost optimizations.
4. _Security and identity_ ensure security is a foundational element. [CrossGuard](/crossguard/) provides policy-based controls---including remediation of policy violations---using the same general purpose programming languages that our core IaC offering supports. [Pulumi ESC](/product/esc) enables centralized access to secrets and configuration information.
5. Pulumi's robust provider ecosystem opens up access to a wide plethora of _resources_ to help ensure that all the necessary services, platforms, and offerings needed to build a well-architected design are available.

Pulumi offers a modern and flexible approach to solving the needs of platform engineering teams. [Request a demo](/request-a-demo) of Pulumi, or [get started using Pulumi's tools](/docs/get-started) today.
