---
title_tag: "Pulumi Cloud: What is it?"
meta_desc: Learn how Pulumi Cloud relates to the open source Pulumi infrastructure as code tool.
title: "What is it?"
h1: "What is Pulumi Cloud, and how does it relate to Pulumi's open source IaC tool?"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    cloud:
        name: "What is it?"
        parent: pulumi-cloud-get-started
        weight: 1
        identifier: pulumi-cloud-what-is-it
---

So you've chosen to use Pulumi infrastructure as code, and are now deciding how to manage your state and whether Pulumi Cloud is a good fit? Or you've heard Pulumi is open source but aren't entirely clear on what part is fully open and free, and what is a paid Pulumi product? This page will give you a better understanding about the answers to these questions and everything in between.

## In Summary

Pulumi Cloud is a managed service that helps teams adopt collaborative, secure, and robust cloud engineering practices. This includes infrastructure as code, secrets management, and continuous enforcement of cloud policies. Pulumi's flagship infrastructure as code tool is [open source](https://github.com/pulumi) and is how many community members initially learn about Pulumi. The two are related in that Pulumi IaC uses Pulumi Cloud by default to make adopting IaC in your team easier, secure, and reliable out-of-the-box and automatically.

Pulumi IaC can be used with a so-called "DIY" backend if you prefer, which comes with some tradeoffs outlined below. From an adoption perspective, Pulumi Cloud is the most popular way to use Pulumi, especially within a team -- so if you choose it, you're in good company.

{{% notes "info" %}}
An analogy to other software you may be familiar with is that, just like Git is fully open source and you can host, secure, and manage repositories yourself, so too can you with hosting your Pulumi infrastructure as code projects and stacks. It is much easier, especially in a team, however, to use Git in conjunction with GitHub, as it features easy security, reliability, and collaboration, as well as powerful features like Pull Requests. A similar dynamic exists with Pulumi and Pulumi Cloud.
{{% /notes %}}

Pulumi Cloud is a platform of three products: [Pulumi IaC](/product/infrastructure-as-code), the companion to Pulumi open source IaC; [Pulumi ESC](/product/secrets-management), a secrets and configuration solution; and [Pulumi Insights](/product/pulumi-insights), an intelligent cloud inventory, compliance, and management product. Pulumi Cloud is offered as a service (SaaS) as well as a self-hosted edition that you can run anywhere. It features a novel client/server architecture to increase your confidence in using the SaaS.

## Five Key Areas

There are five key areas where Pulumi Cloud adds value beyond what is available in the Pulumi IaC open source software:

* **Instant Collaboration**: provides a common place where developers, security experts, and infrastructure practitioners meet to automate, secure, and manage cloud infrastructure
* **Automatic Security**: ensures security best practices are built-in from the outset
* **Robustness, Performance, and Scalability**: automatically ensures reliability and scalability as your cloud needs grow, minimizing outages and the need to rearchitect your system over time
* **Governance and Extensibility**: guarantees that teammates are following your established practices early and always, with full visibility
* **Cost Effectiveness**: the lowest total cost to maximize return on your cloud investments

Let's examine each of these areas in more detail.

### 1/ Instant Collaboration

The first thing you will notice with Pulumi Cloud is that all of your [projects, stacks, and resources](/docs/pulumi-cloud/projects-and-stacks/) are easy to see, search, and explore. A complete history is always available, of who has changed what, when, and how, with full resource change diffs, and links to both the source changes that triggered a deployment, as well as forward links to the resources in your cloud consoles.

All actions taken by teammates on Pulumi Cloud are logged for [full auditability](/docs/pulumi-cloud/admin/audit-logs/). Full deployment logs are also captured and easy to review to facilitate debugging failures. This is particularly useful for automated deployments, as is common with the [Pulumi Automation API](/automation) and [Pulumi Kubernetes Operator](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/). All deployment history for all time is maintained and organized.

It is easy to get new teammates onto Pulumi Cloud, especially when [using SAML/SSO](/docs/pulumi-cloud/access-management/saml/) which automates onboarding, offboarding, and role assignment. From there, you can see the identity of teammates who are making infrastructure changes, and delegate responsibilities to them.

Pulumi Cloud integrates with [over a dozen CI/CD systems](/docs/iac/using-pulumi/continuous-delivery/), such as GitHub Actions, GitLab Pipelines, Jenkins, etc., and has [a built-in deployment service](/docs/pulumi-cloud/deployments/) for easy Git-based deployments. The result is that configuring delivery pipelines with Pulumi Cloud is flexible so that if you want to collaborate with teammates using standard Git-driven code flows, like pull requests, code reviews, and branch-driven deployments, you can do so. The Pulumi GitHub App will put previews of your deployments right into the pull request comments, making reviews seamless.

