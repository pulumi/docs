---
title: What is Infrastructure as Code?
meta_desc: |
    Understand what is infrastructure as code, along with the main benefits and importance for modern application development.
type: what-is
page_title: "What is Infrastructure as Code?"
---

Infrastructure as code (IaC) is an approach to automating the provisioning and management of infrastructure. At its heart, **infrastructure as code is about bringing software engineering principles, approaches, and tools into the cloud infrastructure space.**

Before infrastructure as code, infrastructure was (and in some cases still is!) provisioned in a variety of ways, such as by pointing and clicking in a user interface (UI), by running commands via a command-line interface (CLI), by running batch scripts, or by using configuration management tools that may not have been designed with cloud infrastructure in mind. Each of these methods falls short in some way; interactive methods involving a UI or a CLI often create problems with repeatability and consistency while batch scripts or configuration management tools may be unable to declaratively manage infrastructure. Today, modern approaches use platforms, such as [Pulumi](/), which embrace and support the full software engineering lifecycle.

In this article, we'll touch on four key questions regarding infrastructure as code:

* Why is infrastructure as code important?
* What are the key elements of infrastructure as code?
* What benefits does infrastructure as code provide?
* How do you get started with infrastructure as code?

Let's start with examing why infrastructure as code is important.

## Why is infrastructure as code important?

IaC is important because of three significant trends, all of them happening at the same time.

### The transition to the cloud

One trend, of course, is the ongoing transition to the cloud. More and more companies are shifting workloads from on-premises infrastructure to cloud environments.

It's worth mentioning the scope of this transition. The term "cloud environments" is more far-reaching than many may realize. Hyperscaler clouds like AWS or Microsoft Azure may be the first to come to mind, but there is so much more to cloud infrastructure:

* Regional clouds, like Alibaba Cloud
* Specialized cloud providers
* Private cloud technologies running in on-premises data centers, such as VMware vSphere
* Modern SaaS infrastructure companies such as Cloudflare, Snowflake, Confluent, Datadog, New Relic, and many others
* Other cloud-based assets like Auth0, GitLab, or GitHub

All these cloud environments can be provisioned or managed via APIs, and, as a result, can be managed with infrastructure as code tools.

### Cloud modernization

The second trend is cloud modernization. At first glance this may seem redundant with the first trend, which is the ongoing transition to the cloud. However, after organizations transition to the cloud, they tend to look for opportunities to maximize the value they get from their cloud environment. This frequently involves adopting technologies such as serverless, containers and Kubernetes. In some cases, cloud modernization involves using managed services to offload some of the heavy lifting to the cloud provider. In other cases, cloud modernization means more use of ephemeral, stateless workloads that exist only for a short while, and then need to be decommissioned. When applied correctly, all these approaches enable teams to deliver value more quickly. These technologies and services generally require a more granular management of infrastructure. Stitching together all the primitives that the cloud provider offers into solutions that serve the business is a great fit for IaC.

### Frequent infrastructure changes

Finally, the rate of change for a company's infrastructure is increasing. Part of this increase in the rate of change is due to cloud adoption and cloud modernization. There is a third reason, though: organizations are finding that they can move faster if they take advantage of the fundamental elasticity of the cloud.

For teams managing tens or hundreds of cloud resources that change once every few months, managing infrastructure using scripts or via interactive means (such as using a UI or a CLI) might still be possible. More commonly, teams finding themselves managing thousands or tens of thousands of resources that change daily or even hourly. Embracing automation via infrastructure as code is the only way to take control of that kind of complexity.

## What are the key elements of infrastructure as code?

The key elements of infrastructure as code are the same key elements you'd find in the majority of software engineering environments. These include:

