---
title: "What is Infrastructure as Code (IaC)?"
meta_desc: "Infrastructure as code (IaC) provisions cloud resources from machine-readable files. Learn how IaC works, declarative vs. imperative, top tools, and benefits."
meta_image: /images/what-is/what-is-infrastructure-as-code-meta.png
type: what-is
page_title: "What is Infrastructure as Code (IaC)?"
aliases:
  - /blog/five-years-of-infrastructure-as-code-part-one/
authors: ["zack-chase"]
---

**Infrastructure as code (IaC) is the practice of provisioning and managing computing infrastructure with machine-readable configuration files instead of clicking through a console or running one-off scripts.** You write code that describes the infrastructure you want, check it into Git, and let an IaC engine reconcile the real world with what you've declared.

IaC brings infrastructure into the same workflow that software engineers already use for application code: version control, code review, testing, and CI/CD. Modern platforms like [Pulumi](/) take it a step further by letting you write that code in TypeScript, JavaScript, Python, Go, C#, Java, or YAML rather than a custom configuration language.

In this article, we'll cover the key questions about infrastructure as code:

* Why is infrastructure as code important?
* How did infrastructure as code evolve?
* What is the difference between declarative and imperative IaC?
* What are the key elements of infrastructure as code?
* What benefits does infrastructure as code provide?
* What are common use cases for infrastructure as code?
* What are the most popular infrastructure as code tools?
* How do I get started with infrastructure as code?
* Frequently asked questions about IaC

## Why is infrastructure as code important?

IaC is important because of three trends, all of them happening at the same time.

### The transition to the cloud

The first is the ongoing transition from on-premises infrastructure to the cloud. The term "cloud" is broader than it first sounds — it includes:

* Hyperscaler clouds such as AWS, Microsoft Azure, and Google Cloud
* Regional clouds such as Alibaba Cloud or OVHcloud
* Specialized providers (DigitalOcean, Linode, Civo, etc.)
* Private cloud running in on-premises data centers (VMware vSphere, OpenStack, Nutanix)
* SaaS infrastructure companies such as Cloudflare, Snowflake, Confluent, Datadog, and New Relic
* Other cloud-managed assets like Auth0, GitHub, or GitLab

All of these are managed through APIs, which is what makes them addressable by IaC tools.

### Cloud modernization

The second trend is what most organizations do *after* they've moved to the cloud. They start adopting serverless, containers and Kubernetes, managed services, and ephemeral workloads in order to extract more value from the cloud and ship faster. Those modern architectures require fine-grained management of many small infrastructure primitives stitched together — exactly the workload IaC is built for.

### Frequent infrastructure changes

The third trend is the increasing rate of change. Teams that managed tens of resources changing every few months could get by with scripts and consoles. Teams now routinely manage thousands or tens of thousands of resources that change daily or hourly. At that scale, manual processes don't work; IaC is the only practical way to keep the system consistent.

## How did infrastructure as code evolve?

Infrastructure as code didn't emerge all at once. It's the latest step in a long arc of automation maturity, and the patterns that dominate today reflect lessons learned from earlier approaches.

### From manual clicks to declarative code

Most teams have moved through some or all of the following stages of automation as their infrastructure footprint has grown:

1. **Manual point-and-click in a UI console.** Quick to start with, but every recovery, scale-up, or environment clone repeats the same painful sequence of clicks.
1. **CLI commands or direct API calls.** Each UI step can be translated into a CLI invocation or HTTP request. Procedures become easier to document but remain step-based and brittle.
1. **Shell scripts.** Capturing those commands in a script is a real jump in repeatability. The downside is fragility: a failure halfway through a script often leaves infrastructure in an unknown state.
1. **SDK-driven code.** Using a cloud provider's SDK in a general-purpose language adds error handling, logging, and debugging, but the partial-failure and combinatorial-upgrade problems remain.
1. **Infrastructure as code.** Instead of describing the steps required to reach a desired state, you declare the state itself, and an engine figures out how to get there.

That last step is qualitatively different from everything before. Earlier tools described *how* to change infrastructure; IaC tools describe *what* the infrastructure should look like and let a deterministic engine handle the rest.

### From pets to cattle

