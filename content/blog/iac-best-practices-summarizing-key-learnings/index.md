---
title: "IaC Best Practices: Summarizing Key Learnings"
feature_image: feature.png
date: 2024-04-08
updated: 2026-11-03
draft: false
meta_desc: Key IaC best practices from the Pulumi series, rechecked for 2026, covering stacks, ESC, components, policies, and guardrails for AI agents.
authors:
    - scott-lowe
tags:
    - best-practices
category: best-practices
series: iac-best-practices
aliases:
    - /blog/iac-recommended-practices-wrapping-up/
---

Welcome to the final post in our series of articles focused on infrastructure as code best practices. In this post, we'll wrap up our recommendations for [IaC with Pulumi](/product/infrastructure-as-code/), summarizing the best practices from previous posts as well as highlighting some areas of potential future growth for the team at Zephyr Archaeotech Emporium---the fictional company at the center of the story throughout this series.<!--more-->

{{% notes type="info" %}}
**Updated November 2026.** We rechecked each recommendation in this series against current Pulumi guidance. The main changes: Pulumi ESC is now the recommended way to share data between stacks in Pulumi Cloud, CrossGuard is now Pulumi Policies, components can be consumed from any Pulumi language, and there is a new section on applying these practices when AI agents make infrastructure changes.
{{% /notes %}}

## Recapping IaC Best Practices

As this series has progressed, we've been showing you how Zephyr's use of Pulumi has changed in response to how the organization, the team, and the application has changed. In case you haven't been following along---or in case you need a refresher---here's a brief summary of what's happened in the series:

* Zephyr started with a single project in a single repository with two stacks, one for production and one for testing. _(Details are available in [the first blog post](/blog/iac-best-practices-understanding-code-organization-stacks/) in the series.)_
* Zephyr quickly added per-developer stacks as a way to enhance developer productivity. _(You can read about per-developer stacks in [the second post](/blog/iac-best-practices-enabling-developer-stacks-git-branches/) in the series.)_
* As Zephyr continued to grow, their single Pulumi project grew into three different Pulumi projects: one for base infrastructure, one for their Kubernetes platform, and one for the online store application. _(The [third post in the series](/blog/iac-best-practices-structuring-pulumi-projects/) describes the reasoning for adopting multiple projects.)_
* Accompanying the switch to multiple projects, Zephyr implemented stack references (to pass information between stacks in different projects) and applied role-based access control (RBAC) to the stacks in Pulumi Cloud. _(Refer back to [the fourth post](/blog/iac-best-practices-applying-stack-references/) and [the fifth post](/blog/iac-best-practices-implementing-rbac-and-security/) in the series for more details on each of these areas.)_ Since this series was written, Pulumi ESC has become the recommended way to share data between stacks when you use Pulumi Cloud (more on that below). Stack references remain fully supported, and they are what to use with other state backends.
* Zephyr realized a need to split out their data layer, going from three projects to four projects, and along the way saw an opportunity to add a higher level of orchestration using the Pulumi Automation API. _(Refer back to [our sixth post](/blog/iac-best-practices-using-automation-api/) for more details on Zephyr's initial use of Automation API.)_

Since the last blog post, the Zephyr team has continued to explore [Automation API](/docs/iac/concepts/automation-api/), and has added an Automation API program that allows their developers to deploy the Zephyr online store directly from the associated GitHub repositories---developers don't even need to clone down the repositories first.

{{% notes type="info" %}}
To see the latest Automation API programs for Zephyr, refer to [the `zephyr-automation` GitHub repository](https://github.com/pulumi-zephyr/zephyr-automation).
{{% /notes %}}

## Areas of future growth for Zephyr

We've stated before that best practices are always point-in-time recommendations based on the requirements of the organization/team/individual using Pulumi. What this means, in practice, is that there is almost always room for growth and evolution. Organizations, teams, and individuals rarely remain static, and therefore their use of Pulumi is also unlikely to remain entirely static.

So, what are some potential areas of future growth for Zephyr?

* **Splitting the deployment of the microservices**: We alluded to this [in the previous post](/blog/iac-best-practices-using-automation-api/). Right now, all the microservices that comprise the online store are deployed together. What if one particular team needs to deploy only their service? The current approach can certainly accommodate that---Pulumi is declarative and will only change what needs to be changed---but what's better for the Zephyr team? Does Zephyr need to optimize for allowing service teams to move independently? Is it about reducing blast radius, so that undesired changes aren't introduced to another service? These are the sorts of considerations that drive this decision (and the third post in our series discusses [structuring Pulumi projects](/blog/iac-best-practices-structuring-pulumi-projects/) in more detail).
* **Using component resources**: Currently, the Zephyr team is using the standard API objects supplied by the Pulumi provider. For example, the various microservices for the Zephyr online store are defined using standard Kubernetes objects, like this:

    ```typescript
    const assetsNs = new k8s.core.v1.Namespace("assets-ns", {
        metadata: ...})

    const assetsService = new k8s.core.v1.Service("assets-service", {
        metadata: ...})

    const assetsDeployment = new k8s.apps.v1.Deployment("assets-deployment", {
        metadata: ...})
    ```

    [Component resources](/docs/iac/concepts/components/) would allow the Zephyr team to define a single logical resource that contains "child" resources. This would allow the Zephyr team to create a `Microservice` resource that incorporates the standard Kubernetes `Namespace`, `Deployment`, and `Service` objects. Deploying an instance of a `Microservice` resource deploys all the child objects defined in the component resource. This can simplify the Pulumi code through further use of [DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Components are also no longer tied to the language they are written in. Packaged as a Pulumi package and published to the [Private Registry](/docs/idp/concepts/private-registry/), a `Microservice` component written in TypeScript can be consumed from Python, Go, C#, Java, or YAML, which lets a platform team ship one vetted building block to every service team.
* **Making use of Pulumi Deployments**: Zephyr's CI/CD pipelines are not a topic we've discussed in the series. Given that Zephyr uses GitHub, they could use GitHub Actions (GHA); Pulumi has [an action for GHA workflows](https://github.com/pulumi/actions), and [`pulumi/auth-actions`](https://github.com/pulumi/auth-actions) exchanges the workflow's OIDC token for a short-lived Pulumi access token so no long-lived secret is stored. Zephyr could also use [Pulumi Deployments](/docs/deployments/), which provides git-driven deployments, drift detection and remediation, review stacks (per-PR stacks), scheduled operations, TTL-based cleanup, and [OIDC for dynamic cloud credentials](/docs/deployments/guides/oidc/). Deployments can also run from Automation API through a [remote workspace](/docs/iac/concepts/automation-api/), so Zephyr could extend their existing Automation API code to use it.
* **Addressing secrets and configuration management**: We've also not discussed how Zephyr could manage their secrets and configuration data. [Pulumi ESC](/product/secrets-management/) is a good option here. It integrates with AWS Secrets Manager, Azure Key Vault, Google Cloud Secret Manager, HashiCorp Vault, and 1Password, and it serves other [DevOps tools and use cases](/topics/platform-engineering/infrastructure-as-code-for-devops/) beyond Pulumi programs. ESC can also replace Zephyr's stack references: the [`pulumi-stacks` provider](/docs/esc/providers/iac/pulumi-stacks/) exposes one stack's outputs as configuration for another, which is more loosely coupled because the consuming program reads config instead of instantiating a `StackReference`. The [migration guide](/docs/esc/guides/pulumi-iac/migrate-from-stack-references/) walks through the change.

Even though it's working well, clearly there's a lot of room for the Zephyr team to continue to enhance and improve their infrastructure as code implementation!

## Summarizing best practices

Throughout the series, we've provided guidelines on how to best utilize Pulumi. While we recommend reading the entire series, in this section we "summarize our summaries" and provide some broad, overarching practices. We rechecked each one against current guidance.

1. With regard to Pulumi projects, **keep it as simple as possible, but no simpler.** [Current guidance](/docs/iac/guides/basics/organizing-projects-stacks/) describes a spectrum: start with a monolithic project and one stack per environment, move to layered stacks (networking, then clusters, then workloads) when a growing blast radius, divergent ownership, or slow deploys begin to hurt, and reserve micro-stacks for cases where you genuinely have many independent services. Layered stacks are the recommended default once a monolith becomes painful. Use multiple projects when necessary, but only when necessary.
1. **Use stacks freely.** Using multiple projects has a cost in complexity. Using multiple stacks, on the other hand, does not, so use them to model different environments, to provide per-developer test environments, to test changes before rolling them into production, or for any other use case where you need a separate, independent instance of the infrastructure defined in your Pulumi program. Each stack carries its own configuration, secrets, access controls, and policies.
1. **Focus on the requirements.** It can sometimes be too easy to focus on the technology instead of the requirements. There are a _lot_ of very cool things you can do with Pulumi, but try not to get distracted from the reason you're using infrastructure as code: repeatable, reliable, consistent deployments of your cloud infrastructure.
1. **Don't forget about security along the way.** Three pieces work together here. [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) (formerly CrossGuard) provides policy as code guardrails, with [pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) and enforcement levels from advisory to mandatory. Pulumi Cloud's [role-based access control](/docs/administration/concepts/rbac/) gives teams and tokens only the permissions they need, using built-in or custom roles. [Pulumi ESC](/docs/esc/) and OIDC keep long-lived credentials out of your code and pipelines.
1. **Test your infrastructure code.** Because Pulumi programs are written in general-purpose languages, you can apply [unit, property, and integration tests](/docs/iac/guides/testing/) the same way you test application code.

## Applying these practices with AI agents

AI agents now propose and make infrastructure changes alongside developers. The practices above matter more in that setting, because they define how much any one change, human or agent, can affect.

* **Permissions bound the blast radius.** [Pulumi Neo](/docs/ai/concepts/neo/permissions/) acts on behalf of the user who invokes it and can only do what that user could do. Role-based access control and stack boundaries therefore apply to agents with no extra setup. If Zephyr's developers can update only the application stack, Neo can update only the application stack.
* **Layered stacks keep changes small.** An agent asked to change the online store touches the `zephyr-app` project and leaves base infrastructure and the data layer alone. A monolithic project would put everything in scope of one run.
* **Per-developer and review stacks are safe sandboxes.** Let an agent iterate against a personal or per-PR stack, read the preview, and fix errors before anything reaches production. Preview output is the feedback loop that makes agent changes checkable.
* **Match approval to risk.** Neo's [task modes](/docs/ai/concepts/neo/tasks/) range from Review (approval before previews, updates, and pull requests) to Balanced (approval before updates) to Auto. Reasonable defaults are Auto or Balanced on developer stacks and Review on production.
* **Policies apply to everyone.** A mandatory Pulumi Policies rule blocks a noncompliant deployment whether a person or an agent proposed it, so write the guardrail once.
* **Give agents vetted building blocks.** Components from your Private Registry let agents compose approved patterns instead of inventing resource configurations. Record team conventions in Neo's [custom instructions](/docs/ai/concepts/neo/instructions/), including a per-repository `AGENTS.md`.

Other coding assistants can reach the same context through the Pulumi [MCP server](/docs/ai/guides/set-up-mcp-server/), which lets them list stacks, search resources, and check policy violations.

## Reviewing the code

The code reflects the 2024 series. It predates ESC-based stack sharing and the Pulumi Policies rename, so treat it as a reference for structure rather than a template for every current feature. You can view the code we've presented in this series in the following GitHub repositories:

* The ["zephyr-infra" repository](https://github.com/pulumi-zephyr/zephyr-infra) contains the base infrastructure definitions.
* The ["zephyr-k8s" repository](https://github.com/pulumi-zephyr/zephyr-k8s) contains the Pulumi code to stand up the Kubernetes cluster onto which Zephyr deploys their online store application.
* The ["zephyr-data" repository](https://github.com/pulumi-zephyr/zephyr-data) manages Zephyr's "data layer" for persistent data used by the online store application.
* The ["zephyr-app" repository](https://github.com/pulumi-zephyr/zephyr-app) is Zephyr's online store. This repository has both the application code as well as the Pulumi code for deploying the application (see the "infra" directory).
* In the ["zephyr-automation" repository](https://github.com/pulumi-zephyr/zephyr-automation) you'll find Automation API programs used by Zephyr to orchestrate deployments of the different projects involved in supporting the online store.

In each of these repositories, there are different branches that reflect the state of the code as of a particular blog post. The "main" branch reflects the final state of the code, as described in this wrap-up post.

## Wrapping up

This series has used the story of a fictional company, Zephyr Archaeotech Emporium, to discuss some recommendations around how to best utilize Pulumi for solving their infrastructure as code needs. While this company is fictional, the benefits of Pulumi and infrastructure as code are real. We invite you to try for yourself---[install Pulumi](/docs/install/) and sign up for [a free Pulumi Cloud account](https://app.pulumi.com/signup) today!

{{< related-posts >}}
