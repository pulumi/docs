---
title: What is Infrastructure as Code (IaC)?
meta_desc: Infrastructure as Code (IaC) manages cloud infrastructure using code and automation. Learn how IaC works, key benefits, and get started with examples.
type: what-is
page_title: "What is Infrastructure as Code?"
---

**Infrastructure as Code (IaC) manages and provisions infrastructure using code and automated processes, rather than manual configuration. IaC enables teams to define, version, test, and deploy infrastructure changes reliably through version control systems and CI/CD pipelines.**

Infrastructure as code (IaC) is an approach to automating the provisioning and management of infrastructure. At its heart, infrastructure as code is about bringing software engineering principles, approaches, and tools into the cloud infrastructure space.

Before infrastructure as code, infrastructure was (and in some cases still is!) provisioned in a variety of ways, such as by pointing and clicking in a user interface (UI), by running commands via a command-line interface (CLI), by running batch scripts, or by using configuration management tools that may not have been designed with cloud infrastructure in mind. Each of these methods falls short in some way; interactive methods involving a UI or a CLI often create problems with repeatability and consistency while batch scripts or configuration management tools may be unable to declaratively manage infrastructure. Today, modern approaches use platforms, such as [Pulumi](/), which embrace and support the full software engineering lifecycle.

## How Infrastructure as Code Works

Infrastructure as Code fundamentally changes how we manage cloud resources by treating them as software. This approach involves several key components working together:

**Code-based Definitions:** Infrastructure is defined using configuration files written in code—whether that's TypeScript, Python, Go, C#, Java, or YAML. These files describe the desired state of your cloud environment in a declarative way. Instead of writing step-by-step instructions (imperative), you describe what you want the end result to be, and the IaC tool figures out how to achieve it. This declarative approach means you can focus on the "what" rather than the "how," making infrastructure definitions clearer and more maintainable.

**Automation and Orchestration:** IaC tools like Pulumi automate the entire deployment process. They read your code, understand the dependencies between resources, and create them in the correct order. If a database needs to exist before an application server can connect to it, the tool handles that sequencing automatically. This automation extends to updates as well—when you change your infrastructure code, the tool determines what needs to be modified, replaced, or removed, and executes those changes in the correct sequence. This eliminates manual steps and reduces human error significantly.

**Version Control Integration:** All infrastructure definitions are stored in version control systems like Git, GitHub, or GitLab. This provides complete audit trails of all infrastructure changes, the ability to review changes before they're applied, instant rollback to previous configurations if issues arise, collaboration through pull requests and code reviews, and branch-based development workflows for testing changes.

**Continuous Testing:** Infrastructure code goes through the same rigorous testing as application code. Teams write unit tests to validate individual components, integration tests to verify system interactions, and compliance tests to ensure security and regulatory requirements are met. This testing happens automatically before any changes reach production, catching issues early in the development cycle when they're easier and less expensive to fix.

## Key Benefits of Infrastructure as Code

The adoption of Infrastructure as Code provides transformative benefits for organizations managing cloud infrastructure:

**Speed and Efficiency:** What once took hours or days of manual configuration now happens in minutes. IaC automates the entire provisioning process, from creating networks and compute instances to configuring security rules and deploying applications. Teams can spin up complete environments with a single command, enabling rapid prototyping and reducing time-to-market for new features. This speed extends to disaster recovery scenarios as well—entire infrastructures can be recreated quickly in new regions if needed.

**Consistency and Repeatability:** Every deployment happens exactly the same way, every time. Whether you're creating a development environment or deploying to production, IaC ensures identical configurations. This eliminates the "works on my machine" problem that has plagued software development for decades. Configuration drift—the gradual divergence of environments over time—becomes a thing of the past when infrastructure is defined in code and regularly reconciled.

**Reduced Errors:** Manual configuration is prone to mistakes—a mistyped IP address, a forgotten security rule, or an inconsistent setting across environments. IaC eliminates these human errors by codifying best practices and automating their application. When changes are needed, they're reviewed through pull requests, tested automatically, and applied consistently across all environments.

**Enhanced Scalability:** Scaling infrastructure becomes as simple as changing a number in code. Need to go from 2 servers to 200? Update the configuration and deploy. The same applies to scaling down—resources can be decommissioned just as easily, preventing unnecessary costs. This elasticity enables organizations to respond quickly to changing demands without the operational overhead traditionally associated with scaling.

**Complete Audit Trails:** Every infrastructure change is tracked in version control, providing a complete history of who changed what, when, and why. This audit trail is invaluable for troubleshooting issues, meeting compliance requirements, and understanding how your infrastructure has evolved over time. Unlike manual changes that might go undocumented, every IaC modification is automatically recorded.

**Improved Collaboration:** Infrastructure as code breaks down silos between development and operations teams. When infrastructure is defined in code, developers can understand and contribute to infrastructure decisions, while operations teams gain visibility into application requirements. This shared language and toolset fosters better communication and more effective problem-solving across traditional organizational boundaries.

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

## Core Elements of Modern Infrastructure as Code

The key elements of infrastructure as code mirror those found in mature software engineering practices:

