---
title: "Serverless: Is it Really the Future (Part 2)"
date: 2021-04-06
meta_desc: "Serverless is popular because it's fast and cheap, but is it really? This article discusses the pros and cons of serverless architecture."
meta_image: serverless.png
authors:
    - lee-briggs
    - piers-karsenbarg
tags:
    - serverless

---

In our second post about serverless, we'll discuss some broader issues. Again, we’re not trying to be prescriptive. We want to bring up points that will foster discussions among all the stakeholders. Many people who say that all applications will be serverless haven't run their applications at scale and haven't solved all of the problems regarding latency, complexity, and vendor lock-in. That’s what we’re going to talk about here.

<!--more-->

## What about Vendor Lock-in?

How much do you care about vendor lock-in? It's highly likely that you're not going to be able to  move serverless architecture in AWS, for example, to another cloud provider. Some organizations don’t care about vendor lock-in, but many do. If you do care, then deciding how much you care should happen before you go any further.

## How Large Is Your Organization?

Serverless can be a good choice for younger organizations or smaller, perhaps greenfield teams in large organizations where the immediate focus is on delivering value. Once the organization grows large enough to support a team dedicated to managing infrastructure and usage grows, it might be time to reevaluate the situation. Large organizations that have successfully adopted serverless platforms often have undergone cultural shifts to be successful. If you’re not ready to invest heavily at all levels of your organization to make serverless adoption a success, a more traditional approach, where a dedicated team takes control of provisioning infrastructure, might be more appropriate. Finally, as discussed in a previous post, large enterprises might want to consider building an infrastructure platform where technologies like Kubernetes can be beneficial.

## What about Architecture?

A point to consider is the significant differences in mindset between serverless offerings and more “traditional” approaches, which means that applications may often have to be rearchitected when switching platforms.. You might want to consider what the ROI would be on these architectural changes. Often, rearchitecting any application becomes costly, both from a time and financial perspective, and can create problems for even the most successful engineering teams.

Whether you’re developing a greenfield application or evaluating an existing one, it’s important to think about the architecture for a serverless application. The traditional n-tier-styled architecture or n-tier-styled web application will need significant investment to move to a serverless platform.

## Summary

To summarize, serverless isn’t the answer to everything but it has a lot to offer in the right places. Keep these questions  in mind:

**[&nbsp;&nbsp;&nbsp;] How much do you care about vendor lock-in?**<br>
Serverless architectures can’t simply be ported from one cloud provider to another. How much does your organization care about vendor lock-in?

**[&nbsp;&nbsp;&nbsp;] What’s the size of your organization?**<br>
Serverless is often a better fit for smaller organizations. Once you have the IT staff to support it, you might want to look at more traditional options. Large enterprises might want to look at Kubernetes.

**[&nbsp;&nbsp;&nbsp;] Do you care about providing value quickly more than application transparency?**<br>
If you want to get an application to market as quickly as possible, serverless can be a great choice. However, you’ll be sacrificing metrics and insight into your application. This can cause real problems as the scale grows.

**[&nbsp;&nbsp;&nbsp;] Do you understand your application’s profile?**<br>
Serverless is often said to save money since you only pay for the time you use. However, if your application has long response or start-up times, look more closely. Serverless can turn out to be an expensive choice.

**[&nbsp;&nbsp;&nbsp;] What is the architecture of your application?**<br>
Don’t expect traditional end-tier-styled architectures to work well with serverless. Look for applications that can be broken down into smaller components that work together. It also works the other way around—moving a serverless application to a server you control requires that you re-architect the application. Do you have the time and people to do that?

**[&nbsp;&nbsp;&nbsp;] Is serverless a way to bypass IT?**<br>
Using serverless as a way to bypass your IT department may not be the best idea. It’s too easy to put up code that’s non-compliant and vulnerable to attacks. Instead, use the DevOps approach and meet with all the stakeholders to come up with a solution.

**[&nbsp;&nbsp;&nbsp;] What about security?**<br>
Security is problematic with serverless architectures. Cloud providers offer some ready-made options, such as Amazon GuardDuty, but they may have so many constraints limiting the flexibility that serverless offers. Implementing secure serverless applications requires a lot of thought.

## Learn More

If you want to learn more about how, with Pulumi, you can use the languages and tools you already know to implement a serverless architecture, get started with [Serverless In Just a Few Lines of Code](https://www.pulumi.com/serverless/). There are plenty of tutorials, such as [Serverless App Using API Gateways and Lambda]({{< relref "/docs/tutorials/aws/rest-api" >}}).

Also, we mentioned Kubernetes as a possible endpoint for journeys that begin with serverless. If you’re interested in our take on Kubernetes, take a look at our blog posts, “It’s Time to Embrace Kubernetes! Really?” [Part 1]({{< relref "/blog/embrace-kubernetes-part1" >}}) and [Part 2]({{< relref "/blog/embrace-kubernetes-part2" >}}).
