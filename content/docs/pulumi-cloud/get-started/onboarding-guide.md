---
title: Setting Up Pulumi for Your Organization
meta_desc: Learn how to onboard your entire team to Pulumi, and build out your infrastructure
  platform, with built-in security, best practices, and compliance.
menu:
  cloud:
    name: Onboarding guide
    parent: pulumi-cloud-get-started
    weight: 2
    identifier: pulumi-onboarding-guide
search:
  keywords:
    - organization
    - setting
    - onboard
    - platform
    - entire
    - practices
    - team
---

In this guide, you’ll find everything you need to know about using Pulumi within your organization, from setting things up to recommended usage patterns and practices.

## In this guide

* Setup and start using Pulumi Cloud, whether SaaS or self-hosted
* Set and achieve onboarding goals for your team’s first 30 days to three months
* Understand and adopt recommended practices for Pulumi’s suite of products
* Work through (and prepare for) common first-time user challenges

{{% notes type="tip" %}}
**Pro tips**

* To help everyone quickly adopt Pulumi in your organization, identify a group of “Pulumi champions” across your organization who will encourage other team members to get started right away. The faster your team uses Pulumi, the faster you can ship.
* Check out the [Pulumi Glossary](/docs/iac/concepts/glossary/) for specific terms we use across our sites and documentation.
{{% /notes %}}

## Part one: Setting up Pulumi Cloud

Setting up your Pulumi Cloud account will lay the foundation for onboarding your team and enabling collaboration. We’ll walk through the basics of getting your teams ready to build.

### Choosing SaaS versus self-hosted

Pulumi Cloud is available in two flavors: 1\) a multi-tenanted, secure, and compliant software-as-a-service (SaaS), and 2\) a self-hosted edition. These are referred to as simply Pulumi Cloud and Self-Hosted Pulumi Cloud, respectively.

