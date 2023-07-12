---
title: What is Platform Engineering?
allow_long_title: true
meta_desc: |
    Understand what platform engineering is, along with the main benefits and importance
    for modern application development.

type: what-is
page_title: What is Platform Engineering?

---

## What is platform engineering?

Platform engineering is a set of modern engineering practices where infrastructure teams build shared tools and services to help development teams develop, deploy, and operate cloud infrastructure on a self-service basis. This includes cloud infrastructure, container orchestration platforms, databases, networking, monitoring, code repositories, and deployment pipelines.

Platform teams use a customer-driven mindset where they treat the application developers that they serve as customers that must be understood and won over through products that solve their problems. The products these teams offer are infrastructure tools and building blocks that development teams use to provision and manage standardized infrastructure for their applications and services. Typically, these tools have built-in guardrails that enforce best practices and security standards without impeding developers’ agility and workflow.

The responsibilities of a platform engineer may include the following:

* Providing development teams with self-service infrastructure tooling and golden paths to production

* Defining and creating standardized cloud architectures used by development teams, typically using an [infrastructure as code framework](/what-is/what-is-infrastructure-as-code/)

* [Automating infrastructure and operational tasks](/automation/) using tools such as infrastructure as code and continuous integration/delivery (CI/CD) pipelines

* Improving internal infrastructure tooling and processes in order to improve developer productivity, increase velocity, and reduce errors and downtime

* Defining and enforcing best practices and security standards for infrastructure, such as by using a [policy as code framework](/crossguard)
Researching and evaluating new technologies and tools to continually improve internal tooling

## What is a platform engineer?

Platform engineer is a term used to describe the engineers that make up a platform team. Typically, these engineers have the multi-disciplinary skills, experience, and empathy needed to build a great product, serve developers’ needs, and “go to market” within their company. Often, they have experience with multiple engineering disciplines like infrastructure or DevOps and software engineering. The reality is that many engineers who perform platform engineering responsibilities do not have the title “platform engineer.” In practice they have varying job titles like software engineer, DevOps engineer, SRE, cloud architect, cloud engineer, and more. By providing developers with infrastructure and tooling to deploy and operate their applications efficiently, platform engineers enable developers to focus on building great software.

## Why is platform engineering important?

Developers need infrastructure to run their applications and services. Traditionally, companies have used central infrastructure teams that provision and manage infrastructure on behalf of developers, but this model is prone to bottlenecks as developer requests for infrastructure overwhelm central teams. As modern development teams have taken responsibility over owning and operating their own infrastructure, they also need simple and fast ways of provisioning it while adhering to best practices.

Platform teams solve these challenges:
* The cloud is too complex and unwieldy for most developers to use without abstractions and tooling
* Developers need to know which infrastructure resources to provision
* Developers need an easy way to provision, configure, and manage infrastructure
* Infrastructure provisioned by developers needs to adhere to company best practices

Platform engineering can increase development velocity, improve security, increase infrastructure's adherence to best practices, and reduce operational costs through automation. It helps organizations increase the ROI on cloud investments and improves the software delivery lifecycle so that developers can ship new features faster.

Many companies have already started to create dedicated teams for platform engineering. According to Gartner, by 2026, 80% of software engineering organizations will establish platform teams as internal providers of reusable services, infrastructure components, and tools for application delivery.

## What are the main approaches to platform engineering?

There are three main approaches that platform teams are using to enable developers to self-service infrastructure.

### Infrastructure libraries

Infrastructure libraries express infrastructure resources and configurations in code. These libraries are used to provision infrastructure using an infrastructure as code tool.

### Infrastructure CLIs

Infrastructure CLIs allow developers to provision and manage infrastructure through a familiar command-line interface similar to Heroku.

### Infrastructure platform

These are typically web applications that provide a graphical user interface for developers to provision and manage infrastructure.

## Case studies

### Elkjøp Nordic

<iframe width="560" height="315" src="https://www.youtube.com/embed/aoa_O-rh5KE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Elkjøp Nordic is the leading consumer electronics retailer in the Nordics. The company had a modernization strategy to increase agility of development teams by giving them ownership over their services and the infrastructure that runs them. At the same time, they wanted to create security and compliance guardrails that prevent issues while maintaining developers’ freedom. They accomplished this by building an infrastructure platform application that enabled developers to provision infrastructure running on Kubernetes in Azure. Learn more in the [blog post](/blog/how-elkjop-nordic-enables-developers-to-self-serve-infrastructure/).

### Washington Trust Bank

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q63ZaX340M4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Washington Trust Bank modernized its software development and infrastructure practices since migrating to Azure and adopting infrastructure as code. It enables developers with self-service infrastructure components, prevents developers from deploying forbidden resources with CrossGuard policies, and uses automation to save time and effort.

## Choosing an infrastructure as code framework

Choosing an infrastructure as code framework is an important foundation of a platform engineering strategy because it impacts how infrastructure is modeled, tested, distributed, and deployed across an organization. In particular, the choice of IaC language affects infrastructure’s usability, reusability, and capacity for scale. General-purpose languages provide major advantages because they are widely adopted already, have more flexibility and expressiveness than DSLs, and come with rich ecosystems of tools and frameworks that increase productivity. Last but not least, it’s much easier for developers to use IaC when it’s written in languages they already know.

Pulumi is open-source infrastructure as code in any programming language including TypeScript, Python, Go, C#, Java, and YAML. It supports all major clouds and over 120+ cloud and SaaS providers. [Try it out for free](/docs/get-started/).