---
title: "Why Switch to Pulumi for Infrastructure as Code?"
date: 2024-07-23T19:47:50-07:00
meta_desc: "Pulumi: the top choice for infrastructure as code. Boost productivity,
  scale infinitely, and leverage AI to revolutionize infrastructure management."
meta_image: meta.png
authors:
  - aaron-kao
tags:
  - infrastructure-as-code
  - platform-engineering
  - ai

social:
  twitter: Why should you switch to Pulumi? This blog post runs through all the reasons
    by use case, by alternatives, and by benefits.
  linkedin:
search:
  keywords:
    - infrastructure
    - switch
    - revolutionize
    - infinitely
    - boost
    - ai
    - code
---

The cloud promised to revolutionize your business.

**Faster innovation. Lower costs. Unlimited scalability.**

But for many companies, that promise remains frustratingly out of reach.
Instead of accelerating product development, infrastructure has
become a bottleneck. You and your team (DevOps, platform, or infrastructure engineering teams)
are bogged down by:

- Clunky tools and manual processes
- Provisioning a simple test environment takes days
- Rolling out updates across regions takes weeks
- The combinations of modern cloud architectures seems infinite

You know there has to be a better way. A way to truly
harness the power of the cloud and turn it into your competitive
advantage.

**But how?**

Enter Pulumi -- the open source infrastructure as code (IaC) platform
that gives 10x better scale, productivity, and time to value for thousands of companies worldwide.

So why should you switch to Pulumi? How is it different from other
infrastructure as code tools? This post should answer all those
questions.

## What is Pulumi?

Pulumi is an infrastructure as code platform that allows you to manage
and scale infrastructure, configurations, policies, and secrets with
programming languages. Pulumi facilitates clear collaboration across your
infrastructure, development, and security teams.

**Pulumi's approach is better.**

**10x Better.** Pulumi takes a unique and 10x better approach to
infrastructure as code by empowering you with the familiar
languages and tools you love for application development. While modern
programming languages have evolved to provide powerful features like AI
copilots, Intellisense, linting tools, testing frameworks, and CICD
pipelines, infrastructure management has lagged behind, relying on rigid
scripting languages and error-prone manual processes. Pulumi bridges
this gap by allowing you to use industry-standard programming
languages to manage infrastructure with the same level of sophistication
and tooling you enjoy for application development. Pulumi embraces the
change and direction the industry is going, so you never fall
behind with your IaC tooling.

**Powering the Next Wave.** Pulumi is at the forefront of the industry.
It helps you embrace the latest practices (e.g., Platform Engineering, GitOps) and
builds the latest technologies (e.g., AI Copilots) into the core user
experience. It also helps you build and manage new technology
paradigms (e.g., AI workloads, LLMs, internal developer platforms).

**Powerful Automations.** Another unique approach is that Pulumi makes it
easy to automate and scale modern cloud architectures. In the last
decade, the industry has moved from monolithic to microservices
architectures, which operate as distributed systems over shared
infrastructure platforms, to achieve greater resilience, team agility,
flexible scaling, and modular codebases. The cloud\'s programmability,
infinite elasticity, and on-demand nature made it easy to spin up
micro-sized services tailored to business demands, facilitated by
technologies like containers, Kubernetes, and serverless. Pulumi empowers you to apply
software engineering to manage infrastructure of this
modern and immense scale.

**AI-Powered.** Pulumi builds AI into the core infrastructure management
experience. Pulumi combines the power of large language models with
semantic understanding of the cloud to unlock greater insights and
controls over managing cloud infrastructure. Pulumi leverages the
familiar GPT experience you know, love, and use daily, so
you can find and take action on any resource in your cloud
environments.

### Ok, but why does this matter enough for me to switch?

Only you can answer that question, but there are some compelling reasons
to adopt the platform trusted by hundreds of thousands of developers.

