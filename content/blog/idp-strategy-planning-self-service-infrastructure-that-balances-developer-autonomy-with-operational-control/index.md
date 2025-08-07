---
title: "How to Build an Internal Developer Platform: Strategy, Best Practices, and Self-Service Infrastructure"
allow_long_title: true
# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-08-07T15:13:02+02:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false


series: idp-best-practices

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Learn how to design and implement an effective Internal Developer Platform (IDP) strategy with reusable components, blueprints, and self-service infrastructure.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - mitch-gerdisch
    - engin-diri

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - internal-developer-platform
    - platform-engineering
    - developer-experience
    - self-service
    - governance
    - components
    - templates
    - idp-best-practices

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
    twitter: "Building an Internal Developer Platform that truly empowers developers while maintaining operational control requires strategic thinking. Our latest post breaks down the 5 essential components every IDP needs to succeed. #platformengineering #devops #idp"
    linkedin: "At Pulumi, we've worked with countless platform teams facing the same challenge: how do you accelerate developer productivity without compromising on security, compliance, and governance? Our latest blog post dives deep into the strategic approach to IDP planning, covering the five essential components that separate successful platforms from those that struggle to gain adoption. Learn how abstractions, blueprints, workflows, security guardrails, and self-service capabilities work together to create developer platforms that truly transform how organizations deliver value. #platformengineering #developerexperience #infrastructureascode #pulumi"

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Welcome to the first post in our **IDP Best Practices** series. In this guide, we’ll walk through the strategic foundations for designing an Internal Developer Platform that empowers developers without sacrificing governance, security, or operational control.

At Pulumi, we’ve worked with hundreds of teams facing the same core challenge:  **How do you give developers the infrastructure access they need, while maintaining the governance and security your organization requires?**

That tension is at the heart of every IDP conversation.  
Teams want to **move faster and innovate**, but also need to stay compliant, control costs, and maintain operational stability.

The good news? You can do both, with a clear strategy and the right approach.

This series shares proven best practices for designing, building, and scaling IDPs using Pulumi.  

<!--more-->

These lessons come from real-world implementations across industries and company sizes—and are built to grow with you.

This post is part of our IDP Best Practices series. You can explore the full series below:

