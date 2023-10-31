---
title: "Infrastructure as Code in Any Programming Language"
canonical_url: https://thenewstack.io/infrastructure-as-code-in-any-programming-language/
date: 2023-10-31T22:36:29Z
draft: false
meta_desc: Not every engineer has a deep infrastructure background and yet needs to get more hands-on with it these days. That’s where Infrastructure as Code can help.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

authors:
    - joe-duffy
tags:
    - infrastructure-as-code
    - fundamentals


---

*This is the first of a three-part series originally published on The New Stack.*

[Infrastructure as Code](/what-is/what-is-infrastructure-as-code/) is a technology for automating the infrastructure for your cloud applications. If you’re an engineer, whether that’s developing a backend service or within a central platform team, it’s not just about writing application code. You’ll need to provision, update and perform other tasks associated with its supporting infrastructure, and that’s where Infrastructure as Code can help. Instead of manually pointing-and-clicking in the cloud console, which is unrepeatable and error-prone, or writing ad-hoc scripts, which can be tedious and hard to scale, Infrastructure as Code lets us, as engineers, use familiar techniques by just writing code.

Not every engineer has a deep infrastructure background and yet needs to get more hands-on with infrastructure these days, which is OK: This three-part series was written from an engineer’s point of view. In it, we will demystify Infrastructure as Code — the why, what, and how — through the lens of Pulumi, a popular Infrastructure as Code tool among engineers.

## Why We Need Infrastructure as Code

Modern applications need cloud infrastructure to run. That is equally true for simple monolithic applications running on virtual machines as it is for exotic distributed serverless applications that are fully elastic in scale. The applications themselves need infrastructure that they directly use, like whatever they run within (such as virtual machine, containerized service, serverless function, static website) in addition to any other resources they consume (databases, pub/sub topics, queues, AI/ML services, observability metrics and dashboards), but also depend on more primitive infrastructure to run atop (Kubernetes clusters, security roles and permissions, private networks, load balancers, encryption keys and more).

The phrase “cloud infrastructure” is also broader than it may seem. This phrase evokes immediate thoughts of popular clouds like Amazon Web Services (AWS) , Microsoft Azure, and Google Cloud, as well as more specialized or regional ones like Alibaba Cloud, DigitalOcean and Oracle Cloud. It also quickly leads to cloud native infrastructure like Docker, Kubernetes and Helm. But this phrase also perhaps not obviously applies to modern software-as-a-service (SaaS) infrastructure companies who increasingly are supplying critical pieces of cloud infrastructure, including Confluent, Cloudflare, Databricks, DataDog, Elastic, MongoDB, New Relic and Snowflake.

These companies are essentially specialized clouds providing more specialized services but are increasingly expanding to become clouds of their own. It also applies to private cloud technologies like F5, VMware vSphere and related technologies. Finally, also not obviously, there are SaaS tools that have configurable state that we use every day and may want repeatable management of just like our other cloud assets, including Auth0, GitHub, GitLab and PagerDuty.

Cloud infrastructure’s reach is far and wide! But it also means that there are many complex moving pieces to manage and tame. And with so much innovation happening in cloud capabilities, that complexity is just growing with time. This begs questions like the following:

Where does the infrastructure come from? How do we change it as our requirements evolve? How do we scale it as our needs grow, whether that’s increasing the compute and memory available to our workloads, scaling to many new instances, increasing our availability and reducing latency by deploying to new regions and environments worldwide… or, as is usually the case, a combination of all of these?

How do we ensure our infrastructure practices are repeatable in the event something fails or a mistake is made? How do we capture and reuse best practices? Do the answers to these questions differ across clouds? How do we ensure collaboration can take place safely and our deployments aren’t flaky and prone to colliding? And how do we secure all of it and ensure best practices and policies are enforced at all times?

These are all things that Infrastructure as Code solves, and it starts with code.

## Benefits of Infrastructure as Code

The Infrastructure as Code approach provides many benefits, but they fall into two primary categories:

1. Using code to declare infrastructure
2. Using a declarative engine to orchestrate infrastructure changes

It is the combination of these two things that leads to the magic of “Infrastructure as Code.”

## The Benefits of Code

Encoding your cloud application infrastructure in code results in a durable artifact representing your desired architecture. This can be code-reviewed, committed to source control and versioned in the usual ways. Infrastructure as Code tools not only know how to stand up the initial version of your infrastructure, but can replicate it across many environments (like dev, staging, prod and multiple regions), in addition to upgrading individual environments as your requirements evolve.