In the early cloud era, each server was special: patched in place, mourned when it failed, and treated like a pet. Today, most infrastructure is managed as fleets of interchangeable resources that are replaced rather than upgraded, with cluster managers and serverless control planes handling scaling, fault tolerance, and traffic routing automatically. This is the well-known shift ["from pets to cattle"](https://www.engineyard.com/blog/pets-vs-cattle/), and it changed the kind of infrastructure IaC needed to manage.

### From configuration to provisioning

The second shift was what IaC was *for*. Earlier tools like CFEngine, Puppet, Chef, Ansible, and SaltStack targeted the "two VMs and a database" world, where the central problem was configuring and patching long-lived servers. Modern provisioning-oriented tools like [Pulumi](/) target a wider range of cloud resources (containers, serverless functions, managed databases, queues, networks, identity) and treat the creation, update, and replacement of those resources as the primary workflow.

### From a couple of VMs to thousands of resources

Older infrastructure was static and slow-moving. Modern systems routinely span dozens or hundreds of cloud resources (microservices, clusters, networks, security policies, secrets, load balancers, serverless functions, queues, data stores, hosted AI/ML services) across many environments. That growth in moving pieces is what makes IaC essential rather than optional.

## Declarative vs. imperative infrastructure as code

Most IaC tools fall into one of two camps: declarative or imperative.

**Declarative IaC** asks you to describe the end state you want. You say which resources should exist and how they should be configured, and a deployment engine works out the steps. It compares your declared state against what's actually running and then creates, updates, replaces, or deletes resources as needed. Pulumi, Terraform, OpenTofu, AWS CloudFormation, Azure Resource Manager (ARM and Bicep), and Google Cloud Deployment Manager all work this way.

**Imperative IaC** asks you to write the steps. Create this VM, attach that disk, open this port. The tool runs your steps in order but usually doesn't keep a model of what it built, so it can't easily detect drift or reconcile it. Shell scripts, cloud provider SDKs, and Ansible playbooks (when used procedurally) are typical examples.

| Aspect | Declarative IaC | Imperative IaC |
|--------|-----------------|----------------|
| You specify | The desired end state | The steps to reach the state |
| Drift handling | Engine reconciles automatically | Manual or re-run scripts |
| Idempotency | Built-in | Must be implemented by hand |
| Best for | Cloud resource lifecycle management | One-off automation, glue scripts |
| Examples | Pulumi, Terraform, CloudFormation, Bicep | Bash, cloud SDKs, Ansible playbooks |

Declarative is the more common style for cloud infrastructure because the lifecycle is messy. Changes happen constantly, deployments fail halfway through, multiple teams update the same resources, and drift creeps in. Solving those problems imperatively means writing a lot of bookkeeping code that the tool ought to handle for you. Pulumi is declarative under the hood but lets you write the declarations in a real programming language, so loops, conditionals, abstractions, and unit tests are all available without giving up the deterministic deployment engine.

## What are the key elements of infrastructure as code?

A real IaC practice depends on a few moving parts working together:

1. **An IaC engine.** A tool that translates IaC programs into cloud-API calls, computes plans, and reconciles state. Some are limited to a single cloud (AWS CloudFormation) and a fixed language (YAML or JSON); others, like [Pulumi](/), support multi-cloud and multiple general-purpose programming languages.
1. **Version control.** When infrastructure lives in code, every change is reviewable: who changed what, when, and why. Systems like GitHub, GitLab, or Bitbucket let you treat infrastructure changes with the same discipline as application changes.
1. **Tests.** As critical systems grow, untested changes get scary. With IaC you can write [unit, integration, and property tests](/docs/iac/guides/testing/) for your infrastructure and encode policies that block non-compliant changes.
1. **CI/CD pipelines.** Changes to IaC code can flow through the same CI/CD systems that build and deploy application code, with previews, gating tests, and automated rollback.
1. **Policy as code.** Security, compliance, and cost rules expressed as code that runs against every change. [Pulumi Policies](/docs/insights/policy/) blocks non-compliant configurations in CI before they reach production.
1. **Secrets and configuration.** Centrally managed, encrypted secrets and environment-specific configuration. [Pulumi ESC](/product/esc/) gives every application, CI job, and IaC program a single audited interface to pull from.

## What benefits does infrastructure as code provide?

IaC tames the complexity of cloud infrastructure by applying the same software-engineering principles that already work for application code:

* **Repeatability and consistency.** Stand up identical development, staging, and production environments from the same code, varying only configuration and sizing. Multi-region deployments become a loop, not a copy-paste exercise.
* **Accountability.** Every change is a commit. Version control answers "who changed what" without forensic effort.
* **Improved productivity.** When infrastructure is code, you get autocompletion, refactoring, jump-to-definition, and other IDE features. With Pulumi, you also get the full ecosystem of your chosen language: package managers, testing frameworks, linters, and existing libraries.
* **Faster recovery.** Re-provision an entire environment in another region or account from versioned code instead of rebuilding by hand.
* **Better cross-team alignment.** [DevOps](/what-is/what-is-devops/) and [platform engineering](/what-is/what-is-platform-engineering/) both rely on IaC as a common substrate. When infrastructure speaks the same language as the app, the teams responsible for them collaborate more naturally.

## What are common use cases for infrastructure as code?

IaC shows up across a lot of cloud workflows, but a few patterns account for most adoption:

1. **Provisioning cloud environments.** Stand up identical development, staging, and production environments from the same code, varying only config values and sizing. A fresh AWS or Azure account can go from empty to fully provisioned in minutes.
1. **Multi-cloud and hybrid setups.** Manage AWS, Azure, Google Cloud, on-premises VMware, and SaaS providers like Cloudflare, Snowflake, or Datadog through one workflow instead of juggling separate consoles.
1. **Kubernetes and container platforms.** Define a cluster alongside the workloads, ingress, IAM, and managed databases the app depends on, so the platform and the application ship as a single unit.
1. **CI/CD pipelines.** Infrastructure changes go through the same pull-request workflow as application code, with a preview step so reviewers can see what's about to change before it lands.
1. **Disaster recovery.** Re-provision a complete environment in a different region or account from versioned code, rather than rebuilding individual resources by hand.
1. **Policy and compliance.** Encode security, cost, and architectural rules as [policy as code](/docs/insights/policy/) and have every deployment checked against them automatically.
1. **Platform engineering.** Platform teams package vetted infrastructure patterns as reusable [components](/docs/iac/concepts/components/) that product teams consume through a standard interface.
1. **Ephemeral environments.** Spin up short-lived environments for pull-request previews, load tests, or customer demos, then tear them down when you're done.

## What are the most popular infrastructure as code tools?

The IaC tooling landscape has grown a lot since CFEngine kicked off the category back in 1993. The tools you're most likely to encounter today fall into a few clear categories.

| Tool | Language | Cloud coverage | License | Notes |
|---|---|---|---|---|
| **[Pulumi](/)** | TypeScript, JavaScript, Python, Go, C#, Java, YAML | 200+ providers, multi-cloud and SaaS | Apache 2.0 | Real programming languages on a declarative engine. |
| **Terraform** | HCL | Large multi-cloud ecosystem | BUSL 1.1 (source-available since 2023) | The category's incumbent. |
| **OpenTofu** | HCL | Same provider ecosystem as Terraform | MPL 2.0 | Linux Foundation-hosted fork of Terraform. |
| **AWS CloudFormation** | YAML, JSON | AWS only | AWS-managed | Native AWS, no multi-cloud. |
| **AWS CDK** | TypeScript, Python, Java, C#, Go | AWS (compiles to CloudFormation) | Apache 2.0 | Generates CloudFormation templates from code. |
| **Azure ARM / Bicep** | JSON / Bicep DSL | Azure only | Microsoft-managed | Bicep is the modern DSL that compiles to ARM JSON. |
| **Google Cloud Deployment Manager** | YAML, Python templates | Google Cloud only | Google-managed | Google Cloud's native option. |
| **Ansible** | YAML | Cross-platform (config-management oriented) | GPLv3 | Often used procedurally; Red Hat-owned. |
| **Chef, Puppet** | Ruby DSLs | Server configuration | Various | Earlier-generation configuration management. |

To see how Pulumi compares head-to-head, see [Pulumi vs. Terraform](/docs/iac/concepts/vs/terraform/), [Pulumi vs. CloudFormation](/docs/iac/concepts/vs/cloudformation/), [Pulumi vs. CDK](/docs/iac/concepts/vs/cloud-template-transpilers/), or the full [comparisons index](/docs/iac/concepts/vs/).

## How do I get started with infrastructure as code?

Most teams aren't starting from a blank slate. They have legacy services, hand-built environments, half-automated pipelines, and a backlog of incidents. Adopting IaC doesn't have to be a big-bang reorg — it works best as an incremental shift.

### Define "good"

Before evaluating tools, define what good infrastructure management looks like for your organization. Most teams converge on a similar set of assumptions:

* The amount of infrastructure is going to be high.
* The number of interconnections between managed services will be high.
* The rate of change should be high, to take maximum advantage of the cloud's elasticity.
* The number of people who have access to your cloud's capabilities should grow.
* Infrastructure code should be integrated into your continuous delivery system.

Get stakeholders from infrastructure, security, and application teams in a room to agree on these before picking a tool.

### Import existing infrastructure

You probably already have a lot of cloud resources that were created by clicking around or running scripts. The right IaC tool should let you [import existing infrastructure](/docs/iac/adopting-pulumi/) without tearing it down and rebuilding. Pulumi's [`pulumi import`](/docs/iac/adopting-pulumi/import/) can pull in individual resources, or import many resources at once from a JSON manifest.

### Integrate with existing engineering practices

Once your IaC code is in a Git repository, hook it into the same CI/CD system that runs your application tests. Add [infrastructure tests](/docs/iac/guides/testing/), policy checks, and a preview step so reviewers see exactly what's about to change.

### Think about policies and security

Layer in [policy as code](/docs/insights/policy/) so security and compliance rules are enforced automatically rather than reviewed manually. Aim for guardrails that are the default path, not gates that developers route around.

### Start small

Pick a single service or value stream, move it to IaC, measure the impact, and use what you learn as the template for the next one. A working slice of IaC for one team beats a half-finished platform across the whole org.

## Frequently asked questions about infrastructure as code

### What is infrastructure as code in simple terms?

It's the practice of describing your cloud setup — servers, networks, databases, IAM policies, secrets — in files that a tool can read and apply. You check those files into version control, and the tool keeps your real infrastructure in sync with what's described.

### What is the difference between infrastructure as code and configuration management?

IaC provisions and manages the lifecycle of cloud resources themselves: a VM, a Kubernetes cluster, a load balancer. [Configuration management](/what-is/what-is-configuration-management/) tools like Chef, Puppet, and Ansible were originally about configuring software *inside* servers that already existed. As more workloads have moved into immutable images and containers, most of that configuration work has shifted into the image build, leaving IaC as the primary discipline for runtime infrastructure.

### Is infrastructure as code the same as DevOps?

No. [DevOps](/what-is/what-is-devops/) is a broader culture and set of practices for delivering software; IaC is one of the technical practices that makes DevOps work. IaC specifically brings infrastructure into the same pull-request, code-review, and CI/CD workflows that developers already use for application code.

### What languages are used for infrastructure as code?

Most tools have their own. Terraform and OpenTofu use HCL, CloudFormation uses YAML or JSON, and Bicep is a DSL for Azure. Pulumi is the outlier in supporting general-purpose languages: TypeScript, JavaScript, Python, Go, C#, Java, or YAML.

### Which infrastructure as code tool should I use?

The right answer usually comes down to three things: what languages your team is comfortable in, which clouds you're targeting, and how much you care about testing and abstraction. Pulumi tends to be the best fit when you want general-purpose languages, multi-cloud support, and the ability to unit-test your infrastructure. Terraform and OpenTofu have the largest install base and a mature module ecosystem. CloudFormation, ARM/Bicep, and Deployment Manager make the most sense when you're committed to a single cloud and want the deepest native integration.

### Can I use infrastructure as code with my existing infrastructure?

Yes. Every major IaC tool supports importing resources that already exist, so you don't have to tear anything down and rebuild it. Pulumi's [`pulumi import`](/docs/iac/adopting-pulumi/import/) command can pull in individual resources, or import many resources at once from a JSON file that lists them.

### Is infrastructure as code only for the cloud?

No. IaC works against anything with an API, which includes public cloud (AWS, Azure, Google Cloud), private cloud (VMware vSphere, OpenStack), Kubernetes, and SaaS platforms like Cloudflare, Snowflake, Datadog, or GitHub.

### How does IaC handle secrets?

Good IaC tools encrypt secrets in state and let you pull them at runtime from a centralized store rather than embedding them in code or CI variables. Pulumi encrypts secrets in state with a key you control and integrates with [Pulumi ESC](/product/esc/) for cross-environment secret and configuration management.

### Is infrastructure as code mature enough for production?

Yes, and has been for years. Hyperscalers, financial-services firms, governments, and the largest SaaS platforms run their production cloud footprints on IaC tools. The category that started with CFEngine in the early 1990s is now the default way to manage cloud infrastructure at any meaningful scale.

### How does IaC relate to GitOps?

GitOps is an operational pattern in which Git is the source of truth for declared state and a controller continuously reconciles the cluster or cloud with that state. IaC is what produces those declarations in the first place. The two are complementary: most GitOps workflows are reconciling resources that IaC programs originally defined.

## Another look at infrastructure as code

Pulumi's YouTube series, A Quick Bite of Cloud Engineering, tackled the topic of infrastructure as code (IaC) in this video. Have a look.

{{< youtube "WhWf48kcEXU?rel=0" >}}

## Learn more

Pulumi offers a modern approach to IaC that lets you create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/iac/get-started/).

Related reading:

* [What is Pulumi?](/what-is/what-is-pulumi/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Infrastructure as Software?](/what-is/what-is-infrastructure-as-software/)
