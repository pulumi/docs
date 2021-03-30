---
title: "Serverless: Is it Really the Future (Part 1)"
date: 2021-03-30
meta_desc: "Serverless is ~~a~~ popular because it's fast and cheap, but is it really? This article discusses the pros and cons of serverless architecture."
meta_image: serverless.png
authors:
    - lee-briggs
    - piers-karsenbarg
tags:
    - serverless
---

Many developers say that serverless is the future of computing, while others say that it will never be successful. Our own opinion is less polarized. We see serverless as an option, one possible stepping stone on the journey from startup to a midsize company, to a large enterprise. In these two blog posts, we’ll discuss how serverless fits into that journey, what we see as its strong points, as well as its drawbacks.

<!--more-->

Our goal is to help you evaluate serverless computing realistically. We want to spur discussions rather than promote knee-jerk reactions, whether pro or con. Hopefully, these blog posts will help you frame a discussion among everyone involved to agree on the best course for the business. That course may involve serverless, or it may not. In this first post, we’ll consider a few of the most common concerns when discussing serverless. In the second post, we’ll examine some broader issues.

## What Is Serverless?

The term “serverless” is a bit of a misnomer. The more cynical among you may be muttering, “serverless still runs on servers!” and it’s true. No matter what cloud provider you use, you’re always using servers to run your applications. Those servers have to be provisioned, managed, and maintained. Serverless offerings from cloud providers generally abstract away difficult to manage components of running applications: they run and manage the servers for you. Developers can run their applications without worrying about the layers underneath, like the operating system or even computing power.

## Why Adopt Serverless?

There are a few ready-made answers people give when they promote serverless. We’ll mention them quickly here, and then we’ll examine those claims more closely. Here are the top 3 reasons people give.

### It’s a fast way to get started.

Handing over servers'  management to your provider means you can make your application available to users very quickly. There’s a lot of underlying infrastructure you don’t have to write code for or maintain.

### It’s cheap.

Serverless can save you money in several ways. First, because the provider manages the servers, you might reduce management costs. You also don’t need to write as much code since the servers aren’t your concern. You can get your application to market faster, which means you’ll start generating revenue faster. Finally, depending on your usage model, you only pay for the time you use to execute code. You don’t pay for idle time.

### It’s Out of (IT) Control.

People in organizations that adopt cloud engineering often turn to serverless because they feel that IT is too slow or unresponsive. In a “legacy” organization, it may be difficult to buy hardware, the procurement times may be too slow, or there might be pushback from operations or finance. This is often a reason for people to move to cloud providers and, as part of that move, they may consider using serverless.

You also see serverless adoption in companies that have embraced cloud computing if there are obstacles like strict permissions that get in the way of provisioning cloud resources. Going serverless is an easy way to bypass issues seen as “blockers” to getting work done. Sometimes, the push for serverless can come from departments outside of development. For example, marketing might want to publish something that’s time-critical because it’s tied to an event.

## Or Is It?

Let’s look a little more closely at the reasons people advocate serverless.

### Is It Really a Fast Way to Get Started?

Using serverless may make it easier to get your application to market, but it requires rethinking how you build and develop applications, turning into a labor penalty later on. Traditional practices your organization has adopted when building production applications might need to be rethought and even retooled as you start to leverage serverless offerings. A good example of this is when considering monitoring and observability: many monitoring platforms work at a layer that isn’t accessible to you to get insights into how your application performs. Retooling and rethinking how you build production-ready applications with serverless technologies could introduce unexpected delays into your serverless journey.

### Is it Really Cheap?

One of the reasons serverless is considered cost-effective is that you only pay for the compute time you use. However, it’s not a given that you’ll save money with serverless. It’s important to profile your application to see if it’s a good fit. Here are two considerations.

### What Is the Pattern for Requests?

If your application has many small, fast requests then serverless can be a good choice. If, on the other hand, your application relies on long-running operations, you can be in for a shock when you look at your bill.

### What about Start-up Times?

Remember that you still have to “pay” for the start-up time of your application. Serverless services often have a “cold-start” penalty,  so if you have periods of little to no usage, you may have to run other processes in the background to make sure your application doesn’t pay that penalty. That also means your first request will take longer than subsequent ones. If your serverless function needs to respond quickly at *all times*, you can pay extra for implementations like provisioned concurrency to improve the cold-start penalty. However, this could easily offset any cost savings you might have over traditional methods of deploying software.

## What about Control?

Adopting serverless platforms as a deployment mechanism means you pass the responsibility for patching infrastructure to your provider. You no longer have the ability to react quickly to security advisories at the operating system layer; you’re placing trust in your provider to do that. It may be the case that you don’t want to relinquish that control.

You will still have to manage security advisories in your application dependencies, and you’ll need a mechanism to react to these issues. Often, serverless adopters can be under the mistaken impression that their applications are “secure” because of the lack of infrastructure to manage, but this is very rarely true. Any existing mechanisms you may have adopted for penetration testing your applications will need to be adapted and fitted to any new serverless platform. While you may have a smaller attack surface area, you’ll still need to ensure it’s difficult for any potential attacker to pivot horizontally through your serverless infrastructure.

If you’re opting for serverless because you, or some other department, want to bypass standard IT procedures, then this points to issues within your organization rather than a need for serverless. Technology doesn’t solve cultural problems. What does solve them is for people to talk to each other and figure out how to make life better for everyone concerned.

You must understand that you’re handing control of the server over to the provider, not taking control yourself, and the tradeoff between compliance and the advantages of serverless need to be examined in detail.

## Want to Learn More?

If you’re curious about using serverless, Pulumi gives you a way to implement it using the languages and tools you already know. To get started, check out [Serverless In Just a Few Lines of Code](https://www.pulumi.com/serverless/).
