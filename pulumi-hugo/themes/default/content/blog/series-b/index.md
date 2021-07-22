---
title: "Pulumi raises Series B to build the future of Cloud Engineering"
allow_long_title: True
authors: ["joe-duffy"]
tags: ["pulumi-news"]
meta_desc: "Today I'm thrilled to announce that we've raised $37.5 million in a new Series B led by NEA to bring Cloud Engineering to the market."
date: "2020-10-27"
meta_image: "series-b.png"
---

Today I'm thrilled to [announce](https://info.pulumi.com/press-release/series-b-announcement) that we've raised $37.5 million in Series B funding led by NEA with participation from existing investors, Madrona Venture Group and Tola Capital. We will use this funding to continue serving our fast-growing community of developers and infrastructure practitioners, making Cloud Engineering the new reality for organizations embracing the modern cloud in all aspects of how they ship software.

<!--more-->

<blockquote style="font-size: 1.5rem; background-color: #745687; color: #fff; text-align: center">
All software is cloud software,<br>
All developers are cloud developers,<br>
Infrastructure teams enable innovation.
</blockquote>

## Our vision for the modern cloud era

All software is cloud software, all developers are cloud developers, and infrastructure teams enable innovation. This is Cloud Engineering. The cloud has become a competitive advantage for many companies, enabling new disruptive business models and end user experiences. Pulumi aims to enable this new way of building.

We set out over three years ago to fundamentally rethink how teams create cloud software, with a belief that by standing on the shoulders of giants&mdash;leveraging our industry's best languages, tools, and ecosystems for infrastructure&mdash;we could build a platform that uniquely enables developers and infrastructure experts alike to leverage the cloud in new ways. Despite having created languages like C# and TypeScript in our past lives, it struck our founding team that the world didn't need another programming language, DSL, or YAML templating solution; instead, we could unleash creativity and collaboration by embracing the very languages our industry already knows and loves.

This led to Pulumi's [unique approach to infrastructure as code]({{< relref "/docs" >}}), something we often call "[infrastructure as software]({{< relref "/what-is/what-is-infrastructure-as-software" >}})." Bring your own language, fire up your favorite editor, get full access to any or many clouds of your choice, and code away. Use standard libraries, package up and share and reuse your own best practices, or benefit from the community's shared knowledge. Tap into all the goodness surrounding that language including [familiar engineering superpowers]({{< relref "/superpowers" >}}) like refactoring, interactive documentation and error checking in your IDE, debugging, test frameworks, and tools like code formatters and linters. All the while still getting the belts and suspenders of infrastructure as code: plan deployments by previewing them before they happen, get a full history of who deployed what and when, enforce security, compliance, and cost controls using policy as code, and more, all open source with an [easy to use, but optional, SaaS backend]({{< relref "/docs/intro/concepts/state" >}}).

In addition to turbocharging infrastructure as code, this new approach has enabled new ways to program the cloud. When we were starting, we often heard that infrastructure is "too boring" or that general purpose languages instead of YAML was "too powerful." On the contrary, the day that AWS put a REST API in front of spinning up a new virtual machine, the world changed irreversibly forever. By having an entire programming and resource model for interacting with cloud infrastructure, we can layer rich abstractions on top, and build bigger things out of smaller things, as we've always done with operating systems and the hardware/software interface. As a recent example and preview of things to come, [check out our new Automation API]({{< relref "/blog/automation-api" >}}), something that simply isn't possible with traditional YAML, JSON, or DSL-based infrastructure as code approaches.

We also took an approach of integrating with many incredible partners. Pulumi now supports [over 50 infrastructure providers]({{< relref "/docs/reference/pkg" >}}) including AWS, Azure, Google Cloud, Kubernetes, Alibaba, Auth0, Cloudflare, Datadog, Fastly, GitHub, GitLab, MongoDB, New Relic, and more; [over a dozen CI/CD integrations]({{< relref "/docs/guides/continuous-delivery" >}}) including Azure DevOps, CircleCI, GitHub Actions, GitLab CI, Jenkins, Octopus Deploy, and Spinnaker, for seamless and continuous delivery; and many identity providers, including Atlassian, Azure Active Directory, G Suite, GitHub, GitLab, and Okta. We [embraced the Kubernetes ecosystem]({{< relref "/docs/guides/crosswalk/kubernetes" >}}) from day one, with great support for the entire Kubernetes API, managed clusters in all the major clouds (AWS EKS, AKS, GKE, etc.), Helm 2 and 3, Kustomize, Open Policy Agent (OPA)'s Rego language for policy as code, and a Kubernetes Operator, to name a few key features that are helping customers go to production with Pulumi and Kubernetes.