In terms of the “code” aspect, the expression of your code varies across the Infrastructure as Code landscape. Some tools support markup languages like JSON or YAML, while others support domain-specific languages (DSLs) that are specific to that tool. In this article, we will use Pulumi, which takes a unique approach to Infrastructure as Code that is well-suited for engineers: namely you use industry-standard general-purpose languages, including C#, Go, Java, JavaScript, Python or TypeScript, to express your code. This approach is great for engineers because it makes infrastructure more accessible and lets you use standard engineering tools and practices that you’re already using to build other software in your team.

Examples of these benefits include having rich constructs like simple if-statements and for-loops, which help avoid repetition and model complex infrastructure needs. Since all of these languages are broadly supported throughout the industry, virtually any editor you pick up will have great support, such as Visual Studio Code, PyCharm, Sublime Text, IntelliJ or even vim or emacs. That means you’ll get interactive statement completion, red squiggles if you make a typo or have a type-checking error, documentation as you hover, right-click to go to definition or refactor, and so much more. It’s easy to take these things for granted, but they are essential for software engineering productivity.

There are other benefits still such as linters, testing tools, the ability to share and reuse with package managers rather than copy-and-pasting and more. Lastly, each of these languages has enormous communities that add up to more than 20 million engineers, which means there’s a wealth of knowledge and support available.

It turns out [Pulumi supports YAML](/blog/pulumi-yaml/) too — the L in YAML stands for language, after all — which is a fine choice for simple scenarios, those where you want to machine-generate your Infrastructure as Code, or when engineers want to enable their sysadmins to do Infrastructure as Code too.

## The Benefits of Declarative

Code is one major benefit. But in addition to the benefits of code, Infrastructure as Code has another significant advantage: It is “declarative,” even if you’ve chosen an imperative language like Go to express your code.

Infrastructure as Code tools generally work using a concept called “desired state.” The code, when run, produces a picture of the infrastructure your application requires. The Infrastructure as Code tool then understands how to compare the desired state with reality, and plan a course of action based on that information.

If it’s your first time creating a certain environment, something Pulumi calls a stack, then of course all the declared infrastructure will need to be created from scratch. Upon subsequent evaluations, however, that same infrastructure may need to be updated, deleted or even re-created, in addition to new infrastructure that may get spun up when it’s the first time it has been declared. This plan is presented ahead of performing any actions, so you and your team can review it, and if the course of action is wrong, you can correct it first.

One example of this process would be to first create a microservice environment that includes a Layer 4 network load balancer, a containerized cluster and a replicated, containerized service. You could subsequently add a private container registry, switch to a Layer 7 application load balancer, and scale up the service from one to three replicas.

This declarative approach ensures we can preview changes before they are made so we don’t have any unpleasant deployment surprises, gives us a full audit history of exactly what has changed in our actual infrastructure and when, similar to what source control does for our code artifacts, allows us to gate deployments on verification checks such as testing and policy enforcement, and makes it easier to integrate with various automation workflows.

It’s the codification of infrastructure and repeatability of the declarative approach that lets us use Infrastructure as Code in many kinds of automated workflows. That includes running a command-line interface (CLI) manually or as part of a script. Although “manual” may sound bad, the actual deployment is done with all of the above safeguards, so it’s fairly common for an Infrastructure as Code tool to be run this way.

However, most teams will adopt a CI/CD model for their most important environments, like production, which will trigger the actual deployment of code changes off a code commit. This ensures that all changes have been reviewed in the usual ways and go through a standard CI/CD pipeline. That pipeline may also include continuous verification (CV) such as running tests.

Some Infrastructure as Code tools support just one cloud, but our chosen tool, Pulumi, supports many, [including all of those mentioned above](/registry), so all of these workflows can be standardized across all of the clouds and service providers. It can even track dependencies between cloud services — for example, it would not be strange to provision an Elastic Kubernetes Service cluster in AWS, install Datadog agents on its nodes, deploy some Kubernetes workloads, and place a Cloudflare content delivery network in front of that application, all using a single Infrastructure as Code program.

Pulumi’s unique approach unlocks an even more sophisticated workflow for running your code, using its so-called “[Automation API](/automation/).” This approach embeds Infrastructure as Code workflows right into larger pieces of software so that it can be programmed for highly dynamic scenarios.

This unlocks scenarios like building custom tools and libraries that build on top of and extend Infrastructure as Code, [internal infrastructure provisioning portals](/product/internal-developer-platforms/) and even entire SaaS products that need to provision or manage infrastructure as part of delivering their capabilities to their own end users.

In Part 2 of our series, we will take you through the steps needed to set up Infrastructure as Code. In doing so, we will be using Pulumi’s free and open source SDK, which is available [here](/docs/install/). It’s easy to get started, but you may want to take time now to explore the platform. You might also like to sign up for Pulumi Cloud, which can be done [here](https://app.pulumi.com/signup).
