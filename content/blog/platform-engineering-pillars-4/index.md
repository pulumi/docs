---
title: "Improve Developer Experience: Increase Dev Productivity with Internal Developer Platforms"
allow_long_title: true
date: 2025-03-13
updated: 2025-08-12
draft: false
meta_desc: Learn how to boost developer experience, productivity, and velocity with an internal developer platform using service catalogs, templates, and CI/CD.
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - platform-engineering
    - platform-engineering-pillars
series: platform-engineering-pillars
social:
    twitter: >
            Developer Experience: the key to platform engineering success! Learn how to eliminate friction points, implement standardized templates, and build fast CI/CD pipelines that help developers achieve flow state and ship features faster.
    linkedin: >
            Developer experience is critical for successful platform engineering. Is your organization creating unnecessary friction?

            🚨 The Challenges:
            • Inconsistent development environments
            • Manual setup processes
            • Slow feedback loops
            • Fragmented tooling and documentation

            🛠️ The Solution:
            Implement streamlined workflows, standardized templates, and integrated CI/CD pipelines as core components of your internal developer platform.
---

In the last article in this [Platform Engineering Pillars series](/blog/tag/platform-engineering-pillars/), we explored how **self-service infrastructure** frees developers from bottlenecks and dependency gates. By providing reusable infrastructure modules and intent-based configurations, platform teams dramatically reduce infrastructure friction. This self-service model powers faster deployments, increased autonomy, and fewer delays.

However, **infrastructure provisioning alone isn’t enough to improve developer experience**. Even with efficient provisioning, developers can still face inconsistent local setups, sluggish CI/CD pipelines, poor documentation, and fragmented tooling. These obstacles quietly reduce **developer productivity**, slow **developer velocity**, and increase operational overhead.

<!--more-->

{{< youtube "is83TV8nrTg?rel=0" >}}

Your platform’s ability to support daily workflows directly impacts core success metrics like **time to first commit**, **time to production**, and **developer satisfaction**.

{{% notes "Metrics Explainer: Measuring Developer Experience" %}}

When improving **developer experience** as part of a platform engineering initiative, measure:

- **Time to First Commit** – How quickly a developer can become productive in a new environment or project. Pay particular attention to new hires.
- **Time to Production** – How fast code moves from commit to successful production release.
- **Developer Satisfaction** – Regularly survey friction points and prioritize fixing the top issues.

**Friction logs** are also a powerful way to identify roadblocks, recording every obstacle encountered during common workflows. This reveals hidden friction and provides a roadmap for improvement.

{{% /notes %}}