1. **An infrastructure as code mechanism:** For all practical purposes, in order to do infrastructure as code you need a tool or engine that is responsible for translating the IaC instructions into something the cloud provider APIs understand and can use. Infrastructure as code tools may be provided by and limited to a single cloud provider (AWS Cloudformation is one example), or may support multiple cloud providers. Tools may be limited to supporting YAML or JSON; may require the use of a specialized and proprietary domain-specific language (DSL); or may support the use of general purpose programming languages such as TypeScript/JavaScript, C#, Go, Python, and Java.
1. **Version control:** When infrastructure is described as code, it can be checked into source control, versioned and code-reviewed using existing software engineering practices. Version control systems, like [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [BitBucket](https://bitbucket.org/), enable you to see _what_ changes were made, _when_ the changes were made, and _who_ made the changes.
1. **Tests:** As any critical system grows in complexity, people can start to feel nervous about making changes. With infrastructure as code, teams can write tests for their infrastructure to ensure its correctness. They can encode policies so that all provisioned infrastructure and its configurations [are compliant](/docs/using-pulumi/testing/property-testing/). Once they're tested, infrastructure components can be reusable pieces of code that capture best practices and that can be shared across teams. No more reinventing the wheel.
1. **CI/CD pipelines:** Assuming the infrastructure as code tool supports the functionality (most do), changes to infrastructure---found in changes to the code that defines the infrastructure---can be deployed using existing CI/CD tools, much in the same way CI/CD pipelines automatically build and deploy other forms of software.

## What benefits does infrastructure as code provide?

Infrastructure as code tames the complexity of cloud infrastructure because it uses the same software engineering principles, approaches, and tools that have enabled other software-based systems to scale up. Here are some of the benefits infrastructure as code provides.

* **Repeatability and consistency**: Infrastructure that is defined via IaC can be deployed in a highly repeatable fashion. Do you need a development environment that is a high fidelity copy of the production environment? Or do you need to ensure that infrastructure is deployed the same across multiple regions? This is easily accomplished with infrastructure as code.
* **Accountability**: Changes to the infrastructure can be easily tracked via the use of version control with your infrastructure as code files.
* **Improved productivity**: Most developers have an integrated development environment (IDE) that they use all the time. When infrastructure is code, you can take advantage of all the features that an IDE offers, such as autocompletion and the ability to look up methods and their parameters.
* **Better alignment among teams**: Infrastructure as code enables infrastructure teams and software development teams to adopt DevOps principles and work together more closely. When infrastructure is code and is integrated into your company's software lifecycle, there's a common language and a common set of practices that stakeholders already understand. That common understanding fosters cross-team collaboration, which is fundamental to DevOps.

## How do I get started with infrastructure as code?

Bringing IaC into a startup or a company with many greenfield applications may not be difficult. For most companies, however, it's not so straightforward. Many companies, both large and small, have a lot of infrastructure that was created by "pointing and clicking" in the console of a cloud provider. Perhaps, over time, someone wrote a run book or created a wiki that describes how to use a cloud provider's console to perform some common task. Maybe even there are Bash or PowerShell scripts, used to manage infrastructure, that are floating around that only one or two people know about (and possibly aren't even being maintained!). What do you do if that's your situation?

Here are steps you can take to get started adopting infrastructure as code.

### Define "good"

<!-- I'm not sure the link in the next paragraph is useful/relevant -->

The first step, even before you begin to [evaluate tools and approaches](/blog/configuring-your-dev-environment/), is to define what "good" looks like to your company. Achieving that ideal doesn't depend on which technology you use. It depends on understanding your company's requirements and what assumptions will remain true regardless of the tools you use. For many companies those assumptions are:

* The amount of infrastructure is going to be high.
* The number of interconnections between managed services will be high.
* The rate of change should be high, in order to take maximum advantage of what your cloud provider(s) offer.
* The number of people who have access to your cloud's capabilities should grow.
* Infrastructure code should be integrated into your continuous delivery system.

A team made up of all the stakeholders is one way to define what your company wants to achieve with its cloud infrastructure.

### Import existing infrastructure

You probably already have a lot of existing infrastructure. Make sure you can [import that existing infrastructure](/docs/using-pulumi/adopting-pulumi/) into your new world. For example, you might have a production database that you want to manage as infrastructure as code. Your tool should let you reliably manage state changes, let you make changes without any downtime, let you test and version those changes, preview the changes, and get pull requests.

### Integrate with existing engineering practices

Assuming your infrastructure code is integrated with your continuous delivery pipeline, you can start instituting the same best practices you use with your application software. For example, to understand your infrastructure's correctness, [you'll need tests](/docs/using-pulumi/testing/). Some tests should run before delivering the infrastructure to ensure that the program is logically correct and that it provisions the infrastructure correctly. Other tests should run when you deploy your infrastructure to ensure that the deployment was successful.

### Think about policies and security

<!-- It would be ideal to link to /docs/using-pulumi/crossguard/ instead of a blog post, but that page isn't well-organized -->

Next, you'll want to enforce policy for the entire organization. That way, you'll have a standard that applies to everyone who builds infrastructure. [Those policies should run against everything anyone does](/blog/benefits-of-policy-as-code/).

It's important to plan policies and security because one of the goals of infrastructure as code is to empower the development teams and give them as much flexibility as possible. Without planning, you may find that you'll create an interface that's so restrictive, teams find ways to go around the platforms. It's a balancing act that requires input from everyone.

### Start small

Any time you make a significant change in technology, you want to do it incrementally. You might start with a new service so you don't disrupt existing ones. Once you've figured out what successful patterns look like, go back and figure out how to transform some existing infrastructure. Pick a project where you'll start seeing value early and then iterate.

## Another look at infrastructure as code

Pulumi's YouTube series, A Quick Bite of Cloud Engineering, tackled the topic of infrastructure as code (IaC) in this video. Have a look!

{{< youtube "WhWf48kcEXU?rel=0" >}}

## Learn more

Pulumi offers a truly modern approach to infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