* **How to Build an Internal Developer Platform: Strategy, Best Practices, and Self-Service Infrastructure** (you are here)
* **Build Golden Paths with Infrastructure Templates and Components**
* **Policy as Code for Safer IDPs: Enabling Developer Self-Service with Guardrails**
* **Day 2 Platform Operations: Automating Drift Detection and Remediation**
* **Extend Your IDP for AI Applications: GPUs, Models, and Cost Controls**
* **Next-Gen IDPs: How to Modernize Legacy Infrastructure with Pulumi**
{{% notes type="tip" %}}
**Want hands-on experience building an Internal Developer Platform?**  Enroll in the free [IDP Builder Workshop Series](https://info.pulumi.com/idp/internal-developer-platform-workshops-course)** to access recordings, demo code, slides, and hands-on guidance.
{{% /notes %}}

## Understanding the Platform Engineering Layers in Your IDP

![img.png](img.png)

When we work with customers on their platform strategy, we often start by referring to the "platform engineering layer cake."
Here is a quick walkthrough of each layer and how Pulumi IDP constructs fit this layer cake approach:

**Layer 1: Infrastructure Layer** - This is your raw cloud resources: VMs, databases, networks, storage.
These are the fundamental building blocks that exist in AWS, Azure, GCP, and other cloud providers.

**Layer 2: Platform Layer** - This is where [Pulumi Components](https://www.pulumi.com/docs/iac/concepts/resources/components/) live.
Components take those raw infrastructure resources and package them into higher-level abstractions that encapsulate best practices, security policies, and organizational standards.
For example, instead of manually configuring 15 different AWS resources to create a secure web application, you create a component that handles all that complexity and exposes just the configuration options that matter to your developers.

**Layer 3: Developer Experience Layer** - This is where [Pulumi Templates](https://www.pulumi.com/templates/) and the [Private Registry](https://www.pulumi.com/docs/pulumi-cloud/private-registry/) come into play.
Templates provide ready-to-deploy patterns that developers can customize, while the private registry makes everything discoverable and manageable at scale.

In our workshop, we focused specifically on those top two layers because that's where the transformation happens. This is where you turn raw infrastructure into something developers can actually use productively without becoming infrastructure experts themselves.

Here's how this maps to what you're actually building:

### Infrastructure Layer → Raw Cloud Resources

Your foundation is still the same: AWS EC2 instances, Azure Virtual Networks, GCP Cloud Functions.
Pulumi's providers give you access to these resources using real programming languages instead of YAML or proprietary DSLs.

### Platform Layer → Pulumi Components

This is where you create your reusable building blocks. A component might encapsulate:

- A complete microservice infrastructure pattern (load balancer, auto-scaling group, database, monitoring)
- A secure data pipeline (storage, processing, access controls, encryption)
- A standardized Kubernetes application deployment (ingress, service, deployment, secrets management)

Components are written once in any supported language (TypeScript, Python, Go, .NET, Java) but can be consumed by teams using any of these languages.
This is crucial. Your platform team might write components in Go, but your application teams can consume them in Python or TypeScript.

### Developer Experience Layer → Templates + Private Registry

Templates are complete, deployable projects that use your components. They provide:

- Getting started patterns: "Deploy a new microservice"
- Reference architectures: "Deploy a three-tier web application"
- Environment patterns: "Set up a complete dev/staging/prod pipeline"

The Private Registry is your distribution mechanism.
It's where components and templates become discoverable, versioned, and manageable.
Developers don't need to hunt through Git repositories or Slack channels to find the right building blocks. Everything is catalogued, documented, and accessible through familiar package management workflows.

## IDP Example: Building a Web Application Platform Step-by-Step

Let's make this concrete with an example from our workshops.
Say you want to enable teams to deploy secure web applications:

**Infrastructure Layer:** You need an Application Load Balancer, EC2 Auto Scaling Group, RDS database, VPC with proper subnets, Security Groups, IAM roles, CloudWatch monitoring, and S3 bucket for static assets.
That's about 20+ individual AWS resources that need to be configured correctly and securely.

**Platform Layer (Components):** You create a `WebApplication` component that encapsulates all this complexity.
Your component exposes simple configuration options like:

```typescript
const app = new WebApplication("my-app", {
    instanceType: "t3.medium",
    minSize: 2,
    maxSize: 10,
    databaseSize: "small",
    environment: "production"
});
```

Behind the scenes, your component handles all the security configurations, networking setup, monitoring, and best practices.
You publish this component to your private registry.

**Developer Experience Layer (Templates):** You create templates like:

- `web-app-starter`: A simple web application using your `WebApplication` component
- `microservice-template`: API service with database and monitoring
- `full-stack-template`: Frontend, backend, and database in a complete environment

Developers can now run `pulumi new web-app-starter` and get a production-ready, secure web application in minutes instead of weeks.
The template uses your component, which handles all the underlying infrastructure complexity.

This layered approach solves the core challenge we see every platform team struggling with: how do you provide developers with the infrastructure they need without creating operational bottlenecks or compromising security standards.

## Why Internal Developer Platforms Matter in 2025 and Beyond

While DevOps brought us incredible advances in how we ship and maintain software, we've watched many organizations struggle with the unintended consequences: tool sprawl, Day 2 operational pain, and developers who are drowning in infrastructure complexity.

That's why platform teams have emerged.
You exist to solve these challenges by building tools and workflows that enable your internal customers (the developers) to provision infrastructure and deploy software without getting blocked.
But here's the thing I've learned from working with hundreds of platform teams: success isn't just about the tools you choose.
It's about the strategy behind how you implement them.

## 5 Core Components of a Successful Internal Developer Platform

Through years of working with platform teams and analyzing what separates successful IDPs from those that struggle to gain adoption, we've identified five essential components that every platform strategy needs.
These aren't theoretical concepts. They're battle-tested patterns that work across organizations of all sizes and industries.

### 1. Abstractions

Let me be clear about something: abstractions aren't about dumbing down infrastructure for developers.
The abstraction is really where you're hiding the complexity of the underlying infrastructure from your end users, but you're doing it intentionally to provide appropriate interfaces for different personas in your organization.

We've seen too many platform teams get this wrong by either over-abstracting (creating black boxes that developers can't customize) or under-abstracting (exposing too much complexity).
The sweet spot is creating [component resources](https://www.pulumi.com/docs/iac/concepts/resources/components/) that encapsulate your infrastructure patterns and best practices into reusable building blocks that can be consumed across different programming languages and deployment scenarios, while still providing escape hatches when needed.

### 2. Blueprints

Blueprints are your templatized, well-architected patterns that developers can use to bootstrap their infrastructure.
But here's what I want you to understand about blueprints: they're not just starting points that you throw over the wall to developers.
They're carefully designed patterns that embody your organizational best practices and architectural decisions.

When we see successful platform teams, their templates serve as both accelerators and guardrails.
They give developers a fast path to production-ready infrastructure while ensuring that everything they deploy follows your organization's standards.
That's the power of good blueprint design: speed and compliance working together, not against each other.

### 3. Workflows

Here's where many platform teams get trapped: they try to build one workflow to rule them all.
But in our experience working with organizations across every industry, you need to support multiple consumption patterns because you have multiple types of users.
You need:

- **No-code workflows** for users who want point-and-click deployment (think product managers or junior developers who just need to spin up a database)
- **Low-code workflows** using tools like [Pulumi YAML](https://www.pulumi.com/docs/iac/languages-sdks/yaml/) for configuration-driven infrastructure (perfect for developers who understand infrastructure but don't want to write Go or TypeScript)  
- **Full-code workflows** for developers who need maximum flexibility and want to leverage the full power of general-purpose programming languages

The key insight? These aren't three different platforms.
They're three different interfaces to the same underlying components and templates.

### 4. Security guardrails

This is probably the most important distinction we can share with you: you want to have guardrails, not gates.
Too many platform teams create approval processes and manual checkpoints that completely undermine the self-service promise they're trying to deliver.

Guardrails are different.
They start with best practices and security built into the reusable abstractions from the start. But even the most secure solutions needs a safety net.
They're policy-as-code that runs automatically, preventing violations before deployment happens.
When we work with customers on implementing [Pulumi CrossGuard](https://www.pulumi.com/crossguard/), we're not creating new friction. We're embedding security, compliance, and cost controls directly into the deployment process.
The developer gets immediate feedback, and you get the assurance that nothing goes to production without meeting your standards.

### 5. Self-service

Everything we've talked about so far builds toward this moment: enabling developers to provision and manage infrastructure independently.
But self-service isn't just about providing a UI. It's about carefully orchestrating all the other components to create experiences that are both powerful and intuitive.

When we walked through the demo in our workshop, what you saw was the culmination of thoughtful platform design.
Developers can discover available services, deploy infrastructure through whatever interface makes sense for them, and manage their resources over time, all without requiring tickets or manual intervention from platform teams.
That's the promise of a well-designed IDP: developer autonomy without operational chaos.

## How to Implement Your Internal Developer Platform Strategy

### Supporting Different Personas in Your IDP Design

One of the biggest mistakes we see platform teams make: they try to build for their most sophisticated users first.
But here's what I've learned from working with hundreds of organizations: you need to think about all your personas from day one.

In most organizations, you're serving:

- **Infrastructure engineers** who want full control and flexibility (they'll use the full-code workflows)
- **Application developers** who need infrastructure but prefer higher-level abstractions (perfect for low-code approaches)
- **Non-technical users** who want simple, point-and-click deployment (your no-code users)

The breakthrough insight that separates successful platform teams from struggling ones is this: all these personas can be served by the same underlying components and templates, just consumed through different interfaces.
You don't need to build three different platforms—you need to build one platform with three different consumption models.

### Why a Private Registry Is Key to IDP Adoption

Here's something we always tell platform teams: if you don't solve the discoverability problem, your beautiful components and templates will sit unused in Git repositories where no one can find them.
That's why the private registry isn't just a nice-to-have. It's the foundation that makes everything else work.

When you establish a private registry as your source of truth for components, templates, providers, and policies, you're solving two critical problems at once.
First, discoverability: developers can actually find and explore what's available.
Second, lifecycle management: you can see where each package is being used, track version drift, and understand the impact of changes before you make them.

The workflow is beautifully simple: you publish standardized building blocks with a single `pulumi publish` command, and developers discover and consume these assets through familiar package management workflows they already know.

### Aligning Your IDP to Organizational Context and Services

One pattern we see in every successful IDP implementation is that the platform reflects how the organization actually works.
Your developers don't think in terms of individual stacks or resources. They think in terms of services, applications, and business functionality.

That's why we built [Pulumi Services](https://www.pulumi.com/docs/pulumi-cloud/insights/services/) to let teams logically group stacks, environments, and resources in ways that make sense to your organization.
This isn't just about better organization. It's about enabling effective Day 2 operations.
When something breaks at 2 AM, your on-call engineer needs to understand dependencies, track usage, and manage infrastructure in the context of the business services that are actually impacted.

## How to Measure the Success of Your Internal Developer Platform

Here's something that might surprise you: the most successful platform teams we work with don't measure their success by how many cool features they've built.
They measure success by the business outcomes they're driving:

- **Reduced time-to-market** through faster infrastructure provisioning (because at the end of the day, your platform exists to help the business move faster)
- **Improved developer productivity** by eliminating infrastructure bottlenecks (happy developers ship more features)
- **Enhanced security posture** through consistent policy enforcement (security that doesn't slow people down is security that actually gets used)
- **Lower operational overhead** through standardization and automation (because your platform team's time is better spent on innovation than toil)

The numbers speak for themselves.
We've worked with customers like Snowflake who reduced deployment times from one and a half weeks to less than a day.
Starburst Data cut their infrastructure deployments from two weeks to just three hours.
These aren't vanity metrics. They're business transformations.

## IDP Strategy: 5 Key Steps to Build a Strong Foundation

If you're just starting your IDP journey, here's the roadmap we give to every platform team we work with:

1. **Start with user research:** Before you write a single line of code, go talk to your developers.
   Understand your different personas and their actual needs, not what you think they need. Do your users like to work from the command line? Do they prefer interacting with a UI? 

2. **Identify common patterns:** Look for infrastructure patterns that get repeated across teams.
   These are your goldmine—the patterns that, once abstracted and templatized, will provide immediate value.

3. **Begin with components:** Build reusable infrastructure building blocks before you worry about fancy UIs or workflow orchestration.
   You need solid foundations before you can build the house.

4. **Implement progressive disclosure:** Give people simple interfaces for common use cases, but always provide escape hatches for complex scenarios.
   The moment your abstraction becomes a prison, developers will route around it.

5. **Measure and iterate:** Track adoption and gather feedback religiously.
   Your platform is only as good as its adoption rate, and adoption only happens when you're solving real problems for real people.

## The Future of IDPs and Platform Engineering

Trends come and go, but platform engineering is here to stay.
It's not just another tool or methodology. This is how modern organizations scale infrastructure to match the speed of innovation. The companies that win are the ones that treat their **Internal Developer Platform (IDP)** as a strategic foundation, not just a tool.

Your job isn’t just to manage infrastructure and choose the right tools - it's to enable developers to move faster while keeping governance, security, and costs under control. Get that balance right, and your platform becomes a force multiplier across your entire engineering department.

The fastest way to get there? Focus on these five essential components:

* **Abstractions**  
* **Blueprints**  
* **Workflows**  
* **Security guardrails**  
* **Self-service**

Together, they turn your IDP into more than just infrastructure automation, they create a platform that developers trust and your business relies on.

### *Ready to build a modern IDP that scales?

Pulumi makes it easy to go from static IaC to dynamic, self-service infrastructure with real programming languages and built-in guardrails.


Explore [Pulumi IDP](https://www.pulumi.com/product/internal-developer-platforms/) or [sign up for free](https://app.pulumi.com/signup) to get started today.