A great **developer experience** accelerates iteration, improves problem-solving, and drives better products. An **internal developer platform (IDP)** designed for [DevEx is a fundamental competitive advantage](https://www.pulumi.com/blog/developer-experience-business-critical/).

## The Service Catalog: Foundation for Developer Experience

Developer friction often starts with something simple: not knowing what’s already available or who owns it. Without a single, reliable source of truth, developers reinvent the wheel, duplicate work, and waste time chasing information.

A well-structured **service catalog** in your internal developer platform addresses this by providing a central repository for all services and applications. At its most basic, it's just a web page with each service's README, service metadata, and operational information.

But, properly structured, this delivers some large benefits:

1. **Context at a Glance**: Every catalog entry follows a standardized template, capturing core information such as purpose, interfaces (REST, gRPC, events, etc.), language/runtime, and environment requirements. New developers can quickly grasp a service's role and easily jump into productive work.

2. **Discoverability and Reuse**: Without a catalog, teams often recreate services they don't realize already exist. Duplicate services not only waste resources but lead to fragmented knowledge and inconsistencies. With a catalog, developers quickly find and leverage existing solutions, increasing reusability and reducing churn.

3. **Ownership Transparency**: Each entry in the catalog explicitly names team ownership, CODEOWNERS files, and pertinent contact details like Slack channels or on-call rotations. Clear ownership streamlines communication, issue resolution, and collaboration, saving precious time and avoiding frustrations.

A **service catalog** supports autonomy, reduces wasted cycles, and increases **developer velocity** by making essential information instantly accessible.

But a Service Catalog alone isn't enough. To fully streamline and enhance your development workflow, you must pair it with consistent local environments and reliable CI/CD processes. Both of which can be serviced by standardized service templates.

## Service Templates: Golden Paths for Improving Developer Productivity

Earlier in this [series](/blog/platform-engineering-pillars-2/), we introduced **service templates** as a way to scaffold consistent, ready-to-go services. In an **internal developer platform**, templates aren’t just for infrastructure, they’re the **golden paths** that define how developers start and succeed.

If 90% of new services are Go GRPC services, then a carefully crafted, opinionated go GRPC service blueprint will remove a lot of friction. It will give developers everything they need to begin delivering real business value immediately. A few select curated options of common starting points will help guide developers to generate projects complete with standardized structure, built-in quality checks, documentation, and clear guidelines for contribution.

A great service template provides:

### Project Bootstrapping

The template quickly scaffolds an entire service—including all necessary files and directories. Everything essential for your organization's standards should be included, from CI/CD configurations and dependency management to directory structures and environment-specific configuration files.

### Built-in Quality Tools

Templates embed guardrails that maintain consistency and high-quality standards across teams:

- **Linting rules and formatters**: Tools like ESLint, flake8, or Checkstyle that ensure code style and consistency across your codebase.
- **Testing frameworks**: Unit tests, integration tests, and contract testing tools set up and pre-configured (JUnit, pytest, Jest, Pact), helping teams maintain high quality right out of the gate.

### Documentation and Contribution Guides

Many platform teams overlook how clear, consistent documentation is crucial for initial and ongoing developer productivity. Every new service should arrive out-of-the-box with:

- **README**: Describing at a glance what the project does, why it exists, and how to run it.
- **Documentation**: Service template establishes a place for service-specific documentation that will be surfaced in the Service catalog. Markdown explanations, example input/output, and real-world use-cases.
- **Contribution guidelines and coding standards**: Clearly documenting the expectations, conventions, and standards every developer can follow with confidence.

Embedding this documentation into templates ensures that even brand-new services are discoverable, understandable, and maintainable—right from their first commit.

A great template means the service catalog becomes more than just an organizational listing. These thoughtfully designed templates can directly power it. Every new service entering your catalog aligns neatly with your organization's best practices in code quality, documentation, and process standards.

When paired with your **service catalog**, templates ensure every new service aligns with best practices—boosting **developer productivity** and **developer velocity** from day one.

## Streamlining Local Development to Reduce Friction

One of the fastest ways to improve **time to first commit** is to standardize local development workflows through your **internal developer platform**.

Your service templates provide the ideal mechanism for simplifying how quickly developers can get projects running locally. By embedding standardized local-development tooling into these templates, you ensure they're available consistently across your service catalog. Good templates typically contain:

- **A preconfigured, containerized environments:** Using Dev Containers, Docker Compose, or similar tools lets developers launch an environment that closely resembles production with minimal friction, completely avoiding dependency drift or local environment inconsistencies.  
- **Simple, standardized command runner:** Makefiles, just scripts, package.json scripts—whatever works as they're consistently documented and easy to run commands such as `make build`, `make test`, or `make lint`. Teams might diverge on preferred tooling over time; if so, simply record clearly in the project's readme (and thus in your service catalog) exactly what's needed.  
- **Built-in documentation:** Each service template includes clear instructions in a README outlining step-by-step processes for setup, running tests, and other everyday developer tasks.

With these pieces fully integrated into your catalog and templates, you significantly reduce friction and speed up development cycles, moving you meaningfully closer to improving your core developer-experience metrics.

The next critical area we need to address is how smoothly and quickly code moves from a local commit to a production release.

## CI/CD Integration: Fast, Reliable Pipelines for Experienced Developers

Experienced developers cite unreliable or slow pipelines as major productivity killers. Their frustrations often revolve around flaky builds, unreliable tests, and cumbersome environment setups. Slow or unpredictable pipelines break developer flow, causing frustration, delays, and lower productivity.

A strong **internal developer platform** integrates fast, stable, and predictable CI/CD processes:

- **Stable, Fast Feedback:**  
  Every new service comes pre-configured with build acceleration strategies like intelligent caching (Gradle, Bazel, Docker layers) and automatic parallel test execution. Stable and speedy pipelines help teams iterate quickly and confidently.

- **Ephemeral, Self-service Environments:**  
  Instead of battling shared staging environments – which get blocked by other teams— developers spin up short-lived testing environments directly from pull requests. Need to test your payment-service changes against the latest user-authentication service? Create a dedicated, temporary environment on-the-fly, validate interactions, then shut it down automatically when finished.

- **Test Reliability:**  
  Strictly enforce policies to quarantine flaky tests, quickly escalate notifications to responsible developers, and provide clear paths for fixing instabilities. Proactive flakiness management ensures credibility and reliability for test pipelines over time.

Reliable CI/CD pipelines protect developer focus, reduce cognitive load, maintain **developer velocity**, and prevent wasted time, increasing **developer productivity**.

{{% notes "There's Always More: Developer Experience Beyond What We Covered" %}}

Developer experience is a vast, nuanced topic, and there's much more a comprehensive platform can include than we've been able to explore fully here. Even just within your Service Catalog and developer workflows, valuable additions might include:

- **Onboarding Guides**: Step-by-step guides rapidly bringing new developers up to speed on teams, tools, and processes.
- **Frictionless Product Backlog Integration**: Quick access from codebases to the product backlog to connect code directly with the business context.
- **Code Coverage & Quality Dashboards**: Easy-to-use visualizations offering fast insights into quality metrics and test coverage.
- **Deprecation Notices & Change Management**: Automated notifications about changes, upcoming maintenance, or decommission plans to keep developers informed and prepared.
- **Pre-built Common Components**: Shared libraries and components solving everyday needs like logging, authentication, validation, and configuration.

And that's truly just scratching the surface. But remember: Platform engineering is an iterative journey, you don't need to tackle every single area all at once. If you start with friction logs and surveys to regularly identify and address pain points affecting daily workflows, you'll already be heading confidently in the right direction.

{{% /notes %}}

## Conclusion: IDPs as a DevEx Multiplier

A great **developer experience** is not optional—it’s a force multiplier for **developer productivity** and **developer velocity**. An **internal developer platform** with service catalogs, golden path templates, streamlined local dev, and integrated CI/CD removes friction at every step of the developer journey.

The result? Faster onboarding, quicker delivery, and happier teams.

With Pulumi, platform teams can automate consistent environments, implement golden paths, and enable self-service infrastructure that scales with your organization.

- [Organization Templates](/templates/) enables standardized service creation and consistent developer experiences
- [Stack References](/docs/concepts/stack/#stackreferences) for managing dependencies between environments and services
- [Pulumi Deployments](/docs/pulumi-cloud/deployments/) to streamline CI/CD workflows and enable self-service infrastructure
- [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks/) for creating ephemeral, on-demand testing environments
- [Automation API](/docs/iac/packages-and-automation/automation-api/) for programmatically managing infrastructure and implementing platform workflows

By prioritizing **developer experience** in your platform engineering strategy, you empower teams to move faster, build better, and maintain momentum—making your internal developer platform one of the most valuable assets in your organization.