**Version Control:** When infrastructure is described as code, it gains all the benefits of modern version control systems. Teams can track changes, understand history, and collaborate effectively. Version control systems like [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [BitBucket](https://bitbucket.org/) enable you to see what changes were made, when they were made, and who made them. This visibility is crucial for maintaining large-scale infrastructure. Teams can use branching strategies to test changes in isolation, merge requests to review infrastructure modifications, and tags to mark specific versions for deployment.

**Testing:** Infrastructure testing has evolved to match the sophistication of application testing. Teams write unit tests to validate individual resource configurations, integration tests to verify components work together correctly, [policy tests to ensure compliance](/docs/iac/concepts/testing/property-testing/) with security and regulatory requirements, performance tests to validate scalability assumptions, and smoke tests to verify basic functionality after deployment. These tests run automatically in CI/CD pipelines, catching issues before they reach production. The result is infrastructure that's not just functional, but proven to be correct.

**CI/CD Pipelines:** Infrastructure deployments flow through the same continuous integration and continuous deployment pipelines as application code. This integration enables automated testing on every change, preview environments to see changes before applying them, approval workflows for production deployments, gradual rollouts to minimize risk, automatic rollback capabilities if issues are detected, and integration with monitoring and alerting systems.

**Infrastructure as Code Tools:** The IaC ecosystem offers various tools to meet different organizational needs. Cloud-specific tools like AWS CloudFormation excel at deep integration with a single provider, offering native support for all services. Multi-cloud tools like Pulumi enable management across multiple providers, avoiding vendor lock-in. Language support varies from simple YAML/JSON configurations to full programming languages like TypeScript, Python, Go, C#, and Java. State management approaches differ, with some tools managing state automatically while others require manual configuration.

## Infrastructure as Code in Practice

Here's a real-world example demonstrating how Infrastructure as Code works with Pulumi. This example creates an EC2 instance with a security group, showing how multiple cloud resources work together:

{{< example-program path="aws-ec2-instance-with-sg" >}}

This example demonstrates several important IaC concepts:

**Resource Creation:** Both a security group and an EC2 instance are defined in code, showing how infrastructure components are declared as objects in your programming language.

**Dependencies:** The EC2 instance automatically depends on the security group through the vpcSecurityGroupIds reference. Pulumi understands these relationships and creates resources in the correct order.

**Configuration as Code:** Security rules, instance type, and AMI are all specified declaratively. Changes to these values in code will be reflected in your infrastructure when deployed.

**Output Values:** Important information like the instance's public IP and DNS are exported, making them available for other systems or team members to use.

To learn more about creating cloud infrastructure with Pulumi, check out our [getting started guide](/docs/iac/get-started/aws/).

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

You probably already have a lot of existing infrastructure. Make sure you can [import that existing infrastructure](/docs/iac/adopting-pulumi/) into your new world. For example, you might have a production database that you want to manage as infrastructure as code. Your tool should let you reliably manage state changes, let you make changes without any downtime, let you test and version those changes, preview the changes, and get pull requests.

### Integrate with existing engineering practices

Assuming your infrastructure code is integrated with your continuous delivery pipeline, you can start instituting the same best practices you use with your application software. For example, to understand your infrastructure's correctness, [you'll need tests](/docs/iac/concepts/testing/). Some tests should run before delivering the infrastructure to ensure that the program is logically correct and that it provisions the infrastructure correctly. Other tests should run when you deploy your infrastructure to ensure that the deployment was successful.

### Think about policies and security

<!-- It would be ideal to link to /docs/using-pulumi/crossguard/ instead of a blog post, but that page isn't well-organized -->

Next, you'll want to enforce policy for the entire organization. That way, you'll have a standard that applies to everyone who builds infrastructure. [Those policies should run against everything anyone does](/blog/benefits-of-policy-as-code/).

It's important to plan policies and security because one of the goals of infrastructure as code is to empower the development teams and give them as much flexibility as possible. Without planning, you may find that you'll create an interface that's so restrictive, teams find ways to go around the platforms. It's a balancing act that requires input from everyone.

### Start small

Any time you make a significant change in technology, you want to do it incrementally. You might start with a new service so you don't disrupt existing ones. Once you've figured out what successful patterns look like, go back and figure out how to transform some existing infrastructure. Pick a project where you'll start seeing value early and then iterate.

## Frequently Asked Questions

### What is Infrastructure as Code?

Infrastructure as Code (IaC) is the practice of managing and provisioning cloud infrastructure through machine-readable code files rather than manual configuration, enabling consistent, repeatable, and automated infrastructure deployment.

### How does IaC differ from configuration management?

While configuration management tools (Chef, Puppet) focus on configuring existing servers, Infrastructure as Code provisions and manages the infrastructure itself - creating servers, networks, databases, and other cloud resources from scratch.

### What programming languages does Pulumi support for IaC?

Pulumi supports TypeScript, JavaScript, Python, Go, C#, Java, and YAML, allowing teams to use languages they already know rather than learning proprietary DSLs.

### Why is Infrastructure as Code important for DevOps?

IaC enables DevOps practices by treating infrastructure the same as application code - with version control, testing, code reviews, and CI/CD pipelines, breaking down silos between development and operations teams.

## Another look at infrastructure as code

Pulumi's YouTube series, A Quick Bite of Cloud Engineering, tackled the topic of infrastructure as code (IaC) in this video. Have a look!

{{< youtube "WhWf48kcEXU?rel=0" >}}

## Learn more

Pulumi offers a truly modern approach to infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).

There are many other practices related to infrastructure as code, read more:

* [What is Secrets Management?](/what-is/what-is-secrets-management)
* [What is Platform Engineering?](/what-is/what-is-platform-engineering)
* [What is Infrastructure as Software?](/what-is/what-is-infrastructure-as-software)
