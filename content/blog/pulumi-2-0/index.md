---
date: "2020-04-21"
title: "Announcing Pulumi 2.0 -- Now with Superpowers"
authors: ["joe-duffy"]
tags: ["Pulumi-News"]
meta_desc: "Today we are announcing Pulumi 2.0, a modern infrastructure as code platform with advanced capabilities including new languages, testing, and policy as code."
meta_image: "pulumi-2-0.png"
---

Today we are excited to announce Pulumi 2.0, the next major stage in our journey as an open source project, company, and community. This release expands on our original vision of using your favorite languages and tools to do all things infrastructure as code, now with new cloud engineering superpowers that will help you and your team adopt modern cloud architectures.

<div class="header-hero-actions mt-8 mb-4 text-center">
    <a class="btn btn-lg mr-2" href="{{< relref "/docs/get-started" >}}">
        Get Started
    </a>
    <a class="btn btn-lg btn-orange ml-2" href="{{< relref "/" >}}">
        Learn More
    </a>
</div>

## What is Pulumi?

Pulumi's approach to modern infrastructure as code is unique:

* **Real Languages**. Use the best languages and tools to declare infrastructure and gain best-in-class productivity and engineering capabilities. Connect to existing communities and ecosystems and leverage world-class language and tooling innovation.

* **Multi-Cloud**. Adopt consistent workflows across any cloud(s) &mdash; public, private, or hybrid &mdash; while still using the full breadth and depth of your target cloud's services.

* **Modern Architectures**. Although Pulumi works great for legacy workloads, it was born in a world of modern container, serverless, and cloud native architectures. Feel free to mix and match these approaches as you modernize over time.

* **Cloud Engineering Teams**. By choosing Pulumi, you're betting on your team. The whole team, in fact: developers, infrastructure and operations teams, and security engineers alike. Tackle cloud solutions together without technology or team silos.

## Introducing Superpowers!

The main theme of 2.0 is something we've taken to calling "superpowers." This isn't just a buzzword we came up with &mdash; it's something we keep hearing from happy end users:

<div class="ml-8">
{{< tweet 1169245701714468864 >}}
</div>

## What is Pulumi 2.0?

Ater [shipping 1.0 last year]({{< relref "/blog/pulumi-1-0" >}}), we've been working hard at work helping customers to succeed at their modern cloud projects. This has taken us beyond the basics to include:

* **Provisioning**. All core language SDKs are now at parity, including all existing languages &mdash; [Node.js (JavaScript, TypeScript)]({{< relref "/docs/intro/languages/javascript" >}}) and [Python](({{< relref "/docs/intro/languages/python" >}})) &mdash; as well as the new additions to the family &mdash; [.NET (C#, F#, etc)](({{< relref "/docs/intro/languages/dotnet" >}})) and [Go](({{< relref "/docs/intro/languages/go" >}})). We've also significantly expanded upon the [supported cloud resource providers]({{< relref "/docs/intro/cloud-providers" >}}), totalling above three dozen, and rolled out [entirely new API documentation]({{< relref "/docs/reference/pkg" >}}).

* **Delivery**. As we've worked with customers to go from development to production, we've added [more CI/CD integrations]({{< relref "/docs/guides/continuous-delivery" >}}) as well as [environment management capabilities to help at scale]({{< relref "/blog/pulumi-service-improvements_02-2020" >}}), such as [project and stack tagging and filtering]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}).

* **Architecture**. Customers are [building their own platforms]({{< relref "/webinars/building-self-service-clouds" >}}) that use abstraction and packaging mechanisms, including our component model, to codify their own best practices. [New coexistence and migration options]({{< relref "/docs/guides/adopting" >}}) help to build larger systems out of many component parts, including those you haven't been able to port to Pulumi yet.

* **Policy**. [Our new policy as code framework, CrossGuard]({{< relref "/docs/guides/crossguard" >}}), lets you define policies using real languages and then apply those policies at deployment-time. This prevents mistakes from ever getting out the door, including cost, security, and compliance. [Configurable policy packs]({{< relref "/docs/guides/crossguard/configuration" >}}) let you write a single policy and apply it flexibly across your projects.

* **Testing**. Many customers are using a spectrum of techniques to [validate their infrastructure in new ways]({{< relref "/docs/guides/testing" >}}). This includes [unit testing using familiar frameworks and new mocking capabilities]({{< relref "/docs/guides/testing/unit" >}}) through [integration testing for short- and long-lived environments]({{< relref "/docs/guides/testing/integration" >}}).

## Welcome to the Team, Pulumipus!

<img src="/images/mascot/pulumipus.svg" style="max-width: 240px; float: right; margin-top: -80px; padding: 4px;">

We're also taking the opportunity to have a little fun with the launch and introducing a new mascot, _The Pulumipus_. You may have met them already at an event or at PulumiHQ, and we're happy to welcome them as the official mascot going forward.

Expect The Pulumipus to pop up from time to time to help you out with your infrastructure superpowers!

## Give it a Try Today

Today is an exciting day for us, our customers, and our community &mdash; your passionate support and feedback shaped this release and we thank you.

To learn more, [join us for our launch event next Wednesday]({{< relref "/webinars/pulumi-update-2020-04-29" >}}), [check out the new superpowers page]({{< relref "/" >}}) with more details and videos, or just [download Pulumi and give it a try]({{< relref "/docs/get-started" >}}).

<div class="header-hero-actions mt-8 mb-8 text-center">
    <a class="btn btn-lg mr-2" href="{{< relref "/docs/get-started" >}}">
        Get Started
    </a>
    <a class="btn btn-lg btn-orange ml-2" href="{{< relref "/" >}}">
        Learn More
    </a>
</div>

Please tell your friends and colleagues &mdash; we will see you in [the Community Slack](https://slack.pulumi.com) where we look forward to hearing what you're doing with your new superpowers!

Joe
