---
title: "Pulumi Patterns and Practices Platform (P3): A reference architecture for
  large-scale organizations"
allow_long_title: true
date: 2024-08-05
draft: false
social_media: "TBD"
meta_desc: "Pulumi Patterns and Practices Platform (P3) is a reference architecture
  of a Pulumi-based internal platform for infrastructure management and secure deployments
  in a large-scale environment."
meta_image: meta.png
authors:
  - troy-howard
tags:
  - platform-engineering
  - patterns-and-practices-platform
  - developer-experience-devex
  - devsecops
  - architecture
  - enterprise
  - devops
search:
  keywords:
    - Platform
    - Architecture
    - Internal Platform
    - Developer Experience
    - Infrastructure Management
---

Infrastructure management is all fun and games until you find yourself scrolling through 1000+ resources in your AWS console. Worse, when one rogue product team wants to use Azure and your data team wants to be on GCP, you're ARM wrestling in Azure and watching your economies of scale tip the wrong direction as you're copy-pasting CloudFormation templates into yet another git repo. This. Needs. To. Be. A. Platform!

<!--more-->

And in that moment of overwhelm, you will be sold to, nurture-emailed every week, and told all your problems will be solved by implementing an IDP (internal developer platform, as if you've never seen this acronym before). An IDP that costs a lot of money and a lot of time to implement beyond default settings. An IDP that really only solves half of your problems. Your internal team offers to build something that feels more like welding together random pieces of code into an abstract found-art sculpture built from junkyard refuse, already 5 years out of date. How long will this investment be useful before you have to start over?

It's exhausting. If there was a good solution on the market, you wouldn't be reading this article. So let's talk about what you really need, and how Pulumi can help.

## An effective internal developer platform

There are quite a few [listicles](https://en.wikipedia.org/wiki/Listicle) out there professing to authoritatively tell you the 5, or 7, or 11 essential components of an internal developer platform. Personally, I trust our customers to tell us, and here's what they have said they need:

**[Consistency:](/blog/pulumi-patterns-and-practices/#consistency)** Bring some order to the chaos. As your company and your infrastructure grows, it gets more and more complicated to maintain consistency. You might already have established design patterns that you want to replicate, but don't have any way to encode those practices in your current tools. There's a lot of copy/paste of reusable blocks, but no way to apply [DRY principles](https://www.youtube.com/watch?v=5xw04T20lto&t=7s) or to modularize/templatize the important parts (hint: all the parts are important!).

**[Reproducibility:](/blog/pulumi-patterns-and-practices/#reproducibility)** Repeatable behaviors, who dat? If you run your deploy twice do you get the same results each time? What if you replicate your production environment to create a test environment, are they actually identical? How much more work does it take to get them to be? Will you get the same version of the training dataset every time you run your AI workloads? It's anyone's guess. A lack of reproducibility slows down development, makes debugging more difficult, and makes that reuse we just talked about harder to achieve.

**[Visibility:](/blog/pulumi-patterns-and-practices/#visibility)** When your node count, and user count starts to go beyond about 50-100 resources (computing or human) you quickly run into a problem of visibility. It can be very difficult to get a handle on what's happening, how many resources you have, where they are, and how much they cost. Any system that purports to be able to manage 1000 nodes or more must have deeply integrated analytics, dashboards, charts, and be searchable, across all your clouds, all your users, and every kind of resource.

**[Security and Compliance:](/blog/pulumi-patterns-and-practices/#security-and-compliance)** Good fences make good neighbors. RBAC, policy-as-code, excellent secrets management, integration with your existing identity providers. These are the things you need to build security and policy guardrails you can rely on. Without them? It's just a powder keg of liability waiting to catch a spark.

**[Auditability:](https://www.pulumi.com/blog/pulumi-patterns-and-practices/#auditability)** What happened and who did it? This is like a high-stakes game of [Clue](https://en.wikipedia.org/wiki/Cluedo). How quickly can you figure out who ran that bad deployment? Was it *Colonel Mustard* in the *library* with the *candlestick*? Or Blake the new Front-End Developer with overly-broad permissions in AWS? Being able to answer these questions needs to happen quickly. Quickly, like minutes, not hours or days. And it might have happened 6 months ago. Oof.

**[Developer Experience:](https://www.pulumi.com/blog/pulumi-patterns-and-practices/#auditability)** In the ideal world, developers drive their own DevOps. The platform team provides self-service tools and streamlined workflows that allow your engineers to provision new resources, so your team doesn't have to. And you know, if the developers don't like the user experience, they won't use it at all, and will invent their own tools. You will have ROGUE SYSTEMS to hunt down and argue against in tedious overly-technical meetings. This is not what you want. We need to keep the developers happy to prevent this.

## A holistic view of the Patterns and Practices Platform reference architecture

Pulumi has a broad surface area of [products and features](https://www.pulumi.com/product/) that address these needs. Designed with integration in mind from the beginning, our tools orchestrate well, presenting a smooth and streamlined workflow for both operations teams and developer teams.

We have an idea of how you can use all the Pulumi products together to deliver a comprehensive internal platform for security, infrastructure management, and deployments. Call it an [internal platform for developer platform engineers](https://www.pulumi.com/what-is/what-is-platform-engineering/) (IPfDPE), if you want. We call it the realization of a vision we've been working hard to build for many years.

**Pulumi Patterns and Practices Platform (P3)** is a reference architecture that we will be describing, and providing code for, through this series of articles. We'll be diving deep into not just what you can do with our tools, but how to do it, and provide code for a reference implementation that you can use to jump start the process.

Here's a quick overview to give you an idea of how we'll be addressing those needs in Pulumi Patterns and Practices Platform (P3).

### Consistency

Pulumi can help bring consistency to your software catalog by encoding design patterns into reusable *[component resources](https://www.pulumi.com/learn/abstraction-encapsulation/component-resources/)* and by building custom *[organization templates](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/)* that provide a no-code or low-code way to start a new project. Templates help get projects off the ground faster and ensure consistent code structure, policy compliance, and best practices.

<figure>
{{< video title="The New Project Wizard in Pulumi Cloud" src="npw-720p.mp4" controls="false" autoplay="true" loop="true" >}}
  <figcaption><p>Figure: An internal developer portal using custom templates in Pulumi Cloud</p></figcaption>
</figure>

Beyond that, because Pulumi is [multi-cloud](https://www.pulumi.com/blog/deploy-to-multiple-regions/) (AWS, Azure, Google Cloud, and more) and [multi-language](https://www.pulumi.com/blog/pulumiup-pulumi-packages-multi-language-components/) (JavaScript, Python, Go, C#, Java) you can enjoy the same consistency across all your environments and all your developer teams, regardless of the languages they prefer, or cloud tooling they need.

Another core aspect of consistency is *[drift detection](https://www.pulumi.com/docs/pulumi-cloud/deployments/drift/)*. Pulumi automatically detects and remediates cloud resources that have deviated from the expected state stored in Pulumi Cloud. This tech is better than ibuprofen at getting rid of developer-created headaches.

### Reproducibility

Since 2010, scientists have felt that we are in a crisis – a *[reproducibility crisis](https://en.wikipedia.org/wiki/Replication_crisis)* – wherein we cannot easily reproduce an experiment in order to verify published results. Similarly, the software industry is entering into a reproducibility crisis of its own, especially around AI training workflows, where it is increasingly difficult to recreate crucial build and prod environments. [Pulumi Stacks](https://www.pulumi.com/learn/building-with-pulumi/understanding-stacks/) make it very easy to manage both configuration and state across multiple environments, and make [reproducing a deployment](https://www.pulumi.com/blog/simple-reproducible-kubernetes-deployments/) within Pulumi a matter of a few basic operations.

You can use Pulumi programs to capture ***all*** of the necessary resources for an AI training workload, including things like [versioned data](https://www.pulumi.com/ai/answers/xig35anR7ibjAP5MhHDyxC/time-travel-queries-on-snowflake-dynamic-tables) using dynamic tables with time-travel functionality in [Snowflake](https://www.pulumi.com/case-studies/snowflake/). That means you can be sure that not only will your deployment be on the infrastructure you need, it will also have the exact version of data, every time, which is essential to A/B testing and debugging your models.

### Visibility

Every resource under management by Pulumi is visible within [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/). From this single-pane-of-glass interface, you can search for resources across all cloud environments. [Pulumi Copilot](https://www.pulumi.com/product/copilot/) provides a state-of-the-art AI chat interface to ask complex questions and get immediate results. Pulumi Insight's analytics gives you the ability to identify anomalies or trends in resource usage and dig into cost, security, and compliance concerns.

{{< figure src="https://www.pulumi.com/uploads/pulumi-insights-search.gif" caption="Figure: Search for any resource with Pulumi Insights">}}

### Security and Compliance

In the modern parlance, when you say DevOps, you mean DevSecOps. Pulumi is designed to be secure by default. Pulumi Cloud offers full [role-based access control (RBAC) functionality](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/) including deep integration with [GitHub teams](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/#github-based-teams) and [SAML-based SSO](https://www.pulumi.com/docs/pulumi-cloud/access-management/saml/), managed secrets and flexibly-defined secure environments with [Pulumi ESC](https://www.pulumi.com/product/esc/), and policy-as-code provided by [Pulumi Crossguard](https://www.pulumi.com/crossguard/). Most importantly all of these features are deeply integrated across the platform, creating an air-tight system with all the guardrails you need for managing security and access.

### Auditability

Every action a user takes in Pulumi can be tracked via the [audit log](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/) which is searchable in two clicks from the Pulumi Cloud homepage dashboard. Audit logs can be filtered by user with one more click. Creating automated backups of your audit logs is a [first-class feature](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/#automated-export). You will never have to worry about responding quickly when someone asks about an event that happened in your system. Also, each deployment and update has logs directly visible from the Pulumi Cloud app, regardless of how it was initiated.

{{< figure src="/images/docs/guides/self-hosted/auditlogs.png" caption="Figure: Viewing the audit log in Pulumi Cloud">}}

### Developer Experience

Probably the most compelling aspect of Pulumi is the developer experience. [Developers love Pulumi](https://www.pulumi.com/testimonials/), because they get to use their preferred tools. General purpose programming languages, visual IDEs, command-line tools, and products with an API-driven architecture are what developers want, and it's what Pulumi delivers in spades.

With Pulumi templates and custom internal component resources in place, [developers can drive their own DevOps](https://www.pulumi.com/blog/software-developer-experience-devex-devx-devops-culture/#how-does-devex-intersect-with-devops), provisioning their own infrastructure resources and managing their own deployments directly, reducing bottlenecks in platform teams. Product engineering teams can self-service with a stream-lined workflow that stays compliant with company policy by default. Deep in the code of their favorite programming languages, your developers will never even know they are following the company rules.

{{< figure src="pulumi-ide.png" caption="Figure: Using C# to write a Pulumi program in VS Code">}}

### More to Come

So now that we've made a case for how Pulumi can be applied to meet the most pressing needs of a larger organization, hopefully you will realize that the Pulumi Patterns and Practices Platform (P3) reference architecture we are presenting here is more than just infrastructure-as-code. P3 is a Pulumi-powered platform for teams, where your developer portal is not just a catalog of software, but a fully functional control-plane across all your cloud environments.

Stay tuned for the following series of posts where we will use Pulumi to implement the P3 reference architecture for a fully-featured internal developer platform (IDP, or IPfDPE if you prefer). That said, you may already have invested in some popular in cloud-native tools like [Backstage](https://www.pulumi.com/blog/pulumi-in-a-cloud-native-world/#the-kebap-stack-reference-architecture) or [Kubernetes](https://www.pulumi.com/blog/kubernetes-4-0-even-more-kubernetes-native/). Pulumi plays well with others, and you will be delighted to see [how you can use Pulumi to cover the gaps](https://www.pulumi.com/blog/pulumi-in-a-cloud-native-world) in the [CNCF](https://www.cncf.io/) ecosystem.

And if you are already ready to get your hands on Pulumi after this introduction, feel free to [create an account](https://www.pulumi.com/signup/) and follow some of our [Getting Started](https://www.pulumi.com/docs/get-started/) guides to see how easy simple use cases are and begin to imagine how that same developer experience will scale up to your entire organization.

To learn more, you can watch the following video which provides a high level overview of how Pulumi works:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/Q8tw6YTD3ac?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Introduction to Pulumi in Three Minutes"
        srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img{position:absolute;width:100%;top:0;bottom:0;margin:auto}</style><a href=https://www.youtube.com/embed/Q8tw6YTD3ac?autoplay=1><img src='/images/home/youtube-getting-started.png' alt='Introduction to Pulumi in Three Minutes'></a>">
    </iframe>
</div>

## Pulumi Cloud

The Pulumi Cloud is a fully managed service that helps you adopt Pulumi's open source SDK with ease. It provides built-in state and secrets management, integrates with source control and CI/CD, and offers a web console and API that make it easier to visualize and manage infrastructure. It is free for individual use, with features available for teams.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>