The easiest option is to choose SaaS, as things like high availability, disaster recovery, geo-replication, and more are available out of the box. It is secure and compliant and its unique architecture allows you precise control over security, as described in the [Pulumi Cloud Security Whitepaper](https://www.pulumi.com/security/pulumi-cloud-security-whitepaper.pdf). To choose this option, simply log into [pulumi.com](http://pulumi.com).

For companies who require more control over the Pulumi Cloud hosting environment, such as would be the case for air-gapped or other highly regulated environments like FedRAMP, the self-hosted edition can be hosted anywhere: on-premises, in your cloud account, on a virtual machine, in a Kubernetes cluster, and so on. Learn more about [self-hosting Pulumi Cloud here](https://www.pulumi.com/product/self-hosted/).

### Signing up for an account

Every user of Pulumi Cloud has an account. As you get started, you will sign up with either an email address and password, or use your GitHub, GitLab, or Atlassian identity. After signing up, you will have the ability to configure a SAML/SSO identity provider for subsequent onboarding of your teammates, if you so desire. Learn more about [Pulumi Cloud accounts here](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/) and, to sign up, go to [app.pulumi.com/signup](http://app.pulumi.com/signup).

### Getting familiar with the management console

As soon as you are up and running, you will want to familiarize yourself with the Pulumi Cloud console. The console is accessible via the “Sign In” link in the upper right corner of [pulumi.com](http://pulumi.com) or by going to [app.pulumi.com](http://app.pulumi.com) directly. You’ll land on a Dashboard with useful content and links and the left navigation bar features product-specific tabs as well as Settings. From the console, you can manage your teams, see your stacks and resources, search for resources, and more. Your personal account is accessible from your avatar in the upper right corner and there is also a sparkle icon in the lower right corner which opens Pulumi Copilot, a smart AI assistant.

## Part two: Managing your teams

Pulumi Cloud makes it easy to collaborate on your cloud projects faster and with more confidence. Typically the infrastructure platform group will own the configuration of Pulumi and onboarding developers and security experts to facilitate building secure cloud applications and infrastructure. The onboarding process begins with configuring your organization.

### Organizing people for collaboration

Your Pulumi Cloud hierarchy is made up of individual **users**, **organizations**, and **teams**. Each plays a critical role in how your team collaborates and enforces security and best practices.

You will begin by creating an organization. An organization is first and foremost a collection of individual user members. It is a container for IaC projects and stacks, ESC projects and environments, and Insights accounts and discovered resources. Most companies only need a single organization, although it is possible to have multiple if you need extra separation or multiple identity providers. Learn more about [organizations here](https://www.pulumi.com/docs/pulumi-cloud/admin/organizations/).

An organization can also contain teams. A team is a group of individual users that typically reflects your company’s structure or working groups. By grouping members into teams, you can control which projects, stacks, and environments they have access to, and with what permissions, through role-based-access-control (RBAC). We know that teams and roles change frequently, so Pulumi Cloud makes it easy to reconfigure teams as needed, or even have them automatically sync with your identity provider of choice. Learn more about [teams here](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/).

Start by creating [your organization here](https://app.pulumi.com/?create-organization=1). Organizations and their capabilities are a paid feature of Pulumi Cloud, so you will notice that creating an organization starts a free trial. Pulumi has a generous free tier when the trial expires and you can always [contact us](https://pulumi.com/contact) if you need more time.

### Configuring Single Sign-On (SSO)

Many organizations prefer to use Single Sign-On (SSO) to leverage an identity provider such as Microsoft Entra ID, Google Workspace, Okta, or any other SAML 2.0 compliant provider. To learn about configuring SSO for your organization, [read Pulumi Cloud SAML(SSO)](https://www.pulumi.com/docs/pulumi-cloud/access-management/saml/). If you’d like to continue using email, GitHub, GitLab, or Atlassian identity, you can skip this step.

### Inviting your teammates

As soon as you’ve completed these set up steps, you are ready to invite your team\! If you have SSO with System for Cross-domain Identity Management (SCIM) enabled, onboarding and offboarding happen automatically. Otherwise, refer to [Inviting members to an organization](https://www.pulumi.com/docs/pulumi-cloud/admin/organizations/#inviting-members-to-an-organization).

## Part three: Building securely

Before getting started creating projects and shipping to the cloud, you will want to make some key decisions, starting with security. Security is a team effort and it is best to ensure it from the outset. Pulumi Cloud makes it easy to adopt security best practices as part of team onboarding.

### Staying in compliance

Modern enterprises have rigorous compliance requirements. Pulumi Cloud is SOC 2 Type II certified and has been reviewed by AWS for compliance with its best practices. The infrastructure hosting Pulumi Cloud is designed and managed in alignment with IT security standards, including SOC 1/SSAE 16/ISAE 3402, SOC 2, SOC 3, FISMA, FedRAMP, DOD SRG Levels 2 and 4, PCI DSS Level 1, EU Model Clauses, ISO 9001 / ISO 27001 / ISO 27017 / ISO 27018, ITAR, IRAP, FIPS 140-2, MLPS Level 3, and MTCS. Learn more at [Pulumi Security](https://www.pulumi.com/security/).

Pulumi’s Policy as Code engine, CrossGuard, enables teams to enforce compliant infrastructure practices. Pulumi CrossGuard includes hundreds of out-of-the-box policies for AWS, Azure, Google Cloud, and Kubernetes, spanning PCI DSS, ISO 27001, SOC 2, HITRUST, and CIS Benchmarks. You can also write custom policies that are unique to your industry or enterprise requirements.

Pulumi CrossGuard finds issues with existing cloud infrastructure as well as gating attempts to introduce new problems. It can be configured at various warning and error levels, and flexibly applied to projects differently – e.g., GDPR rules might only apply to infrastructure in European regions. CrossGuardPaC also features automatic remediations. Learn more about [Pulumi CrossGuard here](https://www.pulumi.com/security/).

Pulumi Cloud also keeps an audit log of every activity and who performed it. Read more about [Pulumi Cloud audit logs here](https://www.pulumi.com/docs/pulumi-cloud/admin/audit-logs/).

### Setting up cloud access methods

Pulumi supports hundreds of cloud providers, but most organizations will end up using at least AWS, Azure, Google Cloud, and/or Kubernetes. Other supported providers include SaaS infrastructure products, such as Cloudflare, DataDog, MongoDB, and Snowflake, as well as on-premises technologies such as VMWare vSphere. For a complete list of Pulumi providers, check out the [Pulumi Registry](https://pulumi.com/registry). The registry is your one-stop shop for provider documentation, including how to configure access to each of the clouds, as well as resource APIs.

Although each cloud offers flexible authentication unique to that cloud, Pulumi ESC offers rich OpenID Connect (OIDC) support for several popular providers, ensuring dynamic, short-lived credentials. This technique is the most secure and should be preferred for those providers that have support. Learn more about [dynamic login credentials here](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/).

In the event your chosen cloud doesn’t have a Pulumi ESC OIDC provider, refer to the registry documentation. Each provider has an “Install & config” section on the left-hand navigation. See [AWS Installation & Configuration](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/) as an example. Pulumi generally uses native tools and techniques for authenticating so it is idiomatic and consistent with your other usage patterns.

## Part four: Structuring your projects

Pulumi’s project model is intentionally flexible to support many different architectures and working styles. This flexibility, however, does mean that you will need to make some decisions up front about how to structure your projects. Many teams figure this out and adjust as they go but it is helpful to have a discussion and general direction in mind from the outset.

### Deciding on your architecture

Both Pulumi IaC and Pulumi ESC have a notion of **project**. A project is an abstract concept that defines a collection of related configurations. Pulumi IaC projects then have any number of **stacks**, each of which is an instance of that project. Similarly Pulumi ESC projects have any number of **environments**, each defining a group of related secrets and configuration.

To use an analogy, an IaC project is like a Git repo, and a stack is like a Git branch. And just like Git repos and branches, the way teams can decide to structure them can vary greatly. Some teams prefer monolithic Git repos that contain many different parts of the codebase, while other teams prefer smaller, more single-purpose Git repos.

For the most part, it is better to prefer smaller, purpose built projects. This makes securing and deploying them independently easier, but it does come at the expense of some complexity as then your architecture is made up of many interdependent stacks.

As a concrete example, your team might have the following IaC projects:

* Security layer defining IAM roles, KMS keys, etc.
* Networking base layer defining VPCs, subnets, etc.
* Multiple Kubernetes clusters defined and configured differently
* Multiple database projects, e.g. a data lake, several MySQL infrastructures, etc.
* Dozens of application projects, some containerized, some on VMs, some serverless

These projects can depend upon one another; for instance, the Kubernetes project almost certainly needs VPC and subnet IDs exported from the lower networking base layer.

For IaC stacks, we may have some shared stacks across all of these projects:

* Production us-west, us-east, and Europe
* Staging in fewer regions
* Many development stacks, perhaps even one per developer on your team

Each of our IaC projects has their own set of stacks, despite them clearly sharing a logical grouping, so we may then want ESC environments representing each logical grouping.

Learn more about Pulumi IaC [projects](https://www.pulumi.com/docs/iac/concepts/projects/) and [stacks](https://www.pulumi.com/docs/iac/concepts/stacks/), and check out the [Organizing Pulumi projects & stacks](https://www.pulumi.com/docs/iac/packages-and-automation/organizing-projects-stacks/) guide for much more detailed guidance on how to choose to structure your projects. Learn more about Pulumi ESC [projects and environments here](https://www.pulumi.com/docs/esc/environments/).

### Deciding on a language strategy

Pulumi IaC’s main strength compared to competitive IaC technologies is its inherent polyglot nature. It supports the Top 5 languages according to GitHub, including Python, Go, any Node.js language (JavaScript, TypeScript, etc), any .NET language (C\#, F\#, etc), and any JVM language (Java, Groovy, Scala, Clojure, etc). Pulumi even supports YAML for simple use cases. Pulumi’s language support is not just limited to the languages themselves, but rather, the entire ecosystem around those languages. To learn more about Pulumi’s support for these languages, see [Pulumi Languages & SDKs](https://www.pulumi.com/docs/iac/languages-sdks/).

As part of adopting Pulumi in your organization, you will want to decide your language strategy. Broadly speaking there are two options: 1\) single-language or 2\) multi-language.

For most teams getting started, single-language is the way to go. This makes it easier to standardize on tools, patterns, and practices, and to train your team on them. The choice of language is usually dictated by whatever language your team already uses – this is the beauty of Pulumi’s IaC approach, as you can leverage whatever existing standards you’ve adopted.

In large organizations, however, multi-language is often the eventual outcome, even if teams begin with single-language. The risk of this approach is fragmentation between different teams who use different languages. To address this risk, Pulumi offers many consistent experiences for managing all of your projects, regardless of their language of choice. Pulumi Cloud works consistently regardless of language, in addition to Pulumi CrossGuard policies.

Pulumi Packages provide a way to author packages in one language and consume them in another. This enables, for instance, a central infrastructure platform team to write shared components in Go, and then have other engineers in the organization consume them from their own native language, such as Python and/or Java. For even simpler use cases, perhaps they will get consumed with a dozen lines of YAML. Learn more about [Pulumi packages here](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/).

### Creating and executing a migration strategy

If you have existing cloud infrastructure you are trying to bring into Pulumi IaC, there are a number of strategies you can take. One option is to simply throw it away and begin anew. This ensures you can adopt all best practices from the outset without worrying about technical debt. This option is clearly not always practical, however, for existing business critical services.

Pulumi has tools to import any cloud infrastructure no matter how it was created, even by manually pointing and clicking in your cloud console. Pulumi also offers tailored migration tools for Terraform, AWS CloudFormation/CDK, Azure ARM, and Kubernetes YAML. All of these tools will not only generate the Pulumi IaC code in your language of choice, but also actively place the management of existing resources under Pulumi IaC. This effectively swaps out the management of these resources without perturbing them so you experience zero downtime. Finally, Pulumi has professional services offerings where we will help you with the migration.

In addition to migration tools, Pulumi supports coexisting with many existing ecosystems. For instance, you may deploy Helm charts as-is, or consume Terraform workspace outputs. This enables you to migrate pieces incrementally and over time, when the value for doing so is right.

To learn more about creating and executing your migration strategy, plus coexistence, check out the [Pulumi Migration Hub](https://www.pulumi.com/migrate/) or [detailed migration tooling documentation](https://www.pulumi.com/docs/iac/adopting-pulumi/).

## Part five: Ensuring best practices

After deciding on your project architecture, structure, and language choices, you will want to ensure you adopt best practices. Pulumi’s use of general purpose languages makes it easy to encode your team’s best practices and ensure that they stay consistent as you scale.

### Testing your IaC

IaC is code and as such it should be tested. This will yield more predictable deployments, increase confidence, and minimize the chance of costly mistakes. Because Pulumi just uses industry standard languages, you benefit from entire ecosystems of test tools and techniques.

There are three primary ways to test your IaC. First, **unit tests** test targeted functionality without needing to actually deploy cloud infrastructure. These are part of the inner loop and are fast to run. Pulumi makes it easy to mock certain cloud capabilities to facilitate this sort of testing. Next, **Policy as Code**, mentioned earlier, is actually a form of testing, and can block deployments that do not comply with predetermined policies. Finally, **integration tests** coordinate with actual Pulumi deployments to test that real infrastructure is provisioned to specification.

It is possible to build more sophisticated test strategies atop this foundation. For instance, you could fuzz test that your infrastructure configurations react to varying inputs correctly. This might even entail chaos testing by destroying bits of infrastructure and testing how the system responds. To learn more about these capabilities, [see the Testing Pulumi programs guide](https://www.pulumi.com/docs/iac/concepts/testing/).

Beyond these testing techniques, you can also consider using linters and static analysis tools to enforce industry standards as well as your own team’s coding guidelines.

### Sharing and reusing with components and templates

Pulumi projects, stacks, and environments help to reduce “sprawl”: that is, the typical copy-and-paste of configurations that legacy IaC tools lead to. Sprawl is bad in that it causes unintended drift between environments, and can lead to outages and security mistakes.

Pulumi offers two additional facilities for ensuring consistency and best practices in your team.

First, **components** are IaC resources that you define to abstract and encapsulate the usage of one or more other resources. For instance, an AWS Virtual Private Cloud (VPC) might consist of dozens of resources: public and private subnets, Internet and NAT Gateways, the VPC itself, and more. Rather than open coding the VPC definition in every project that needs one – something that can be hundreds or even thousands of lines of code – you can use a component. It turns out the Pulumi component package [AWSX](https://www.pulumi.com/registry/packages/awsx/) offers such a VPC component out of the box, but your organization can create your own components. This just requires subclassing the component resource base class.

Components enjoy all of the benefits of native language packages, such as the ability to store them in package managers, version them, ensure secure dependencies, and so on. [Read more about component resources here](https://www.pulumi.com/docs/iac/concepts/resources/components).

By default, component resources are single-language, which is often fine. For organizations that require multi-language usage, however, components can be made multi-language as noted earlier. The [Pulumi Packages](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/) guide describes how.

Next, **templates** are blueprints that help scaffold entirely new projects. Although a component often encapsulates a cloud resource usage pattern, templates are standard “starting points” for entire projects that typically consist of many resources. [Pulumi Templates](https://pulumi.com/templates), for instance, are available for many common architectures and patterns, but you can create your own. You can also register your own organization’s templates so they’re easily available in the Pulumi Cloud New Project Wizard. Learn more about [building your own templates here](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/).

## Part six: Working together

With Pulumi, your entire team can collaborate and ship cloud applications and infrastructure faster with guardrails that ensure security, compliance, and best practices. The Pulumi CLI enables on-demand action, however, most teams will want to put in place automation, especially for production environments. Many teams will also want to enable developer self-service.

### Deploying continuously

Although most teams will get started by running the Pulumi CLI and performing activities in the Pulumi Cloud console manually, at some stage they will want to automate certain workflows.

The most common workflow is deploying changes to your IaC configurations. The Pulumi CLI can be used to preview and deploy changes. But most teams will prefer to trigger deployments using a Git-based workflow using one of Pulumi’s many continuous integration and deployment (CI/CD) integrations. This approach generally delivers previews in your pull requests, facilitating code reviews and testing, and then performs updates upon merging. Once your organization is comfortable with this basic CI/CD workflow, Pulumi recommends adding drift detection to your stacks on a scheduled basis. (We’ll show you how to do this later on.)

Commonly, a team’s “official” stacks, like staging and production, will use a CI/CD-based approach while individual developers still work on development stacks manually. Many teams already use CI/CD for application delivery and adopting it for infrastructure delivery helps to unify practices.

If you are using GitHub, installing the Pulumi GitHub App will deliver instantaneous support for basic GitOps workflows including deployment previews in your pull requests. [Learn more here](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/github-app/).

The steps to accomplishing complete CI/CD entail first choosing your platform. [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/) is a purpose built delivery model for IaC deployments and built into Pulumi Cloud – we recommend using it as your first choice. The [Pulumi Kubernetes Operator](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/) lets you trigger deployments from within your Kubernetes clusters. Alternatively, you can choose an existing CI/CD solution such as GitHub Actions, GitLab CI, Octopus Deploy, or one of many others. See the [full list of integrations here](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/). Next, you’ll need to define your branching strategy, such as whether main maps to production, or if you’ll have a dedicated branch you merge into for production releases. After that you’ll configure your pipelines, including any testing strategies, and define your workflows. Read more about [Infrastructure CI/CD here](https://www.pulumi.com/solutions/infrastructure-ci-cd/).

To automate your Pulumi activities, you’ll need a Pulumi Cloud access token. These tokens can be generated with various permissions and scopes. Beyond personal tokens, Pulumi also supports team and organization tokens which you’ll want to use for CI/CD. [Learn more here](https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/).

### Guarding against drift

Drift is when a change happens outside of your IaC pipeline, causing a conflict between your last known deployment in IaC and the reality of your cloud resources’ current state. This could have been because of a manual change someone made in your cloud account but forgot to reconcile, for instance. Drift can be very problematic as it can cause security mistakes and/or outages the next time you deploy. Pulumi supports [detecting and remediating drift](https://www.pulumi.com/docs/pulumi-cloud/deployments/drift).

### Accomplishing productive developer experiences

As mentioned earlier, it’s common to give developers their own stacks for development and testing purposes. This is often as simple as literally standing up an entire dedicated stack for each developer who is working on a particular project. Pulumi’s projects and stacks model makes this easy and it can lead to very fast and productive developer experiences.

If some infrastructure is heavyweight or costly, however, it may be impractical for every developer to have an entire copy of your environment. In such cases, Pulumi’s flexible projects model makes it possible to factor out shared infrastructure. For instance, each developer may have their own instance of a containerized application and some of its related services, but ultimately share access to databases and clusters. [This article shows off](https://www.pulumi.com/blog/iac-recommended-practices-using-stack-references/) how we might use Pulumi stack references to facilitate factoring our projects in this way.

Another common pattern is to create short-lived **review stacks** for every proposed change in a pull request. The idea here is that an independent stack can be spun up for each pull request so that the changes can be fully tested end to end. As soon as the pull request is closed, the stack will be torn down so there is no long-term cost. [Learn more about review stacks here](https://www.pulumi.com/docs/pulumi-cloud/deployments/review-stacks/).

**Time-to-live (TTL) stacks** are another helpful feature to ensure you don’t build up cloud waste as a result of letting engineers spin up their own environments. Each TTL stack is given a timeframe that, once exceeded, results in the stack being automatically destroyed. This can increase your confidence in letting developers have their own stacks. [Learn more here](https://www.pulumi.com/docs/pulumi-cloud/deployments/ttl/).

### Enabling developer self-service

In many platform engineering organizations, we want to enable application and backend developers to self-serve their own infrastructure needs. For example, we may want developers to be able to create a functional, production-like environment themselves whenever they’re bringing up a new application, rather than filing a ticket and waiting. Of course, we don’t want to give developers *all* of the keys to the cloud kingdom, as we need to ensure infrastructure remains secure, compliant, and cost effective. Pulumi’s platform enables self-service with guardrails.

The first decision to make is how your developers will interface with the infrastructure. There are broadly three models to choose from.

First is having developers interface with Pulumi IaC directly. In this model, your platform team will give developers direct access to Pulumi. Most likely you’ll use separate teams so that developers have different RBAC settings than the infrastructure team. Capabilities like components, templates, and policies help to enforce the necessary guardrails, while also giving developers simpler starting points. Most developers aren’t experts in VPCs, Kubernetes clusters, and so on – and don’t want to be\! – so these tools can help them get started easily.

In this model, your choice of single- versus multi-language will also play a role in how you architect the components and templates your developers will use.

The second model is to give developers a simpler YAML interface where they can just check in YAML files to a Git repository and have the CI/CD pipeline take care of the rest. This model is enabled much like the first, in that you will write components, templates, and policies, with the difference that you will want very simplistic interfaces conducive to YAML usage. [Learn more about Pulumi YAML here](https://www.pulumi.com/docs/iac/languages-sdks/yaml/).

The final model to choose from is giving developers a UI-based experience for provisioning infrastructure environments. Rather than using code, or even YAML, developers will log into a portal and click a button to spin up or update infrastructure. Pulumi offers a variety of techniques for this use case, ranging from just using Pulumi’s organization templates and New Project Wizard directly, to Pulumi’s Backstage plugin, to hand rolling your own UI portal that is powered by Pulumi’s Automation API. Learn more about [building developer portals with Pulumi here](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/).

## Part seven: Integrating with and extending Pulumi

Pulumi was built with extensibility in mind. Our philosophy is one of “building blocks”: every service we provide is powered by an API that you are able to access for your own custom workflows and systems requirements. We understand that modern enterprise environments are complex and ever evolving, and we want to ensure Pulumi scales to meet those needs.

### Extending Pulumi with custom workflows

There are three primary ways to extend Pulumi with custom workflows.

The first is that the entire **Pulumi Cloud REST API** is well-documented, powerful, and easy to use. These are the very APIs that power the CLI and cloud console experiences. [Learn more about the Pulumi Cloud REST API in the documentation here](https://www.pulumi.com/docs/pulumi-cloud/reference/cloud-rest-api).

Next up is the **Pulumi Automation API**. This capability allows you to embed IaC capabilities into any piece of software, enabling custom tools, self-serve portals, complex deployment orchestrations, and even entire SaaS products that themselves need to provision or integrate with cloud resources. [Learn more about the Automation API here](https://www.pulumi.com/docs/pulumi-cloud/reference/cloud-rest-api).

Finally, **Pulumi Cloud Webhooks** allow you to tap into any lifecycle events in the Pulumi Cloud to invoke a custom REST API endpoint that you control. Using these you can react with your own custom workflows including doing things like posting to Slack channels, triggering test runs after a deployment completes, and more. [Learn more about Pulumi Cloud Webhooks here](https://www.pulumi.com/docs/pulumi-cloud/webhooks/).

### Writing your own IaC providers

Pulumi has support for hundreds of providers out of the box. But what if it is missing one that you need? There are a few options.

Pulumi’s **provider model** is extensible and you can implement your own providers. These providers can manage new or internal systems where neither a Terraform nor Pulumi provider exists. Creating a Pulumi provider entails creating resource schemas for the resource types and properties the provider will expose, as well as create, read, update, delete (CRUD) operations for those resources. This can be considerable work but it’s the most robust approach for providers that are important to you. [Learn how to author and publish your own providers here](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/authoring/).

Pulumi can also bridge **any Terraform provider** in the ecosystem at development time so that it can be used from any Pulumi IaC program without needing to write a provider by hand. If a provider already exists in Terraform, it can be consumed from Pulumi IaC. [Learn more here](https://www.pulumi.com/blog/any-terraform-provider/).

Pulumi also supports **dynamic providers** or providers built “on the fly” with very simple logic. This lets you write CRUD logic right inline in your Pulumi IaC program without needing to author, build, and package an entirely separate provider. [Learn more about dynamic providers here.](https://www.pulumi.com/docs/iac/concepts/resources/dynamic-providers/)

### Contributing to open source

The entirety of Pulumi’s SDK is open source under the Apache 2.0 license, available under the [Pulumi GitHub organization](https://github.com/pulumi). There are over 500 repositories and the entire Pulumi team is responsive and loves to collaborate in the open. If you would like to contribute, please read [the Contributing to Pulumi guide](https://github.com/pulumi/pulumi/blob/master/CONTRIBUTING.md) – pull requests are always welcome\!

## Part eight: Driving and measuring success

We work with many teams adopting Pulumi for their mission critical cloud projects. As such, we’ve learned from and put together some best practices to keep in mind when driving and measuring your organization’s success.

### Start with a beachhead win

Getting a new cloud platform off the ground isn’t easy. It’s difficult to balance ambitious goals with the reality of moving an entire organization to a new way of building. This is particularly challenging if your team has existing technical debt to migrate or rebuild in the transition.

You should set a goal of getting your first 1-3 workloads into production as soon as possible. For most organizations, this will take 3-6 months. This “beachhead” win does three things: First, it keeps you grounded in reality, so that you don’t go too dark for too long, which will add considerable risk to your project. Second, it lays the groundwork for onboarding many more workloads in the future while improving your platform in parallel. And third, it gives you tangible accomplishments you can showcase to your management, the business, and to broader teams you aim to adopt your platform. There is always a little bit of an element of marketing here.

These workloads should be automated with CI/CD pipelines and generally use as many of the best practices in this document as possible, even though at this stage you’ll be uncomfortably early on your journey to figuring out things like which components and templates to build.

### Stay focused on impact

This initial beachhead win will inform where you go from here. Rather than starting out by creating dozens of abstractly-useful and broad components, it is better to take a “workload-first” strategy, and inform very specific component requirements from real world applications.

We also recommend resisting the temptation to conflate redesigning your projects to use new cloud architectures with the migration to your platform. This adds risk. Sometimes this is inevitable, especially if the shift to a platform coincides with a major initiative like moving from on-prem to the cloud, but avoid it if you can. If possible, get workloads onto Pulumi and your platform first. From there, it is easier to refactor and redesign projects in place.

### Treat your platform like a product

An internal cloud platform is a product – and, as such, calls for superb end user developer experiences. Although self-service is a primary goal of our platforms, in our experience, self-service is a journey. You should start by getting your platform well-architected as outlined in this guide, and then crawl, walk, and run: Begin by documenting your components and templates, instituting an internal open source strategy so developers can find and collaborate on the code and then you can evolve and building it into a more comprehensive platform over time.

### Don’t kick the security can down the road

It’s easy to defer security and compliance initiatives like using Pulumi IaC’s Policy as Code features or short-lived cloud credentials as is possible with Pulumi ESC and OIDC. Use this moment of change as an excuse to build these into your platform from day one. Pulumi was designed to make security the default, not an afterthought. Teams that take shortcuts and build up technical debt in this area almost always deal with costly implications down the road.

### Measure your success

Put in place clear success metrics from the outset. Common metrics we see Pulumi customers improving dramatically include “Time from checking in code until it ships to production.” Related, the DevOps Research and Assessments (DORA) metric of deployment frequency and related metrics are useful industry standard measurements. It’s common to see improvements of 5-10X in these areas for Pulumi customers. Another metric is how long it takes for a developer to get a new cloud environment to work with, and by adopting some of the self-serve techniques in this guide, many Pulumi customers are able to reduce this from months to minutes.

## Part nine: Getting support

We aspire to make Pulumi as easy to use as possible, and hope that this guide helps you navigate your way around the Pulumi ecosystem. That said, we are here to help with anything you need, whether it’s advice on your architecture, help using a particular cloud resource, training for your team, or anything in between.

### Learning your way around examples

One of the most challenging aspects of any IaC solution, Pulumi included, is learning how to configure the cloud resources you desire to use. Between 100s of clouds, and 100s or 1,000s of services in each of them, and dozens of configuration settings per service, there are endless ways to configure them. Pulumi supports containerized workloads in the cloud as well as serverless and on-premises VM-based workloads. This is very powerful–but can be daunting!

The Pulumi AI assistant was created to help you write IaC. You can describe any cloud architecture in natural language and it will create the code in your chosen programming language. It is getting better and more accurate over time. [Try out Pulumi AI here](https://pulumi.com/ai).

The Pulumi Registry contains detailed documentation for every provider Pulumi supports. For instance, [this page](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/#example-usage) shows numerous ways to configure AWS S3 Buckets. Most resources in the registry will have examples showing common ways to configure them.

The Pulumi examples repo on GitHub contains hundreds of complex examples covering common use cases. These go beyond individual single resource examples to entire cloud architectures. [Check out the examples repo here](https://github.com/pulumi/examples).

### Talking to us on GitHub

Being open source at our core, we are always engaging with our community on GitHub. If you find an issue, please [file it on GitHub](https://github.com/pulumi/pulumi/issues) and we will get back to you right away. If you have a more open ended question, please feel free to use [our GitHub Discussions page](https://github.com/pulumi/pulumi/discussions).

### Connecting with the Pulumi community

Pulumi’s community has grown to hundreds of thousands of practitioners worldwide. We are proud that this is a warm and welcoming community, where you will find many folks eager to help out. There are many avenues for engaging with the Pulumi community.

[Pulumi’s Community Slack](https://slack.pulumi.com) is a vibrant place to ask questions and engage with your peers. The Pulumi team also hangs out there along with tens of thousands of practitioners.

There are now many Pulumi User Groups (PUGs) now exist worldwide, including US-based locations (e.g., Austin, Boston, Chicago, Columbus, Dallas, Denver, New York, Philadelphia, San Diego, San Francisco, Seattle) as well as international (e.g., Auckland, Berlin, London, Munich, Oslo, Prague, São Paulo, Sydney, Tel Aviv). These are organized by local Pulumi champions and are growing by the day. [Join one of the PUGs now](https://www.meetup.com/pro/pugs/).

[Read this guide](https://www.pulumi.com/community/) for a more comprehensive overview of ways to engage with the community.

### Training and learning

In addition to the above ways to connect with the community, Pulumi regularly hosts free events and workshops. These are great ways to go deep on specific topics, whether they are cloud-specific ones, or Pulumi best practices. [See a list of upcoming events here](https://www.pulumi.com/resources/#upcoming) – as well as many that are available for on-demand watching.

For Pulumi Enterprise and Business Critical customers, we offer custom tailored onboarding and ongoing training for your team on whatever topic is important at a given time.

[The Pulumi Tutorials](https://www.pulumi.com/tutorials/) guide offers comprehensive self-guided tutorials on how to use Pulumi, all the way from fundamentals, to sharing and reuse best practices, to how to use specific AWS or Azure resources, and much more.

### Using premium support plans

Pulumi Enterprise and Business Critical customers have the option of purchasing 12x5 or 24x7 support. This support comes with ticketing, guaranteed SLAs, product roadmap reviews, prioritized bugs and feature requests, private Slack channels, and more. Organizations with support plans also have dedicated account managers and architects who are ready to roll up their sleeves and help with any problem you may encounter. If you are on a support plan, you can [file a ticket or view the current system status on the support page here](https://support.pulumi.com/hc/en-us).

### Understanding your usage and billing

Pulumi offers two methods of purchasing: Billed in arrears, monthly, on a credit card, and paid upfront with invoicing. Invoiced purchases benefit from commitment pricing which delivers considerable savings. If you’re on a monthly plan and would like to explore commitment pricing, [Contact Us](https://www.pulumi.com/contact/).

Pulumi Cloud gives you detailed insights into your usage and billing on the Billing & usage page on your organization’s settings left-hand navigation. This includes IaC resources, deployment minutes, ESC secrets, and more. There you will be able to see and/or download a full history of usage. Only organization administrators and designated billing administrators are able to access these pages. [Learn more about how to designate billing administrators here](https://www.pulumi.com/docs/pulumi-cloud/access-management/billing-managers/).

Your organization and billing administrators will also receive a monthly usage report over email.

### Taking advantage of Pulumi Professional Services

If you need more hands-on services, the Pulumi Professional Services team offers deep engineering engagements to help ensure you succeed using Pulumi. In many cases, that will mean helping to design and implement many of the practices called out in this guide. It could also entail building custom providers, components, or policies, migrating existing cloud infrastructure to Pulumi, and more. We offer standard packages but are happy to customize and tailor an approach that works for you. [Learn more about Pulumi Professional Services here](https://www.pulumi.com/proserv/).