Pulumi's projects and stacks model facilitates collaboration especially thanks to the IaC tool's configuration model, but Pulumi Cloud goes beyond this by offering Pulumi ESC, a way to group configuration and secrets that frequently change together into composable and versioned environments. This enables Don't Repeat Yourself (DRY) practices that help to secure access to cloud accounts, share sensitive information, and deliberately roll out changes across multiple related projects and stacks.

Pulumi Cloud also offers short-lived stacks in the form of [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks/) -- ephemeral environments stood up just for the duration of a Pull Request, making verification of changes much more robust and seamless -- as well as [Time-to-Live (TTL) Stacks](/docs/pulumi-cloud/deployments/ttl/), which ensure that temporary stacks get automatically cleaned up, enabling more productive engineering workflows without the risk of cloud waste.

[Pulumi Copilot](/docs/pulumi-cloud/copilot/), an AI assistant built into Pulumi Cloud, collaborates with you to solve a variety of challenges you might encounter. That includes assisting you in debugging cloud deployment failures, helping you to write infrastructure as code, and even asking more general questions like "What versions of Kubernetes am I running?", "What is my most expensive, least used resources?", "Who is my most productive teammate?", and more. Pulumi Copilot is even integrated with the Pulumi CLI as well as the Pulumi VSCode Extension so that you can get AI assistance with your local developer experience.

### 2/ Automatic Security

Pulumi Cloud has [a rich identity model](/docs/pulumi-cloud/access-management/) that integrates with your security identity provider of choice, whether that is Azure Active Directory, Google Workspace, Okta, or any SAML/SSO provider, to regulate all access to your cloud assets.

If you manage your IaC state with a DIY approach, you will need to come up with a scheme that works for your organization. It often looks simple at the outset -- perhaps you can just use AWS IAM for the S3 bucket that stores your state -- but large-scale teams rarely want to grant full access to all engineers. In fact, this may be the difference between passing and failing a compliance audit.

Pulumi Cloud has [a rich RBAC model](/docs/pulumi-cloud/access-management/teams/) that integrates with its projects and stacks; most teams on DIY backends eventually realize they need to build and maintain such a system themselves. Additionally, Pulumi Cloud enables you to [generate short- and long-lived tokens](/docs/pulumi-cloud/access-management/access-tokens/), optionally with fine-grained permissions, for automation scenarios. This includes easy auditing and revocation of those tokens.

Pulumi IaC has [a secrets model](/docs/iac/concepts/secrets/) built in which helps to ensure that sensitive information never ends up in a state file in plaintext. This model is limited with DIY backends because you need to leverage less-secure passphrases, or resort to manually managing encryption keys and devising a scheme for creating and managing new ones. If you use Pulumi Cloud, a secure approach is used by default to ensure each organization and stack is encrypted securely. All communications between client and server are also encrypted for an extra layer of security.