**Faster Time to Value.** Your company moved to the cloud to
increase innovation and reduce costs. However, getting infrastructure to
developers is a frequent bottleneck for you which can slow down
prototyping new products or shipping new features. Spinning up new
development or testing environments takes days and rolling out
production updates across many regions can take weeks. The existing
tools don't allow you to set security and compliance guardrails and
enable easy self-service of infrastructure.\
\
*Pulumi will speed up your deployments and time to value.*

**Open Platform Commitment.** Some platforms, such as Terraform, have
altered their licensing and introduced uncertainty. They are no longer
true open source, and they tie their previously open source software to
their commercial services. The lack of an open source approach fragments
the community and introduces proprietary constraints to cloud
infrastructure.\
\
*Pulumi provides you with an approach to open source and community that
provides stability and choice.*

**Increased Productivity.** You expect your tools
and workflows to keep up with the industry: AI copilots, Intellisense,
linting tools, testing frameworks, and CICD pipelines. But most of these
innovations are just for building applications and services and not for
infrastructure, configurations, policies, and secrets. Existing
infrastructure tools are fraught with bad UX, rigid scripting languages,
and error prone manual processes.

*Pulumi will increase your productivity and velocity through better tooling.*

**Infinite Scale.** Modern cloud architectures are distributed systems
that are microservices that are dynamic and ephemeral in nature. The
number of infrastructure resource types and the configurable input
properties is staggering. You face the daunting task of how to
combine these resources to solve their unique problems. Without software
engineering, managing these modern distributed systems is fruitlessly
manual.

*Pulumi uses software engineering to tackle the scale of infinite
combinations.*

{{% notes type="info" %}}
Customers of Pulumi frequently experience 100% productivity increases, 99% time saved, and 10x acceleration when using Pulumi compared to what they were using before.

![modern-benefits](modern-benefits.png)
{{% /notes %}}

## Frequently Asked Questions - Why Pulumi?

Here are some frequently asked questions about why you should choose Pulumi based on the following use cases and alternatives:

- [Why Pulumi, by use case?](#why-pulumi-by-use-case)
    - [Why Pulumi for Internal Developer Platforms?](#why-pulumi-for-internal-developer-platforms)
    - [Why Pulumi for AI Workloads?](#why-pulumi-for-ai-workloads)
- [Why is Pulumi better than the alternatives?](#why-is-pulumi-better-than-the-alternatives)
    - [Why Pulumi vs. clickops?](#why-pulumi-vs-clickops)
    - [Why Pulumi vs. Terraform?](#why-pulumi-vs-terraform)
    - [Why Pulumi vs. AWS CDK?](#why-pulumi-vs-aws-cloud-development-kit-cdk)
    - [Why Pulumi vs. 3rd party IDP providers?](#why-pulumi-vs-3rd-party-idp-providers-think-port-cortex-backstage)
- [How can I switch to Pulumi?](#how-can-i-switch-to-pulumi)

### Why Pulumi, by use case?

There are many different use cases for why you might use Pulumi:
infrastructure CICD, modern applications, internal developer platforms,
AI/ML workloads, and infrastructure modernization. Below are more
details on two popular use cases.

#### Why Pulumi for Internal Developer Platforms?

You and your team may build internal developer platforms (IDPs) to
maximize the use of the cloud at scale across the company while
being secure and compliant, so your development teams can ship faster. There are a number of components/layers that are considered basic requirements when building an internal
developer platform. The layers are as follows:

- **Developer Control Plane.** Curated experiences that empower
    developers by meeting them at their level of expertise, whether
    it\'s an abstracted developer portal, custom CLI, or shared IaC
    templates.

- **Integration & Delivery.** Automations to version control, test,
    trace, and deploy all infrastructure from resources, configurations,
    environments, and secrets as well as orchestration automations to
    manage provisioning workflows.

- **Monitoring & Logging.** Components to log, monitor, and observe
    all infrastructure for greater operational control as well as
    optimize against unnecessary costs.

- **Security & Identity.** Security and compliance guardrails that
    regulate every piece of infrastructure from policies to fine-grained
    access controls to secrets.

- **Resources.** Providers that support modern cloud architectures
    such as Kubernetes, containers, serverless, generative AI, machine
    learning, data lakes, hybrid cloud/on-premises, and more.

This diagram illustrates the different layers of an internal developer
platform:

![platform-requirements](platform-req-diagram.png)

Most solutions struggle to keep up with the requirements of each layer.
Many of the alternative solutions can't handle the scale of resources you need to
manage, find it difficult to tie infrastructure automation directly
into your core business, have leaky secrets, and enforce compliance and
security incompletely.

Pulumi is a platform engineering solution that enables you to
build a bridge to your developers and empower them to leverage the
cloud with security, scalability, repeatability, and consistency. It provides
 the building blocks for each of the five layers.

![pulumi platform](platform-pulumi-diagram.png)

- **Developer Control Plane.** Pulumi is the simplest and most
    intuitive way to manage cloud infrastructure because of its ability
    to use standard programming languages, including YAML. This removes
    the friction to the basic requirements of managing cloud
    infrastructure well. Pulumi Automation API makes it simple to code
    any user interface for a developer portal / CLI. Pulumi also
    provides private templates that integrate with developer
    portals like AWS Proton and Backstage.

- **Integration & Delivery.** Pulumi Automation API can embed IaC
    programs directly in applications, resulting in 10x greater
    management of resources per engineer. Pulumi can take advantage of
    all existing testing frameworks supported by the selected
    programming language.

- **Monitoring & Logging.** Pulumi Insights adds advanced search,
    analytics, and AI to any cloud infrastructure, giving unique
    insights into cloud usage and cost optimizations. Pulumi partners
    with leading observability solutions making it easy to manage
    monitoring and logging resources through IaC.

- **Security & Identity.** Pulumi CrossGuard provides policy as code with
    auto-remediation. Pulumi ESC makes it easy to manage secrets and configurations
    for every environment. Access to each cloud resource and secret can be granularly
    controlled and audited.

- **Resources.** Pulumi supports modern cloud architectures such as
    Kubernetes, containers, serverless, generative AI, machine learning,
    data lakes, hybrid cloud/on-premises, and more. Pulumi makes it
    simple to create components that abstract away the complexity of
    managing thousands of resources across hundreds of distinct clouds.

***Pulumi is purpose built to make all aspects of platform engineering
vastly simpler.***

[Read more >>](/product/internal-developer-platforms/)

#### Why Pulumi for AI Workloads?

Your company may be using AI to increase innovation and reduce costs.
AI gives them the ability to design richer and more intuitive interfaces
for their products and/or services to connect better with their
customers. The hardest part of AI is at times not the AI pieces but
the cloud infrastructure parts:  how to provision and manage the
infrastructure that AI workloads run on (e.g., compute and networking)
and depend on (e.g., databases and storage).

There are many layers to building and managing AI applications: model
training, data pipelines, backend services, frontend applications.

![ai stack](ai-stack.png)

Pulumi provides an abstraction across all the different layers of the AI
stack (web framework, LLM, containers, databases, secrets, policies,
configurations, etc) as a simple Python library. Through this
abstraction you can manage stacks of AI infrastructure as code.

![ai abstraction](ai-dev.png)

***Pulumi makes it trivial to take local AI development to production in
the cloud.***

[Read more >>](/solutions/ai/)

### Why is Pulumi better than the alternatives?

There are many different tools you can use to manage infrastructure. However, Pulumi provides
you with a more productive authoring experience and more powerful automations that will allow you to
ship faster and manage the infinite scale of cloud infrastructure. Read on for how Pulumi compares to specific options: clickops, Terraform, CDK, and IDP services.

#### Why Pulumi vs. clickops?

Manually provisioning and managing infrastructure for production via the
cloud console (i.e., clickops) is a bad idea. There isn't repeatability
or consistency which leads to errors, and that can lead to downtime or
worse, security breaches. That is why infrastructure as code was
invented as a way to have a single source of truth for all
infrastructure with changes 100% automated.

If you don't believe this, just ask any cloud or devops
subreddit, Slack group, or Discord server.

#### Why Pulumi vs. Terraform?

Pulumi and Terraform are both infrastructure as code (IaC) platforms,
however they have fundamental differences in how they approach your needs
of infrastructure management. First, here are the similarities.

Both Pulumi and Terraform include the ability to create, deploy, and
manage infrastructure as code on any cloud. Both Terraform and Pulumi
follow a desired state infrastructure as code model, where the IaC code
represents the desired state of the infrastructure. The deployment
engine compares this desired state with the current state of the stack
and determines the necessary actions, such as creating, updating, or
deleting resources. Both Terraform and Pulumi support many cloud
providers, including AWS, Azure, and Google Cloud, plus other services
like CloudFlare, Digital Ocean, and more.

However, beyond the basics of infrastructure as code there are
significant differences that affect productivity,
scalability, and collaboration.

- **Increased Productivity.** As discussed at the beginning,
    Pulumi's promise is to build in all the
    latest advancements in both the developer and operations experience.
    When you write Pulumi code, you now have AI copilots that can pair program with you,
    IDEs that have autocompletion and Intellisense squiggles, powerful libraries of low
    level and abstract functions, testing frameworks, code review tools, automated release controls via CICD pipelines, and great software packaging tools. When it
    comes to managing infrastructure with Pulumi, you also have Pulumi Copilot which combines
    the best generative AI models available in the industry today with
    access to your data and actions within Pulumi
    Cloud. Pulumi Copilot incorporates the context of where you are
    in the Pulumi Cloud console to easily answer questions about "this
    stack" or "the latest update" as well as automating cloud tasks.
    Terraform, on the other hand, has built a proprietary
    ecosystem that doesn't tap into the latest advancements of how code
    is written or how infrastructure is managed.

- **Greater Scalability.** Pulumi embraces software engineering as a
    way to solve and manage the exponentially increasing complexity of
    modern architectures. Programming languages with their loops,
    conditional logic, class inheritance, object orientedness allows
    engineers to design more complex and sophisticated infrastructure
    compared to using HCL. Pulumi also allows you to build custom
    workflows atop infrastructure programs, giving rise to
    event-driven automations or internal developer portals that provide
    self-service.

- **Better Collaboration.** Pulumi makes it easy to prototype new
    products and quickly ship them into production because it is easier
    for the platform, development, and security teams to collaborate.
    You (platform engineering and devops teams) can define and manage common
    infrastructure across the company, work with the security teams
    to set security and compliance guardrails, and enable easy
    self-service of infrastructure whether through custom developer
    platforms or shared infrastructure libraries. To define common
    company-wide components, if you don't want to program can use use YAML; if you
    do, you can use Python, TypeScript, Golang, C\#, etc. These components can be consumed by
    the development team in their own IaC program in any programming
    language with the development tools they already know. It\'s easy to
    start with YAML and move to other languages when more power is
    desired. With Terraform, you must understand and use HCL. It
    is difficult to build self-service infrastructure platforms because it
    lacks the programmability and ability to apply software engineering.
    It\'s just harder to bring together platform, development, and
    security teams and empower them with tools that work. Whereas Pulumi
    unblocks infrastructure as the bottleneck for software delivery.

[Read more >>](/docs/concepts/vs/terraform/)

#### Why Pulumi vs. AWS Cloud Development Kit (CDK)?

Pulumi and CDK are similar in that both allow you to use programming
languages to write infrastructure as code. However, there are some key
differences:

- **No Vendor Lock-In.** CDK supports only AWS, whereas Pulumi
    supports over 150 cloud and SaaS providers, with more being added
    all the time. CDK depends on CloudFormation as the deployment
    engine; it shares many of the same benefits and limitations as
    CloudFormation (see [Pulumi vs.
    CloudFormation](https://www.pulumi.com/docs/concepts/vs/cloud-templates/cloudformation/))

- **Execution > Translation.** Pulumi and CDK support similar
    programming languages but differ fundamentally in their deployment
    approaches. Pulumi\'s engine directly understands these languages
    and communicates with cloud providers. In contrast, CDK transpiles
    code into AWS Cloud Assembly, an intermediate format consisting of
    CloudFormation templates and other assets, before deployment via
    CloudFormation. This difference impacts your development speed and
    correctness. CDK\'s approach can lead to slower deployments and
    delayed error discovery, potentially hours into the process since
    the errors aren't caught during compile time. Additionally, you need expertise in both CloudFormation and CDK for effective
    debugging and successful deployments, whereas Pulumi\'s direct
    approach simplifies this process.

- **Versatility.** CDK and Pulumi both support automated testing, but
    Pulumi offers more versatile options. While both allow unit testing,
    Pulumi\'s deep integration between language and runtime enables
    fast, offline tests (in-memory) with mocked cloud provider calls. In
    contrast, CDK only permits assertions against synthesized
    CloudFormation templates and lacks offline testing capabilities.
    This makes Pulumi\'s testing approach more comprehensive and
    flexible than CDK\'s.

[Read more >>](/docs/concepts/vs/cloud-template-transpilers/aws-cdk/)

#### Why Pulumi vs. 3rd party internal developer portal providers?

There are many third party providers of internal developer portals (think Port, Cortex, Backstage).
Some are services and others are open source software. These providers
are similar in that they offer simple developer portals that
are a single part of a greater infrastructure management platform.

As discussed earlier, internal developer platforms have five layers:
developer control plane, integration & delivery, monitoring & logging,
resources management, and security & identity. Most of these providers
offer easy to use GUI consoles, simple CICD integrations, comprehensive
suite of monitoring & logging, and some form of role-based access
controls. However, they lack the infrastructure as code fundamentals and
automation capabilities that Pulumi has, which enable you to build powerful
customizations through software engineering. Many of these solutions
also lack strong secrets management and policy enforcement capabilities
that are critical for production and enterprise deployments.

That said, if you need an off the shelf solution, then one of these
services or software might be a good choice for you. Some of these solutions can
integrate with Pulumi, and if your needs become more complex, you can always switch to
Pulumi later.

{{% notes type="info" %}}
Have a particular ***Pulumi vs X***
comparison that you need thoughts on? Feel free to join the [Pulumi Community
Slack](http://pulumi) if you have quick technical
questions, or talk to a [Solutions Architect](https://www.pulumi.com/contact/?form=tf-migration) if you need more detailed
consultation about your specific architecture.
{{% /notes %}}

### How can I switch to Pulumi?

Switching to Pulumi doesn't have to be intimidating. We've done this
with thousands of customers before, and we can guide you through it.

We provide self-service conversion tools that allow you to Import
infrastructure no matter how it was provisioned, click-ops included. You
can also use tools to convert your HashiCorp Terraform, AWS
CloudFormation, Azure Resource Manager (ARM) templates, or Kubernetes
YAML.

[Self-service Tool
Guide](https://www.pulumi.com/docs/iac/adopting-pulumi/)

If you need help, we have a team of cloud experts who can answer your
questions, give you a demo, or roll up their sleeves to get your
migration done.

[Contact Expert
Services](https://www.pulumi.com/contact/?form=tf-migration)

We have done lots of migrations from all types of infrastructure as code
tools, and we are happy to help you think through how to make switching
to Pulumi as easy as possible.

{{< blog/cta-button "Switch to Pulumi" "https://www.pulumi.com/contact/?form=tf-migration" "_blank" >}}

*Meta image credit: [ESO/M. Kornmesser](https://www.eso.org/public/images/eso2402a/)*