Three years after starting on this journey, [hundreds of customers]({{< relref "/case-studies" >}}) and tens of thousands of end users have used Pulumi to leverage the cloud in transformative new ways, and we regularly hear from developers and infrastructure practitioners about how Pulumi has enabled them to do things previously thought impossible.

## Cloud Engineering is here &mdash; and growing fast

Cloud Engineering is bigger than just Pulumi. Last month, thousands of us tuned in to learn from industry leaders and expert practitioners at [our first annual Cloud Engineering Summit](https://cloudengineeringsummit.com). It is clear that Cloud Engineering is already here in a big way and becoming a standard for the most forward-thinking software teams.

A lot has changed in only three years. At the time we conceived of Pulumi, there was significant fragmentation, uncertainty, and difficulty in adopting Kubernetes, Serverless, Docker, and continuous delivery for production workloads. Developers seldom touched infrastructure. Fast forward to today, and we now have managed container orchestrators, including Kubernetes, across all the major cloud providers, most organizations are shipping daily, and it's evident that mixed workloads of containers, serverless, VMs, and data services are here to stay. And [6.5 million developers have gone cloud native](https://www.cncf.io/blog/2020/08/14/state-of-cloud-native-development/). Teams are now looking for solutions that help them go from idea to production faster than ever before, and Cloud Engineering is emerging as the best way to do just that.

Cloud Engineering teams are also standardizing on platforms and workflows that go beyond ad-hoc "walls of YAML and mountains of Bash" approaches, taming cloud software complexity while also improving reliability and security with technologies like [policy as code]({{< relref "/crossguard" >}}). Teams are also increasingly looking for cloud-agnostic platforms due the reality of multi-cloud, whether that's because they need to ship code to multiple cloud providers, manage Kubernetes resources in addition to cloud infrastructure, manage hosted SaaS infrastructure services by vendors like Cloudflare, Datadog, MailChimp, or MongoDB alongside their cloud infrastructure, or all of the above.

Because all software is cloud software, every software organization in the world needs a Cloud Engineering Platform. We are happy to be that very platform for many of the world's most innovative companies, and look forward to helping many more customers disrupt their own industries as the cloud continues to transform modern businesses.

## What's next?

We remain focused on Pulumi's mission to enable Cloud Engineers of all backgrounds, developers and infrastructure experts alike, to collaborate and do their best work together. We have made great progress in three years, laying a foundation that helps to democratize access to cloud infrastructure. But we're only just getting started.

So, where do we go from here?

We will continue ensuring Pulumi is unquestionably the best infrastructure as code platform available. Features like the Automation API are enabling groundbreaking ways to use cloud infrastructure, powering entire platforms that themselves are powering entire organizations and new cloud products. We are also hard at work creating libraries with built-in best practices, new workshops and educational material, and simpler user experiences, all with the aim of making the cloud easier to use than ever before.

We aren't going to stop there. This foundation also enables new and exciting product experiences. Although all software is becoming cloud software in a meaningful way, the cloud's capabilities aren't yet as easy to harness in our applications as a standard operating system's are. The next phase of our journey will tackle this problem.

Pulumi is and will continue to be the Cloud Engineering Platform powering the world's most innovative companies and teams. All software is cloud software, all developers are cloud developers, and infrastructure teams are central to enabling this innovation&mdash;and this Series B fundraise will help to ensure we realize the full potential of this vision!

I'd like to take a moment to thank our customers. Our community has grown into an inclusive and collaborative place, reflecting our own company values. One of those values says, "our own success is directly enabled by the success of our customers," which we remember every day by helping you transform and innovate. We could not have done it without your support and you will continue to be our guiding light for the future.

To the clouds and beyond!

Joe