To see an example of what can happen in the real world when improperly managing DIY state, see this [Sysdig blog post](https://sysdig.com/blog/cloud-breach-terraform-data-theft/): it describes how an attacker was able to find a statefile (for Terraform but the same would apply for Pulumi) which contained a secret AWS key that they could use to escalation privileges and take over the entire AWS account. If using Pulumi Cloud, this is stopped by construction for multiple reasons: 1) secrets are encrypted, 2) state files themselves are stored encrypted at rest, and 3) most importantly, state files are not stored in easily accessible locations in S3.

### 3/ Robustness, Performance, and Scalability

Pulumi is most robust, performant, and reliable when leveraging Pulumi Cloud as its backend. This is because with a DIY backend like AWS S3, the protocol is limited to blob storage and there is a fundamental limit to how effective this protocol can become. The Pulumi Cloud interface, on the other hand, is a rich REST API that is more transactional in nature. This not only means more robust deployments and failure recovery, but also that fewer bytes need to be sent across the wire compared to the way Pulumi checkpoints its state for DIY backends, improving performance, and ultimately leading to a better experience overall.

Due to the fragile nature of the blob store protocol, teams often need to manually edit DIY-managed state files, because the blob store protocol cannot recover from failures as seamlessly as Pulumi Cloud’s transactional protocol. This means teams on DIY state backends often have to build supporting solutions to backup and recover state.

Managing state files by hand in a DIY backend can also cause outages if not handled properly. For example, [Spotify described at KubeCon](https://www.youtube.com/watch?v=ix0Tw8uinWs) how they accidentally deleted nearly all of their production Kubernetes clusters due to a simple merge mistake, when managing the equivalent of Pulumi DIY state files in Terraform. This is an easy mistake with DIY backends, but Pulumi Cloud avoids it entirely by construction because the Pulumi Cloud service carefully handles concurrency, serialization, and safety.

Pulumi Cloud itself features [a secure, scalable, fault-tolerant, highly-available global architecture](https://www.pulumi.com/security/pulumi-cloud-security-whitepaper.pdf). This results in a level of robustness and scalability that is difficult to replicate when building a custom DIY backend. Numerous organizations use Pulumi Cloud with thousands of end users, hundreds of thousands of stacks, and millions of updates. BMW's scalable and resilient cloud, for example, was built using Pulumi and supports over 11,000 developers ([read more here]).

### 4/ Governance and Extensibility

Pulumi Cloud makes it easier to ensure your team uses the cloud as intended, thanks to policies and enforcement mechanisms not present in DIY backends.

Pulumi Cloud offers organization-wide policies thanks to Pulumi's policy as code engine, [Pulumi CrossGuard](/crossguard/), allowing you to enforce policies for security, compliance, cost, team practices, and more. This works over your IaC resources -- to block violations from ever getting deployed -- as well as it does to find and fix existing violations in your cloud accounts, no matter how they were provisioned thanks to Pulumi Insights. You can even auto-remediate violations, such as automatically tagging all AWS resources with certain configurable metadata.

Pulumi Cloud lets you set up [private templates](/docs/pulumi-cloud/developer-portals/templates/) for your organization which allows end users to spin up infrastructure following patterns you have designated for your team, within an [interactive Internal Developer Platform (IDP) experience](/docs/pulumi-cloud/developer-portals/new-project-wizard/). This, in combination with [Pulumi Components](/docs/iac/concepts/resources/components/), can help ensure you are adopting best practices at scale. Many infrastructure teams review their templates and components with their security counterparts to agree on safe patterns they'll use throughout the organization.

Pulumi Cloud's [drift detection capabilities](/docs/pulumi-cloud/deployments/drift/) can uncover situations where a manual edit to a cloud resource was made outside of your infrastructure as code specifications, with automatic remediation. Left unchecked, these drift issues can cause surprises, outages, and security incidents.

Although Pulumi Cloud has numerous workflows out-of-the-box, many teams need custom workflows or integrations, whether for governance or otherwise. For this, all of Pulumi Cloud exposes a [fully documented, programmable REST API](/docs/pulumi-cloud/reference/cloud-rest-api/) that teams can use to extend the system. Additionally, [webhooks can be configured](/docs/pulumi-cloud/webhooks/) for many event types to trigger custom event-driven workflows such as Slack integrations and more in response to deployments, resource updates, policy violations, and more.

Pulumi Cloud is an AWS Advanced Partner, implements many compliance specifications and best practices, and undergoes annual SOC 2 Type II audits. For custom DIY backends, you would need to consider these yourself, whereas with Pulumi Cloud, you get this out of the box.

### 5/ Cost Effectiveness

Using Pulumi Cloud, you automatically gain all of the above benefits. This means more time to focus on solving your business challenges, versus undifferentiated DIY heavy lifting.

We have found that teams who use DIY backends require at least one full time engineer for every 10 end users in their team just to manage the DIY backend and build systems, and to ensure it is secure and scalable. They also have to maintain costly onboarding and training programs for using their custom DIY backend. Certain Pulumi capabilities can be exceedingly costly to replicate, like search, Copilot, fault tolerance, and the various identity integrations like RBAC. And even with all of that, DIY capabilities typically fall far short of what Pulumi Cloud delivers out of the box (for instance, lacking the full history of who changed what and when).

To learn more about the hidden costs of going it on your own with a DIY backend, read [this blog post](/blog/hidden-costs-of-infrastructure-management/). To learn more from a team of cloud wizards that ultimately decided to retire their DIY backend in favor of Pulumi Cloud, read [the Starburst case study](/case-studies/starburst/).

Perhaps the best feature of Pulumi Cloud is that "it just works" so you can get up and running quickly on an architecture you know will work today with minimal setup and forever into the future.

## Next Steps: Try It Out For Free

Pulumi Cloud is the easiest way to adopt Pulumi's open source IaC tool at scale, securely, reliably, and collaboratively.

That said, DIY backends are fully supported, and this article aims to help you make an informed decision about which option best suits your use case. The [state and backends topic](/docs/iac/concepts/state-and-backends/) describes in-depth how Pulumi IaC uses Pulumi Cloud and DIY backends and other architectural considerations.

A complete list of Pulumi Cloud's features and capabilities is available [on the pricing page](/pricing#compare). For more details about adopting Pulumi Cloud in your team, [see the onboarding guide](/docs/pulumi-cloud/get-started/onboarding-guide). This guide also includes best practices to help you completely adopt the full platform.

To get started today, [sign up for a free Pulumi Cloud account](https://app.pulumi.com/signup). Pulumi Cloud is free for individuals and small teams, and has advanced capabilities for larger teams and enterprises.
