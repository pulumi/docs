---
title: "Iac Recommended Practices: Wrapping Up"
date: 2024-03-11
draft: false
meta_desc: This wraps up the series on IaC recommended practices, summarizing the previous posts and pointing out areas of future growth for the Zephyr team.
meta_image: meta.png
authors:
    - scott-lowe
tags:
    - best-practices
    - zephyr
---

Welcome to the final post in our series of articles focused on infrastructure as code (IaC) recommended practices. In this post, we'll wrap up our recommendations for IaC with Pulumi, summarizing the recommendations from previous posts as well as highlighting some areas of potential future growth for the team at Zephyr Archaeotech Emporium---the fictional company at the center of the story throughout this series.<!--more-->

For ease of navigation, here are links to all the blog posts in the series:

* [IaC Recommended Practices: Code Organization and Stacks](/blog/iac-recommended-practices-code-organization-and-stacks/)
* [IaC Recommended Practices: Developer Stacks and Git Branches](/blog/iac-recommended-practices-developer-stacks-git-branches/)
* [IaC Recommended Practices: Structuring Pulumi Projects](/blog/iac-recommended-practices-structuring-pulumi-projects/)
* [IaC Recommended Practices: Using Stack References](/blog/iac-recommended-practices-using-stack-references/)
* [IaC Recommended Practices: RBAC and Security](/blog/iac-recommended-practices-rbac-and-security/)
* [IaC Recommended Practices: Using Automation API](/blog/iac-recommended-practices-using-automation-api/)
* **IaC Recommended Practices: Wrapping Up** (this post)

## Recapping infrastructure as code with Pulumi at Zephyr

As this series has progressed, we've been showing you how Zephyr's use of Pulumi has changed in response to how the organization, the team, and the application has changed. In case you haven't been following along---or in case you need a refresher---here's a brief summary of what's happened in the series:

* Zephyr started with a single project in a single repository with two stacks, one for production and one for testing. _(Details are available in [the first blog post](/blog/iac-recommended-practices-code-organization-and-stacks/) in the series.)_
* Zephyr quickly added per-developer stacks as a way to enhance developer productivity. _(You can read about per-developer stacks in [the second post](/blog/iac-recommended-practices-developer-stacks-git-branches/) in the series.)_
* As Zephyr continued to grow, their single Pulumi project grew into three different Pulumi projects: one for base infrastructure, one for their Kubernetes platform, and one for the online store application. _(The [third post in the series](/blog/iac-recommended-practices-structuring-pulumi-projects/) describes the reasoning for adopting multiple projects.)_
* Accompanying the switch to multiple projects, Zephyr implemented stack references (to pass information between stacks in different projects) and applied role-based access control (RBAC) to the stacks in Pulumi Cloud. _(Refer back to [the fourth post](/blog/iac-recommended-practices-using-stack-references/) and [the fifth post](/blog/iac-recommended-practices-rbac-and-security/) in the series for more details on each of these areas.)_
* Zephyr realized a need to split out their data layer, going from three projects to four projects, and along the way saw an opportunity to add a higher level of orchestration using the Pulumi Automation API. _(Refer back to [our sixth post](/blog/iac-recommended-practices-using-automation-api/) for more details on Zephyr's initial use of Automation API.)_

Since the last blog post, the Zephyr team has continued to explore [Automation API](/docs/using-pulumi/automation-api/), and has added an Automation API program that allows their developers to deploy the Zephyr online store directly from the associated GitHub repositories---developers don't even need to clone down the repositories first.

{{% notes type="info" %}}
To see the latest Automation API programs for Zephyr, refer to [the `zephyr-automation` GitHub repository](https://github.com/pulumi-zephyr/zephyr-automation).
{{% /notes %}}

## Areas of future growth for Zephyr

We've stated before that recommended practices (or even "best practices," if you prefer that term) are always point-in-time recommendations based on the requirements of the organization/team/individual using Pulumi. What this means, in practice, is that there is almost always room for growth and evolution. Organizations, teams, and individuals rarely remain static, and therefore their use of Pulumi is also unlikely to remain entirely static.

So, what are some potential areas of future growth for Zephyr?

* **Splitting the deployment of the microservices**: We alluded to this [in the previous post](/blog/iac-recommended-practices-using-automation-api/). Right now, all the microservices that comprise the online store are deployed together. What if one particular team needs to deploy only their service? The current approach can certainly accommodate that---Pulumi is declarative and will only change what needs to be changed---but what's better for the Zephyr team? Does Zephyr need to optimize for allowing service teams to move independently? Is it about reducing blast radius, so that undesired changes aren't introduced to another service? These are the sorts of considerations that drive this decision (and the third post in our series [discusses structuring your projects](/blog/iac-recommended-practices-structuring-pulumi-projects/) in more detail).
* **Using component resources**: Currently, the Zephyr team is using the standard API objects supplied by the Pulumi provider. For example, the various microservices for the Zephyr online store are defined using standard Kubernetes objects, like this:

    ```typescript
    const assetsNs = new k8s.core.v1.Namespace("assets-ns", {
        metadata: ...})

    const assetsService = new k8s.core.v1.Service("assets-service", {
        metadata: ...})

    const assetsDeployment = new k8s.apps.v1.Deployment("assets-deployment", {
        metadata: ...})
    ```

    [Component resources](/docs/concepts/resources/components/) would allow the Zephyr team to define a single logical resource that contains "child" resources. This would allow the Zephyr team to create a `Microservice` resource that incorporates the standard Kubernetes `Namespace`, `Deployment`, and `Service` objects. Deploying an instance of a `Microservice` resource deploys all the child objects defined in the component resource. This can simplify the Pulumi code through further use of [DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
* **Making use of Pulumi Deployments**: Zephyr's CI/CD pipelines are not a topic we've discussed in the series. Given that Zephyr uses GitHub, they could use GitHub Actions (GHA); Pulumi has [an action for GHA workflows](https://github.com/pulumi/actions). Zephyr could also use [Pulumi Deployments](/product/pulumi-deployments/), which offers an extensive set of features---OIDC support for dynamic credentials, Review Stacks (per-PR stacks), support for GitHub Enterprise, and GitOps-style workflows, to name a few. Support for Pulumi Deployments is also baked into Automation API, meaning that Zephyr could extend their existing Automation API code to incorporate Pulumi Deployments.
* **Addressing secrets and configuration management**: We've also not discussed how Zephyr could manage their secrets and configuration data. [Pulumi ESC](/product/esc/) is a good option here, offering seamless integration with Pulumi for infrastructure as code while also supporting a variety of other DevOps tools and use cases (here's [one example](/blog/esc-env-run-aws/)).

Even though it's working well, clearly there's a lot of room for the Zephyr team to continue to enhance and improve their infrastructure as code implementation!

## Summarizing our recommendations

Throughout the series, we've provided recommendations on how to best utilize Pulumi. While we recommend reading the entire series, in this section will "summarize our summaries" and provide some broad, overarching recommendations.

1. With regard to Pulumi projects, **keep it as simple as possible, but no simpler.** While tools like Automation API can help with orchestrating multiple projects, it remains true that in most cases a single project is simpler. Use multiple projects when necessary, but only when necessary.
2. **Use stacks freely.** Using multiple projects has a cost in complexity. Using multiple stacks, on the other hand, does not---so use them freely to model different environments, to provide per-developer test environments, to test changes before rolling them into production, or for any other use case where you need a separate, independent instance of the infrastructure defined in your Pulumi program.
3. **Focus on the requirements.** It can sometimes be too easy to focus on the technology instead of the requirements. There are a _lot_ of very cool things you can do with Pulumi, but try not to get distracted from the reason you're using infrastructure as code: repeatable, reliable, consistent deployments of your cloud infrastructure.
4. **Don't forget about security along the way.** Make sure you are properly securing your infrastructure. Pulumi [CrossGuard](/crossguard) can help here by providing "policy as code" guardrails for cloud infrastructure. Pulumi Cloud's RBAC functionality helps with ensuring the right users have the right permissions to the right sets of cloud infrastructure resources.

## Reviewing the code

You can view the code we've presented in this series in the following GitHub repositories:

* The ["zephyr-infra" repository](https://github.com/pulumi-zephyr/zephyr-infra) contains the base infrastructure definitions.
* The ["zephyr-k8s" repository](https://github.com/pulumi-zephyr/zephyr-k8s) contains the Pulumi code to stand up the Kubernetes cluster onto which Zephyr deploys their online store application.
* The ["zephyr-data" repository](https://github.com/pulumi-zephyr/zephyr-data) manages Zephyr's "data layer" for persistent data used by the online store application.
* The ["zephyr-app" repository](https://github.com/pulumi-zephyr/zephyr-app) is Zephyr's online store. This repository has both the application code as well as the Pulumi code for deploying the application (see the "infra" directory).
* In the ["zephyr-automation" repository](https://github.com/pulumi-zephyr/zephyr-automation) you'll find Automation API programs used by Zephr to orchestrate deployments of the different projects involved in supporting the online store.

In each of these repositories, there are different branches that reflect the state of the code as of a particular blog post. The "main" branch reflects the final state of the code, as described in this wrap-up post.

## Wrapping up

This series has used the story of a fictional company, Zephyr Archaeotech Emporium, to discuss some recommendations around how to best utilize Pulumi for solving their infrastructure as code needs. While this company is fictional, the benefits of Pulumi and infrastructure as code are real. We invite you to try for yourself---sign up for [a free Pulumi Cloud account](https://app.pulumi.com/) today!
