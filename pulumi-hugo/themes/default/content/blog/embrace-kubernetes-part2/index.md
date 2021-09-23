---
title: "It’s Time to Embrace Kubernetes! Really? (Part 2)"
date: 2020-12-11
meta_desc: "How to evaluate your choices when choosing Kubernetes as your application platform."
meta_image: embrace-k8s.png
authors:
    - lee-briggs
tags:
    - kubernetes

---

In the [first article]({{< relref "/blog/embrace-kubernetes-part1" >}}) in this series,  we gave you some questions to help you and others at your company decide if Kubernetes is right for you. In this post, we’ll give you an example of where Kubernetes can be a good fit.

<!--more-->

## When is Kubernetes a Good Choice?

If you’ve decided your company can make the large investment of time and resources required to adopt Kubernetes, when is it the right choice? A well designed, well implemented Kubernetes platform can certainly deliver value to your customers. It does a fantastic job of reducing complexity from the application developers’ jobs. Just remember that the payoff, although dramatic, will be many months away and, before that, things will be slower than you’re used to.

One example of where Kubernetes can add a lot of value is when the application side of the engineering organization has a low level of maturity, and the operations side has a high degree of maturity. Kubernetes can make the applications developers jobs easier because it abstracts away deployment details. In turn, the operations team must be willing to take on the burden of shipping software and let the application developers concentrate on creating new products and features. This division implies a good relationship between them, and fostering cooperation is always beneficial. If trust and good communication exist, Kubernetes is a great way for engineers to work together.

Here’s one example of how Kubernetes can help. Developers spend large amounts of time writing code that’s resilient to failure. Kubernetes, on the other hand, almost encourages you not to spend time writing fault-tolerant software and let the Kubernetes handle failure. Application developers don’t need to write resiliency into their applications. They can simply let the programs fail quickly and assume that Kubernetes will take care of it.

## Are There Alternatives?

Asking if there are alternatives to Kubernetes makes sense, but it’s unlikely you’ll find a simple solution. Large-scale, complex problems won’t be solved easily. Most open-source alternatives can’t compete against it because Kubernetes is generic and has many building blocks available.

Another approach is to build your own solution. One example is to rely on raw compute power and spinning VMs in and out very quickly. In this case, you’ll need to decide if you’re getting value for your money because you may not be using the entire VM or sizing it correctly, which Kubernetes does for you.

You’ll also need to build the basic building blocks, as well as the glue that ties everything together. That glue can be anything from a set of shell scripts to a very, very complex orchestration framework. The industry was in this mode for at least 10 years and there were many problems with this approach, particularly at scale. So, even if you think that the Kubernetes tooling is insufficient, you’ll run into similar problems with the DIY approach.

## Picking a First Project

Most medium to large organizations run multiple applications, and some of them are only used internally. A good way to start with Kubernetes is to pick an internal application that’s not mission-critical. Migrating that application to Kubernetes will give you a feel for what the experience will look like. You’ll be able to identify the gaps, the things that you like, and the potential problems.

So, start small and give yourself the time to learn. Once you feel comfortable, evaluate if Kubernetes is right for your company. If it is, then you can start to move things over gradually

## Summary

To summarize, Kubernetes isn’t for everyone but, where it’s a good fit, it has a lot to offer. Keep these questions  in mind:

**[ ] Do you understand your current and future requirements?**
Kubernetes is a popular solution but does adopting it serve the needs of your organization and customers?

**[ ] What’s the size of your organization?**
Kubernetes is a better fit for medium and large organizations. Startups and smaller  companies should take a look at off-the-shelf options.

**[ ] Where does your organization sit in its adoption of DevOps?**
Your organization must be well along in its adoption of DevOps principles such as collaboration, good communication, trust, and the ability to work for the good of the entire company.

**[ ] Do you really need to change your infrastructure?**
Does your current solution allow you to deliver features to your customers quickly, easily, and reliably? Ask yourself the questions, “Is what we have truly broken? Do we really need to fix it?”

**[ ] Do you have the resources?**
Changing technology stacks is a time and resource intensive task. Do you have the budget, the buy-in from leadership, and discipline to switch to a new technology stack?

**[ ] Do you have the people?**
A robust Kubernetes implementation demands a deep understanding of its multi-layer architecture. Do you have the engineers and subject matter experts to maintain and fix problems?

**[ ] Can you afford the technical debt?**
Can your organization redirect engineers who maintain your current systems to a Kubernetes implementation that can take a year or more before it’s operational?

**[ ] Can you afford the extra infrastructure?**
Implementing a Kubernetes solution is not an overnight change. It's common to run the existing solution alongside Kubernetes before fully adopting Kubernetes. Does your organization have the budget and support people to manage this change smoothly? Remember, you are, at minimum, doubling the size of your infrastructure.

## Learn More

If you’ve looked at [Get Started with Kubernetes]({{< relref "/docs/get-started/kubernetes" >}}) and want to learn more about how Pulumi can help you with your implementation, take a look at [Kubernetes Overview]({{< relref "/registry/packages/kubernetes" >}}) and [Getting Started with Kubernetes: Application Basics]({{< relref "/blog/getting-started-with-k8s-part2" >}}).
